#!/usr/bin/env python3
import os
import sys
import json
import glob
import networkx as nx
from networkx.readwrite.graph6 import from_graph6_bytes
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash
from invariants import compute_invariants_for_graph

GRAPHS_DIR = sys.argv[1] if len(sys.argv) > 1 else "graphs"
OUT = sys.argv[2] if len(sys.argv) > 2 else "decks"

os.makedirs(OUT, exist_ok=True)

def load_graphs_from_dir(d):
    for p in glob.glob(os.path.join(d, "*.g6")):
        with open(p) as f:
            for i, line in enumerate(f):
                s = line.strip()
                if s:
                    yield p, i, s

def canonical_card_key(G):
    h = weisfeiler_lehman_graph_hash(G, iterations=3)
    degs = sorted(d for _, d in G.degree())
    return f"{h}|{','.join(map(str, degs))}"

for p, idx, g6 in load_graphs_from_dir(GRAPHS_DIR):
    G = from_graph6_bytes(g6.encode())

    cards = []
    deck_sig = []

    for v in list(G.nodes()):
        H = G.copy()
        H.remove_node(v)

        key = canonical_card_key(H)
        inv = compute_invariants_for_graph(H)

        cards.append({
            "removed": v,
            "card_hash": key,
            "invariants": inv
        })

        deck_sig.append(key)

    data = {
        "source_file": p,
        "index": idx,
        "g6": g6,
        "deck_signature": sorted(deck_sig),
        "cards": cards
    }

    outname = os.path.join(OUT, f"deck_{os.path.basename(p)}_{idx}.json")

    with open(outname, "w") as f:
        json.dump(data, f, indent=2)

    print("Wrote", outname)
