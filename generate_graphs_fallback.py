#!/usr/bin/env python3
import os
import sys
import networkx as nx
from itertools import combinations

OUTDIR = sys.argv[1] if len(sys.argv) > 1 else "graphs_fallback"
n = int(sys.argv[2]) if len(sys.argv) > 2 else 7
max_deg = int(sys.argv[3]) if len(sys.argv) > 3 else 3

os.makedirs(OUTDIR, exist_ok=True)

def graph6_str(G):
    return nx.to_graph6_bytes(G, header=False).decode().strip()

seen = set()
count = 0

nodes = list(range(n))
pairs = list(combinations(range(n), 2))

for m in range(len(pairs) + 1):
    for E in combinations(pairs, m):
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(E)

        if any(d > max_deg for _, d in G.degree()):
            continue

        g6 = graph6_str(G)
        if g6 in seen:
            continue

        seen.add(g6)
        with open(os.path.join(OUTDIR, f"graph_{count}.g6"), "w") as f:
            f.write(g6 + "\n")

        count += 1

    if count > 20000:
        break

print("Wrote", count, "graphs to", OUTDIR)
