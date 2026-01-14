# Computational Experiments on the Graph Reconstruction Conjecture

This repository contains a fully automated computational pipeline designed to experimentally probe the **Graph Reconstruction Conjecture**, one of the central open problems in graph theory.

The conjecture (formulated by Kelly and Ulam in the 1940s) states:

> Every finite simple graph with at least three vertices is uniquely determined, up to isomorphism, by the multiset of its vertex-deleted subgraphs (its *deck*).

Equivalently, no two non-isomorphic graphs on ≥3 vertices should have the same deck.

This project uses large-scale enumeration, canonicalization, invariant extraction, and collision detection to search for potential counterexamples or hard families of graphs.

---

## What this project does:

The entire pipeline is fully automated and runs in the cloud using GitHub Actions. It consists of four major stages:

