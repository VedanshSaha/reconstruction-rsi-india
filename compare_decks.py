#!/usr/bin/env python3
import os
import sys
import glob
import json
from collections import defaultdict

DECKS_DIR = sys.argv[1] if len(sys.argv) > 1 else "decks"
OUT = sys.argv[2] if len(sys.argv) > 2 else "candidate_pairs.json"

sig_to_graphs = defaultdict(list)

for p in glob.glob(os.path.join(DECKS_DIR, "deck_*.json")):
    with open(p) as f:
        data = json.load(f)
        sig = tuple(data.get("deck_signature", []))
        sig_to_graphs[sig].append(p)

candidates = []

for sig, files in sig_to_graphs.items():
    if len(files) > 1:
        candidates.append({
            "deck_signature": sig,
            "graphs": files
        })

with open(OUT, "w") as f:
    json.dump(candidates, f, indent=2)

print("Found", len(candidates), "candidate collisions. Saved to", OUT)
