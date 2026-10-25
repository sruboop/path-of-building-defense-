"""Split a JSON observation into the smallest possible chunks.

No domain knowledge: a chunk is a leaf `path=value`. The only "math" the
agent is allowed is generic arithmetic on numbers: differences between
numeric leaves that share a name (relations) and changes over time (deltas).
"""
import json


def flatten(obj, prefix=""):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.update(flatten(v, f"{prefix}.{k}" if prefix else k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.update(flatten(v, f"{prefix}[{i}]"))
    else:
        out[prefix] = obj
    return out


def _split(path):
    head, _, last = path.rpartition(".")
    return head, last


def perceive(observation_json):
    """Returns (chunk tokens, numeric readings) for one moment."""
    leaves = flatten(json.loads(observation_json))
    numeric = {p: v for p, v in leaves.items()
               if isinstance(v, (int, float)) and not isinstance(v, bool)}
    groups = {}
    for p in sorted(numeric):
        head, last = _split(p)
        groups.setdefault(last, []).append((head, p))
    for last, members in groups.items():
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                (ha, pa), (hb, pb) = members[i], members[j]
                numeric[f"{last}({ha}-{hb})"] = numeric[pa] - numeric[pb]
    tokens = {f"{k}={v}" for k, v in leaves.items()}
    tokens |= {f"{k}={v}" for k, v in numeric.items() if k not in leaves}
    return tokens, numeric


def deltas(before, after):
    return {f"Δ{k}={after[k] - before[k]:+d}"
            for k in before if k in after and after[k] != before[k]}


def parse(token):
    key, _, val = token.rpartition("=")
    try:
        return key, int(val)
    except ValueError:
        return key, val
