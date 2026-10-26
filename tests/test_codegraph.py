import io
import json
import os
import sys
import tempfile
import time
import unittest

from codegraph.graph import Graph
from codegraph.server import Server

FILES = {
    "shop/cart.py": "from .pricing import total_price\n\nclass Cart:\n    def __init__(self):\n        self.items = []\n\n    def checkout(self):\n        return total_price(self.items)\n",
    "shop/pricing.py": "TAX = 0.2\n\ndef total_price(items):\n    \"\"\"Sum of item prices including tax.\"\"\"\n    return sum(i.price for i in items) * (1 + TAX)\n",
    "README.md": "# Shop\n\nA tiny shop.\n\n## Checkout\n\nCheckout adds tax to the cart total.\n",
}


class CodegraphTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        for rel, text in FILES.items():
            os.makedirs(os.path.dirname(os.path.join(self.root, rel)), exist_ok=True)
            with open(os.path.join(self.root, rel), "w") as f:
                f.write(text)
        self.g = Graph(self.root).build()

    def tearDown(self):
        self.tmp.cleanup()

    def test_meaningful_chunks(self):
        self.assertIn("shop/cart.py::Cart.checkout", self.g.chunks)
        self.assertIn("shop/pricing.py::total_price", self.g.chunks)

    def test_associations(self):
        kinds = self.g.edges["shop/cart.py::Cart.checkout"]["shop/pricing.py::total_price"][1]
        self.assertIn("calls", kinds)
        self.assertIn("imports", self.g.edges["shop/cart.py::<module>"]["shop/pricing.py::<module>"][1])

    def test_search_follows_associations(self):
        ids = [h["id"] for h in self.g.search("checkout", k=5)]
        self.assertIn("shop/cart.py::Cart.checkout", ids)
        self.assertIn("shop/pricing.py::total_price", ids)  # reached through the call

    def test_memory_and_learned_links_persist(self):
        nid = self.g.remember("Tax rule", "Tax is 20 percent, set by TAX.", links=["total_price"])
        self.assertTrue(self.g.associate("README.md", "shop/pricing.py", "docs describe pricing"))
        g2 = Graph.load(self.root)
        self.assertIn(nid, g2.chunks)
        self.assertIn("note", g2.edges[nid]["shop/pricing.py::total_price"][1])
        self.assertTrue(any("learned" in k for _, k in g2.edges["shop/pricing.py::<module>"].values()))

    def test_refresh_picks_up_edits(self):
        time.sleep(0.01)
        with open(os.path.join(self.root, "shop/pricing.py"), "a") as f:
            f.write("\ndef discount(price):\n    return price * 0.9\n")
        self.assertEqual(self.g.refresh(), ["shop/pricing.py"])
        self.assertIn("shop/pricing.py::discount", self.g.chunks)

    def test_mcp_round_trip(self):
        s = Server(self.root)
        init = s.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        self.assertEqual(init["result"]["serverInfo"]["name"], "codegraph")
        self.assertIsNone(s.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}))
        names = [t["name"] for t in s.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})["result"]["tools"]]
        self.assertIn("search_code", names)
        res = s.handle({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                        "params": {"name": "search_code", "arguments": {"query": "tax"}}})
        self.assertIn("total_price", res["result"]["content"][0]["text"])

    def test_hook_records_web_research(self):
        from codegraph import hook
        event = {"cwd": self.root, "tool_name": "WebSearch", "tool_input": {"query": "vat rates"},
                 "tool_response": {"result": "Standard VAT is 20 percent in the UK."}}
        sys.stdin, old = io.StringIO(json.dumps(event)), sys.stdin
        try:
            hook.run()
        finally:
            sys.stdin = old
        g2 = Graph.load(self.root)
        self.assertTrue(any(n["name"] == "Web search: vat rates" for n in g2.notes))
    def test_ai_annotations_make_everyday_words_findable(self):
        query = "how much does the customer pay with vat"
        self.assertNotIn("shop/pricing.py::total_price", [h["id"] for h in self.g.search(query, k=1)])
        items, _ = self.g.pending(k=10)
        self.assertIn("shop/pricing.py", [i["target"] for i in items])
        done, missing = self.g.annotate([{"target": "shop/pricing.py::total_price",
                                          "summary": "Works out what the customer pays, VAT included.",
                                          "concepts": ["customer pay", "vat", "bill amount"],
                                          "links": [{"to": "Cart.checkout", "why": "checkout bills with it"}]}])
        self.assertEqual((done, missing), (["shop/pricing.py::total_price"], []))
        g2 = Graph.load(self.root)
        self.assertEqual(g2.search(query, k=1)[0]["id"], "shop/pricing.py::total_price")
        self.assertFalse(g2.stale("shop/pricing.py::total_price"))
        with open(os.path.join(self.root, "shop/pricing.py"), "a") as f:
            f.write("# changed\n")
        g2.refresh()
        self.assertTrue(g2.stale("shop/pricing.py"))  # code changed: annotation is due again

    def test_associate_ideas_creates_concepts(self):
        self.assertTrue(self.g.associate("bunt", "short-range knockback", "a bunt barely moves the ball"))
        self.assertTrue(self.g.associate("bunt", "total_price", "silly example link to code"))
        g2 = Graph.load(self.root)
        self.assertIn("concept:bunt", g2.chunks)
        self.assertIn("concept:short-range knockback", g2.edges["concept:bunt"])
        self.assertIn("shop/pricing.py::total_price", g2.edges["concept:bunt"])
        self.assertEqual(g2.search("knockback", k=1)[0]["id"], "concept:short-range knockback")

    def test_server_sees_what_the_hooks_wrote(self):
        s = Server(self.root)
        s.call("graph_stats", {})                     # server has loaded the graph
        Graph.load(self.root).remember("Hook note", "zebra crossings")   # another process
        out = s.call("search_code", {"query": "zebra"})
        self.assertIn("Hook note", out)
        s.call("remember", {"title": "Server note", "content": "giraffe"})
        titles = [n["name"] for n in Graph.load(self.root).notes]
        self.assertEqual(titles, ["Hook note", "Server note"])   # nothing overwritten

    def test_associate_in_batches(self):
        out = Server(self.root).call("associate", {"links": [
            {"a": "oobleck", "b": "deflect", "why": "hard impacts go solid"},
            {"a": "deflect", "b": "Cart.checkout", "why": "silly"},
            {"a": "same", "b": "same", "why": "rejected"}]})
        self.assertIn("Recorded 2 of 3", out)
        self.assertIn("concept:deflect", Graph.load(self.root).edges["concept:oobleck"])


if __name__ == "__main__":
    unittest.main()
