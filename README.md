# Computational Experiments on the Graph Reconstruction Conjecture

## The conjecture

The Graph Reconstruction Conjecture states that every finite simple graph with at least three vertices is uniquely determined, up to isomorphism, by the multiset of its vertex-deleted subgraphs.  
These vertex-deleted subgraphs are called the *deck* of the graph.

Equivalently, the conjecture says that no two non-isomorphic graphs on at least three vertices have exactly the same deck.

Despite being open for more than seventy years, the conjecture has been verified for many special classes of graphs and for all graphs up to small numbers of vertices, but no general proof or counterexample is known.

---

## Purpose of this repository

This repository implements a computational pipeline to search for graphs whose decks are indistinguishable under strong invariants. The goal is to identify either genuine counterexamples or graphs that are close to being counterexamples and therefore structurally difficult to reconstruct.

The pipeline is designed to:
- enumerate large families of graphs under constraints,
- construct the full vertex-deleted deck of each graph,
- compute invariants of every card in each deck,
- assign a canonical signature to each deck,
- group graphs with matching deck signatures,
- and analyze these groups using further invariants and visualizations.

All steps can be run locally for small cases or on GitHub Actions for larger datasets.

---

## Graph generation

Graphs are generated subject to constraints such as bounded maximum degree. To avoid duplicate labelings, graphs are stored in **graph6** format, which provides a canonical encoding of a graph up to isomorphism.

The generated graphs are stored in the `graphs/` directory. Each `.g6` file contains one graph per line, and each line represents one isomorphism class.

---

## Deck construction

For each graph \(G\), the deck is the multiset of graphs \(G - v\) obtained by deleting each vertex \(v\) in turn.

For every card \(G - v\), the pipeline computes the following invariants:
- number of vertices and edges,
- degree sequence,
- number of triangles,
- number of 4-cycles,
- connectivity information,
- a Weisfeiler–Lehman (WL) graph hash.

These invariants are isomorphism-invariant and give a compact summary of each card’s structure.

Each original graph is stored as a JSON file in the `decks/` directory. The file contains:
- the original graph (in graph6 form),
- all vertex-deleted cards,
- the invariants of each card,
- and a sorted list of card hashes called the *deck signature*.

The deck signature acts as a fingerprint of the entire deck.

---

## Collision detection

All deck signatures are grouped. If two or more graphs share the same deck signature, they are recorded as **candidate reconstruction collisions**.

These are written to the file:


Each entry lists a deck signature and the set of graphs whose decks produce that signature. These groups may contain isomorphic graphs (false positives) or genuinely difficult cases for reconstruction.

---

## Invariant plots

For each candidate collision, the pipeline produces plots showing how certain invariants vary across the cards of each deck. In particular, it plots:
- triangle counts per card,
- 4-cycle counts per card.

These plots are saved as PNG files in the `plots/` directory. They are used to visually compare decks that appear identical under hashing.

---

## Repository structure

graphs/ graph6 datasets
decks/ deck JSON files with invariants
candidate_pairs.json deck collision groups
plots/ invariant plots

generate_graphs_fallback.py
build_decks.py
compare_decks.py
plot_invariants_github.py
invariants.py


---

## What this provides

This repository implements a complete computational framework for exploring the Graph Reconstruction Conjecture on large families of graphs. It produces:
- explicit decks for every graph in the dataset,
- invariant-based deck signatures,
- groups of graphs with matching decks,
- and visual diagnostics for those groups.

These outputs can be used to test reconstruction heuristics, study hard families of graphs, and search for potential counterexamples.
