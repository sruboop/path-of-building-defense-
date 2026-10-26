"""codegraph command line.

  python3 -m codegraph build   [ROOT]          chunk + associate the repository
  python3 -m codegraph search  "question" [ROOT]
  python3 -m codegraph stats   [ROOT]
  python3 -m codegraph serve   [ROOT]          MCP server on stdio
  python3 -m codegraph hook    [ROOT]          Claude Code PostToolUse hook (stdin)
  python3 -m codegraph install [ROOT]          register server + hooks for Claude Code in ROOT
"""
import json
import os
import sys

from .graph import Graph


def install(root):
    """Writes ROOT/.mcp.json and ROOT/.claude/settings.json so Claude Code uses codegraph."""
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.abspath(root)
    # PYTHONSAFEPATH: never import from the repo itself (a repo with its own
    # subprocess.py or json.py would otherwise shadow the standard library)
    env = {"PYTHONPATH": here, "PYTHONSAFEPATH": "1"}
    mcp_path = os.path.join(root, ".mcp.json")
    mcp = _load(mcp_path)
    mcp.setdefault("mcpServers", {})["codegraph"] = {
        "command": "python3", "args": ["-m", "codegraph", "serve", root], "env": env}
    _dump(mcp_path, mcp)

    settings_path = os.path.join(root, ".claude", "settings.json")
    settings = _load(settings_path)
    command = f"PYTHONSAFEPATH=1 PYTHONPATH={json.dumps(here)} python3 -m codegraph hook {json.dumps(root)}"
    hooks = settings.setdefault("hooks", {}).setdefault("PostToolUse", [])
    hooks[:] = [h for h in hooks if "codegraph hook" not in json.dumps(h)]
    hooks.append({"matcher": "WebSearch|WebFetch|Edit|Write|MultiEdit|NotebookEdit",
                  "hooks": [{"type": "command", "command": command, "timeout": 60}]})
    _dump(settings_path, settings)
    print(f"wrote {mcp_path}\nwrote {settings_path}")
    print("Add this to the repository's CLAUDE.md so the AI uses it every time:\n")
    print(CLAUDE_MD)


CLAUDE_MD = """## Code context
Once per repository (and again when `graph_stats` shows unannotated files):
call `pending_annotations`, read the overviews and `annotate` each file with
a plain-language summary and the everyday words someone would use to ask
about it; repeat until none are pending.

Before answering a question or changing code, call the `codegraph` MCP tool
`search_code` with the task in plain words, then `read_chunk` / `related` on
the most relevant ids to follow associations. Search again with different
words when results look thin. After researching anything (web or code),
save what you learned with `remember`, linked to the chunks it concerns, and
record non-obvious connections with `associate`."""


def _load(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _dump(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "search":
        query, root = rest[0], (rest[1] if len(rest) > 1 else ".")
        from .server import Server
        print(Server(root).call("search_code", {"query": query}))
        return
    root = rest[0] if rest else "."
    if cmd == "build":
        g = Graph(root).build()
        print(f"{len(g.files)} files, {len(g.chunks)} chunks, "
              f"{sum(len(v) for v in g.edges.values()) // 2} associations -> {g.dir}")
    elif cmd == "stats":
        from .server import Server
        print(Server(root).call("graph_stats", {}))
    elif cmd == "serve":
        from .server import serve
        serve(root)
    elif cmd == "hook":
        from .hook import run
        try:
            run(root if rest else None)
        except Exception as e:  # a hook must never break the AI's work
            print(f"codegraph hook: {e}", file=sys.stderr)
    elif cmd == "install":
        install(root)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
