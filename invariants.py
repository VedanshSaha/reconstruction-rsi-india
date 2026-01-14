#!/usr/bin/env python3
# invariants.py
# small helpers: degree sequence, triangle count, 4-cycle count, card size

import networkx as nx
from itertools import combinations

def triangle_count(G):
    # networkx.triangles returns dict: total triangles incident to node
    tri = sum(nx.triangles(G).values()) // 3
    return tri

def four_cycle_count(G):
    # brute force: check all 4-node subsets for induced 4-cycle (simple check)
    nodes = list(G.nodes())
    c = 0
    for quad in combinations(nodes, 4):
        sub = G.subgraph(quad)
        # a 4-cycle has 4 nodes, 4 edges, and every node degree 2 in the induced subgraph
        if sub.number_of_edges() == 4 and all(d==2 for _,d in sub.degree()):
            c += 1
    # each 4-cycle is counted twice (two directions) depending on detection, but this counts distinct
    return c

def compute_invariants_for_graph(G):
    degs = sorted([d for _,d in G.degree()], reverse=True)
    tri = triangle_count(G)
    four = four_cycle_count(G)
    return {"n": G.number_of_nodes(), "m": G.number_of_edges(), "deg_seq": degs, "triangles": tri, "4cycles": four}
