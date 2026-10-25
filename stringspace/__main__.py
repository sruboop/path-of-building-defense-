"""python3 -m stringspace build [ROOT] | ask "request" [ROOT] | stats [ROOT]"""
import argparse
import sys

from .context import ask
from .state import State


def main(argv=None):
    ap = argparse.ArgumentParser(prog="stringspace")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="place tokens, associate, seed strings, mine laws")
    b.add_argument("root", nargs="?", default=".")
    a = sub.add_parser("ask", help="hop from a request and print context")
    a.add_argument("request")
    a.add_argument("root", nargs="?", default=".")
    a.add_argument("-k", type=int, default=6, help="number of snippets")
    a.add_argument("--strings", action="store_true", help="also show the strings used")
    s = sub.add_parser("stats", help="size of the space")
    s.add_argument("root", nargs="?", default=".")
    args = ap.parse_args(argv)

    if args.cmd == "build":
        state = State.build(args.root)
        state.save(args.root)
        print(f"{len(state.space.files)} files, {len(state.space.neighbours)} black holes, "
              f"{len(state.strings)} strings, {len(state.laws)} laws")
        return
    try:
        state = State.load(args.root)
    except FileNotFoundError:
        sys.exit("no space yet: run `python3 -m stringspace build` first")
    if args.cmd == "stats":
        sp = state.space
        dense = sorted(sp.neighbours, key=state.strings.density, reverse=True)[:10]
        print(f"{len(sp.files)} files, {len(sp.neighbours)} black holes, "
              f"{len(state.strings)} strings, {len(state.laws)} laws")
        print("densest black holes:", ", ".join(f"{t}({state.strings.density(t)})" for t in dense))
        for law, n in sorted(state.laws.support.items(), key=lambda kv: -kv[1])[:10]:
            print(f"  law [{n}]  " + " ~> ".join(law))
        return
    result = ask(state, args.request, k=args.k)
    state.save(args.root)
    print("seeds:", ", ".join(result["seeds"]) or "(none of these words exist here)")
    if args.strings:
        for score, s, laws in result["strings"][:10]:
            mark = f"  laws:{len(laws)}" if laws else ""
            print(f"  [{score:6.2f} x{s.count}] {s}{mark}")
    for snip in result["snippets"]:
        print(f"\n--- {snip['file']}:{snip['start']}-{snip['end']}")
        for i, line in enumerate(snip["text"], snip["start"]):
            print(f"{i:5d}  {line}")


if __name__ == "__main__":
    main()
