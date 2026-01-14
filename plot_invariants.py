#!/usr/bin/env python3
# plot_invariants.py
# Usage: python plot_invariants.py CANDIDATES_JSON
import sys, json, matplotlib.pyplot as plt
from pprint import pprint

CAND = sys.argv[1] if len(sys.argv) > 1 else "candidate_pairs.json"
with open(CAND) as f:
    cand = json.load(f)

# Simple textual summary + tiny plots for first few candidates
for i, entry in enumerate(cand[:5]):
    print("Candidate", i, "graphs:", entry['graphs'])
    for gfile in entry['graphs']:
        with open(gfile) as gf:
            d = json.load(gf)
            invs = [c['invariants'] for c in d['cards']]
            # collect e.g. triangle counts
            tr = [x['triangles'] for x in invs]
            fc = [x['4cycles'] for x in invs]
            ds = [x['deg_seq'] for x in invs]
            plt.figure(figsize=(6,2))
            plt.subplot(1,2,1)
            plt.plot(tr, marker='o')
            plt.title('triangles per card')
            plt.subplot(1,2,2)
            plt.plot(fc, marker='o')
            plt.title('4-cycles per card')
            plt.suptitle(gfile)
            plt.tight_layout()
            plt.show()
