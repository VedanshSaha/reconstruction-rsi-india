# Graph Reconstruction Conjecture – Computational Pipeline

This repository implements a computational pipeline to test the **Graph Reconstruction Conjecture** on restricted families of graphs.

A graph \(G\) has a **deck** consisting of the multiset of graphs \(G - v\) obtained by deleting each vertex \(v\).  
Two graphs are reconstruction-equivalent if their decks are isomorphic as multisets.

The goal here is to generate graphs in controlled families, build their decks, compute invariant signatures of those decks, and detect graphs whose decks cannot be distinguished by those invariants.

---

## Graph families

Graphs are generated with constraints to keep the search feasible.  
The main families used here are:

- Graphs with at most 10 vertices  
- Maximum degree at most 3  

Graphs are generated with `geng` from the Nauty suite and stored in graph6 format, which represents one isomorphism class per line.

---

## Deck construction

For each graph \(G\):

1. Each vertex \(v\) is deleted to form the card \(G - v\)
2. Each card is converted to a canonical form using Nauty so relabelings do not produce duplicates
3. The full deck is stored as a multiset of canonical cards

This step removes ordering effects and isolates genuine structural differences.

---

## Card invariants

For each card \(G - v\), the following invariants are computed:

- number of vertices
- number of edges
- degree sequence
- number of triangles
- number of 4-cycles
- connectivity
- Weisfeiler–Lehman hash

These are used as isomorphism-invariant fingerprints of each card.

---

## Deck signatures

For each graph, the multiset of card hashes is sorted and stored as a **deck signature**.

Graphs with the same deck signature are grouped together.  
These groups are candidates for reconstruction collisions.

---

## Collision filtering

Some collisions come from graphs that are actually isomorphic.  
These are filtered using Nauty canonical labeling.

Remaining groups are pairs or sets of non-isomorphic graphs whose decks agree under all computed invariants.

---

## Visual inspection

For candidate collisions, additional data is plotted:

- triangle counts per card
- 4-cycle counts per card

These are used to compare how much structural information the deck preserves and where ambiguity remains.

---

## What the code produces

The pipeline outputs:

- canonical graph datasets
- full decks for every graph
- invariant vectors for each card
- deck signatures
- groups of graphs with matching deck signatures
- plots comparing card invariants

This provides a concrete way to test reconstruction on small graph families and to identify families that are hard to distinguish from their decks.

---

## References

- J. A. Bondy and R. L. Hemminger, *Graph Reconstruction—A Survey*  
- B. D. McKay and A. Piperno, *Practical Graph Isomorphism, II* (Nauty/Traces)  
