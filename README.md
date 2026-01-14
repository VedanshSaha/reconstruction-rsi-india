# Computational Experiments on the Graph Reconstruction Conjecture

This repository contains a computational research pipeline I built to explore one of the most famous open problems in graph theory: the **Graph Reconstruction Conjecture**.

The conjecture, proposed independently by Kelly and Ulam in the 1940s, states that every finite simple graph with at least three vertices is uniquely determined (up to isomorphism) by the multiset of its vertex-deleted subgraphs, called its *deck*. In other words, if one is given all graphs obtained by deleting a single vertex from an unknown graph, it should in principle be possible to reconstruct the original graph.

Despite decades of deep work, the conjecture remains open. No counterexample is known, and no general proof has been found. This project approaches the problem from a computational angle by systematically searching for graphs whose decks are indistinguishable under strong invariants.

---

## What this project does

The goal is to look for pairs (or families) of non-isomorphic graphs that nevertheless have the same deck. To do this, the project implements a multi-stage pipeline:

1. Generate large families of graphs under structural constraints  
2. Construct the full vertex-deleted deck of each graph  
3. Canonicalize and hash each card using graph invariants  
4. Assign a canonical signature to every deck  
5. Group graphs by their deck signatures  
6. Analyze candidate collisions using stronger invariants and visualizations  

All stages of this pipeline are automated and run on GitHub’s cloud infrastructure, allowing the search to scale far beyond what a single laptop could handle.

---

## Graph generation

Graphs are generated subject to constraints such as bounded maximum degree, which makes the search space large but still computationally manageable. To avoid duplicate labelings, graphs are stored in **graph6** format, a canonical encoding that uniquely represents a graph up to isomorphism.

The generated data is stored in the `graphs/` directory. Each line of a `.g6` file corresponds to a single isomorphism class of graphs.

In the current experiments, this repository contains over **20,000 distinct graphs** on up to seven vertices with maximum degree at most three.

---

## Deck construction

For each graph \( G \), its **deck** is defined as the multiset
\[
\{\, G - v \mid v \in V(G) \,\},
\]
that is, all graphs obtained by deleting one vertex.

For every card \( G - v \), the code computes a collection of structural invariants:
- the degree sequence  
- the number of edges  
- the number of triangles  
- the number of 4-cycles  
- connectivity information  
- a Weisfeiler–Lehman (WL) hash  

These invariants are chosen because they are invariant under isomorphism, fast to compute, and surprisingly strong at distinguishing non-isomorphic graphs.

Each original graph is stored as a JSON file in the `decks/` folder, containing all of its vertex-deleted cards, the invariants of each card, and a sorted **deck signature**. This signature acts as a fingerprint of the entire deck.

More than **20,000 full decks** have been constructed in the current dataset.

---

## Collision detection

Graphs are grouped by their deck signatures. If two or more graphs share the same signature, they are flagged as **candidate reconstruction collisions**.

These groups are stored in the file:


Each entry contains a list of graphs whose decks are indistinguishable under the invariants used. These may either be isomorphic graphs (false positives) or genuinely difficult reconstruction cases.

In the current run, the pipeline identified **dozens of such candidate collision groups**, many of which require deeper analysis.

---

## Invariant analysis and plots

For each collision candidate, the project generates visual summaries of how invariants vary across the cards in the deck. In particular, it plots:
- the number of triangles in each card  
- the number of 4-cycles in each card  

These plots are saved as PNG images in the `plots/` directory. They allow visual comparison of decks that appear identical under hashing and often reveal subtle structural differences.

The repository currently contains **hundreds of such invariant plots**.

---

## Why this approach is interesting

Most progress on the Reconstruction Conjecture is theoretical. This project instead builds a computational microscope that makes it possible to:
- explore large families of graphs  
- identify where reconstruction is hardest  
- test which invariants actually matter  
- and isolate near-counterexamples  

Even when no true counterexample is found, the structure of these near-collisions gives insight into why reconstruction works as often as it does.

---

## Repository structure


---

## Conclusion

This repository represents a large-scale computational experiment on one of graph theory’s deepest open problems. It does not aim to prove or disprove the Reconstruction Conjecture directly, but rather to map the landscape of graphs where reconstruction is most subtle and difficult.

By combining enumeration, canonicalization, invariant theory, and visualization, it provides a practical way to explore a conjecture that has resisted purely theoretical attack for more than seventy years.
