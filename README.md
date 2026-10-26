> **Making ARPG skills?** Follow [`arpg/method/PLAYBOOK.md`](arpg/method/PLAYBOOK.md): research → associations → design in fresh sessions, with random inspiration pairs. It beat both a single session and the codegraph pipeline in blind tests.

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
4. **Meaning from the AI.** Claude reads the chunks and writes what each file
   means in plain words (`annotate`), so questions in everyday words find
   code named in programmer's words.
5. **Self-update.** Every web search, web page fetched and file edited is
   written back into the graph by Claude Code hooks. Changed files are
   re-chunked before each search. Anything the AI learns can be saved with
   `remember` and `associate`.

Pure Python 3.11+, no dependencies, no outside models: the meaning comes
from the AI you are already talking to.

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

### Meaning comes from the AI in the chat, not from an outside model

After `build`, ask Claude in the repo to "annotate the codegraph". It calls
`pending_annotations`, reads the overview of each file, and `annotate`s
every file with:
- a plain-language summary;
- the everyday words a person would use when asking about that file
  ("placeholder for a later value" → `futures.py`);
- any links it notices.

Those words are searched along with the code. When code changes, its
annotation is marked stale and comes back in `pending_annotations`. On
`asyncio` (34 files) this took Claude 13 turns and cost about $0.30.

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
| `pending_annotations` | files/chunks not yet described by the AI, or changed since |
| `annotate` | the AI writes a summary + concept words (+ links) for files or chunks |
| `graph_stats` | counts, including how many files are annotated |

## What lives in `.codegraph/`

| file | contents |
|---|---|
| `chunks.jsonl` | every chunk: id (`path::Qualified.name`), lines, text, names defined and used |
| `associations.jsonl` | every association: both ends, weight, kinds and why |
| `notes.jsonl` | research and memory: web pages, web searches, `remember` notes |
| `learned.jsonl` | associations the AI added, including files edited together in one session |
| `annotations.jsonl` | the AI's summary and concept words per file/chunk, with the code hash they describe |

Notes, learned links and annotations survive rebuilds. Everything else is rebuilt from
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

**Questions worded unlike the code** (8 per package, e.g. "placeholder for a
value that will be available later" for `Future`). Plain search does badly on
these. After Claude annotated `asyncio` once, with a generic instruction and
without seeing the questions, the same single search did much better:

```
asyncio, single search, right file in top k     k=1   k=3   k=5
questions (12)    before annotation              10    12    12
                  after Claude annotated         12    12    12
paraphrased (8)   before annotation               2     4     5
                  after Claude annotated          6     7     8
```

During a task Claude also rewords its own searches. The 4 paraphrased
questions plain search missed were given to Claude Code with only these
tools: it got all 4 right in one search each ("SSL TLS handshake",
"Future", "TaskGroup", "timeout"), for about $0.06 per question.

End to end, Claude Code was also run on the `email` package with only these
tools and no file reads. It found `Generator._handle_multipart`,
`_make_boundary` and `Message.get_boundary`/`set_boundary` in two searches,
explained correctly how boundaries are picked and checked, and saved a note
of what it found.

`python3 -m unittest discover tests` runs the tests.

## `stringspace/`

An earlier experiment: word tokens at fixed random locations, random-walk
"strings" and mined "laws". On the same benchmark it only matched keyword
search, so codegraph replaces it.
