# Computational Experiments on the Graph Reconstruction Conjecture

This repository contains a full computational pipeline I built to experimentally explore one of the most famous open problems in graph theory: the **Graph Reconstruction Conjecture**.

The conjecture, proposed by Kelly and Ulam in the 1940s, states that every finite simple graph with at least three vertices is uniquely determined (up to isomorphism) by the multiset of its vertex-deleted subgraphs, called its *deck*. In other words, if you are given all graphs obtained by deleting one vertex from an unknown graph, you should in principle be able to reconstruct the original graph.

Despite decades of work, no counterexample is known and no general proof exists. This project uses computation to probe where reconstruction is hardest and to search for potential counterexamples.

---

## What this project does

At a high level, the goal is to search for pairs of non-isomorphic graphs whose decks look identical. To do this, I built a pipeline that:

1. Generates large families of graphs  
2. Builds their vertex-deleted decks  
3. Canonicalizes and hashes every card  
4. Groups graphs by deck signature  
5. Searches for collisions  
6. Analyzes hard cases using stronger invariants and plots  

All of this runs automatically on GitHub’s cloud infrastructure.

---

## Graph generation

Graphs are generated with constraints (such as bounded maximum degree) and stored in **graph6** format, which gives a canonical representation up to isomorphism. This ensures that each graph appears only once.

The output lives in the `graphs/` folder. Each line of a `.g6` file represents one isomorphism class of graphs.

---

## Deck construction

For each graph \(G\), the deck is the multiset of graphs \(G - v\) obtained by deleting each vertex \(v\).

For every card \(G - v\), the code computes:
- degree sequence  
- number of edges  
- number of triangles  
- number of 4-cycles  
- connectivity information  
- a Weisfeiler–Lehman (WL) hash  

These invariants are chosen because they are fast, isomorphism-invariant, and strong enough to distinguish many graphs.

Each graph is stored as a JSON file in `decks/`, containing all of its cards, their invariants, and a sorted **deck signature** that acts as a fingerprint for the entire deck.

---

## Collision detection

Graphs are grouped by their deck signatures. If two or more graphs share the same deck signature, they are flagged as **candidate reconstruction collisions**.

These are stored in:

