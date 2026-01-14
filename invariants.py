#!/usr/bin/env python3
import networkx as nx
from itertools import combinations

def triangle_count(G):
    tri = sum(nx.triangles(G).values()) // 3
    return tri

def four_cycle_count(G):
    nodes = list(G.nodes())
    c = 0
    for quad in combinations(nodes, 4):
        sub = G.subgraph(quad)
        if sub.number_of_edges() == 4 and all(d == 2 for _, d in sub.degree()):
            c += 1
    return c

def compute_invariants_for_graph(G):
    degs = sorted([d for _, d in G.degree()], reverse=True)
    tri = triangle_count(G)
    four = four_cycle_count(G)
    return {
        "n": G.number_of_nodes(),
        "m": G.number_of_edges(),
        "deg_seq": degs,
        "triangles": tri,
        "4cycles": four
    }
