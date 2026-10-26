# codegraph — meaningful chunks + a self-updating association graph, served to the AI over MCP

1. **Chunk** the repository into meaningful pieces: functions, methods,
   classes, module code, Markdown sections, and paragraphs for everything
   else.
2. **Associate** every chunk with others. The kinds of association are:
   - `calls`: uses a name another chunk defines
   - `imports`
   - `contains`
   - `sequence`
   - `similar`: shares rare words
   - `cochange`: changed in the same git commits
   - `note`: research linked to code
   - `learned`: links the AI added itself

   This makes a big `associations.jsonl`.
3. **Serve** it over MCP. The AI searches it first, follows associations,
   and gets the chunks as context.
4. **Self-update.** Every web search, web page fetched and file edited is
   written back into the graph by Claude Code hooks. Changed files are
   re-chunked before each search. Anything the AI learns can be saved with
   `remember` and `associate`.

Pure Python 3, no dependencies.

## Use it on a repository

```bash
git clone <this repo> ~/codegraph
cd /path/to/your/repo
PYTHONPATH=~/codegraph python3 -m codegraph build .     # chunks + associations -> .codegraph/
PYTHONPATH=~/codegraph python3 -m codegraph install .   # writes .mcp.json and the hooks in .claude/settings.json
```

Then paste the snippet `install` prints into the repo's `CLAUDE.md`, so
Claude calls `search_code` before every task and saves what it learns.
Start Claude Code in the repo and approve the `codegraph` MCP server.

Other commands: `search "question" [ROOT]`, `stats [ROOT]`, `serve [ROOT]`
(the MCP server on stdio), and `hook` (the PostToolUse hook; it reads the
event from stdin).

## MCP tools

| tool | what it does |
|---|---|
| `search_code` | BM25 over chunks, then scores flow 2 hops along associations; each hit says *why* it was associated |
| `read_chunk` | full chunk text and its strongest associations |
| `related` | a chunk's neighbours with association kinds |
| `remember` | save research, findings or decisions as a note linked to code |
| `associate` | add a link the graph missed; these weigh the most |
| `graph_stats` | counts |

## What lives in `.codegraph/`

| file | contents |
|---|---|
| `chunks.jsonl` | every chunk: id (`path::Qualified.name`), lines, text, names defined and used |
| `associations.jsonl` | every association: both ends, weight, kinds and why |
| `notes.jsonl` | research and memory: web pages, web searches, `remember` notes |
| `learned.jsonl` | associations the AI added, including files edited together in one session |

Notes and learned links survive rebuilds. Everything else is rebuilt from
the code.

## Measured

`python3 -m codegraph.bench` asks 24 questions about Python's `email` and
`asyncio` packages, each with a known answer file (`asyncio` was never used
for tuning). It counts how often the right file is among the top results:

```
                 email (12)          asyncio (12)
                 k=1  k=3  k=5       k=1  k=3  k=5
keywords          6   10   12        10   10   11
chunks            8   11   11        10   12   12
chunks+assoc      9   11   11        10   12   12
```

Meaningful chunks are most of the gain. Associations add little to a single
search. Where they help is in what the AI does next: following
`calls`/`imports`/`note` links with `related`, and finding past research
again.

End to end, Claude Code was run on the `email` package with only these
tools and no file reads. It found `Generator._handle_multipart`,
`_make_boundary` and `Message.get_boundary`/`set_boundary` in two searches,
explained correctly how boundaries are picked and checked, and saved a note
of what it found.

`python3 -m unittest discover tests` runs the tests.

## `stringspace/`

An earlier experiment: word tokens at fixed random locations, random-walk
"strings" and mined "laws". On the same benchmark it only matched keyword
search, so codegraph replaces it.
