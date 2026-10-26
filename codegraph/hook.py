"""Claude Code hook: everything the AI does flows back into the graph.

Wired as a PostToolUse hook (see `python3 -m codegraph install`):
  WebSearch / WebFetch      the results become research notes
  Edit / Write / MultiEdit  the file is re-chunked, and files edited in the
                            same session are associated with each other
Reads the hook event as JSON on stdin; never blocks the AI (always exits 0).
"""
import json
import os
import sys

from .graph import Graph

MAX_NOTE = 6000


def _text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("result", "content", "text", "output"):
            if key in value:
                return _text(value[key])
        return json.dumps(value)[:MAX_NOTE]
    if isinstance(value, list):
        return "\n".join(_text(v) for v in value)
    return str(value)


def run(root=None):
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    root = root or event.get("cwd") or os.getcwd()
    tool = event.get("tool_name", "")
    data = event.get("tool_input") or {}
    response = event.get("tool_response")
    g = Graph.load(root)
    if tool == "WebFetch":
        url = data.get("url", "web")
        g.remember(f"Web page: {url}", f"Asked: {data.get('prompt', '')}\n{_text(response)[:MAX_NOTE]}", url)
    elif tool == "WebSearch":
        q = data.get("query", "")
        g.remember(f"Web search: {q}", _text(response)[:MAX_NOTE], "web-search")
    elif tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = data.get("file_path") or data.get("notebook_path") or ""
        rel = os.path.relpath(path, root).replace(os.sep, "/") if path else ""
        g.refresh()
        if rel and not rel.startswith(".."):
            _co_edit(g, event.get("session_id", "session"), rel)


def _co_edit(g, session, rel):
    """Files the AI changes together in one session are probably connected."""
    path = os.path.join(g.dir, "session_edits.json")
    try:
        with open(path) as f:
            sessions = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        sessions = {}
    edited = sessions.setdefault(session, [])
    for other in edited[-8:]:
        if other != rel:
            g.associate(rel, other, "edited together in one session")
    if rel not in edited:
        edited.append(rel)
    sessions = dict(list(sessions.items())[-50:])
    with open(path, "w") as f:
        json.dump(sessions, f)
