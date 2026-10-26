#!/usr/bin/env bash
# Runs the research -> associations -> design -> revise pipeline in WORKDIR.
# WORKDIR must contain BRIEF.md and INSPIRATION.md (see PLAYBOOK.md).
#   bash run.sh WORKDIR [--no-revise]
set -euo pipefail
W="$(cd "$1" && pwd)"; HERE="$(cd "$(dirname "$0")" && pwd)"; P="$HERE/prompts"
[ -f "$W/BRIEF.md" ] && [ -f "$W/INSPIRATION.md" ] || { echo "WORKDIR needs BRIEF.md and INSPIRATION.md"; exit 1; }
cd "$W"
step() {  # name, prompt file, allowed tools, max turns
  echo "== $1"
  claude -p "$(cat "$P/$2")" --allowedTools "$3" --max-turns "$4" --output-format json > "$W/log_$1.json"
  python3 -c "import json,sys; m=json.load(open(sys.argv[1])); print(m.get('subtype'), m.get('num_turns'), 'turns, \$%.2f' % m.get('total_cost_usd', 0))" "$W/log_$1.json"
}
step research     1_research.md     "Read,Write,Edit,WebSearch,WebFetch" 120
step associations 2_associations.md "Read,Write,Edit"                    60
cp SKILLS.md SKILLS_previous.md 2>/dev/null || true
step design       3_design.md       "Read,Write,Edit"                    60
cp SKILLS.md SKILLS_draft.md
if [ "${2:-}" != "--no-revise" ]; then step revise 4_revise.md "Read,Write,Edit" 40; fi
echo "done: $W/SKILLS.md (draft kept as SKILLS_draft.md)"
