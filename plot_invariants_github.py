#!/usr/bin/env python3
import sys
import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CAND = sys.argv[1] if len(sys.argv) > 1 else "candidate_pairs.json"
OUTDIR = "plots"

os.makedirs(OUTDIR, exist_ok=True)

with open(CAND) as f:
    cand = json.load(f)

for i, entry in enumerate(cand[:10]):
    for j, gfile in enumerate(entry["graphs"]):
        with open(gfile) as gf:
            d = json.load(gf)

        invs = [c["invariants"] for c in d["cards"]]
        tr = [x["triangles"] for x in invs]
        fc = [x["4cycles"] for x in invs]

        plt.figure(figsize=(6, 2))
        plt.subplot(1, 2, 1)
        plt.plot(tr, marker="o")
        plt.title("triangles")

        plt.subplot(1, 2, 2)
        plt.plot(fc, marker="o")
        plt.title("4-cycles")

        name = f"cand{i}_g{j}.png"
        plt.suptitle(gfile)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTDIR, name))
        plt.close()
