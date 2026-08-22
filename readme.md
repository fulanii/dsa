# Data Structures & Algorithms — Notes & Solutions

My working notebook for data structures and algorithms, written from the perspective of a backend developer who ships Python **Django / FastAPI** applications.

This is not a wall of pasted LeetCode solutions. Every data structure and pattern here is written in my own words, with the parts that actually matter: how it works, what it costs, which problems it unlocks, and where it shows up in real backend code rather than only in interviews.

## What's in here

- **Data structure notes** — one file per structure (arrays, hash maps, linked lists, stacks/queues, heaps, trees, tries, graphs, union-find).
- **Pattern notes** — the reusable techniques (two pointers, sliding window, binary search, BFS/DFS, backtracking, greedy, dynamic programming, topological sort).
- **Solutions** — problems solved in Python, each with the reasoning that led to the approach, not just the final code.
- **Complexity tables** — time and space for every operation, in one place, so I can compare structures at a glance.
- **Backend mapping** — where the idea shows up in real work (hash maps → caching and dedup, heaps → task priority queues, graphs → dependency resolution, DP → query planning).

## Note format

Each note follows the same structure, so it stays useful as a reference long after the interviews:

```
1. What it is           — plain-English definition and mental model
2. How it works         — internals, invariants, and the diagram
3. Complexity           — time/space per operation, and the worst case
4. When to use it       — the problems it actually solves
5. When NOT to use it   — simpler/cheaper alternatives, common misuse
6. Backend mapping      — where this shows up in a real Python service
7. Problems             — representative problems, with my reasoning
```

## Solution format

Every solution carries the thinking, since that's the part worth re-reading:

- The brute-force approach and why it isn't enough
- The insight that improves it
- Final implementation in Python, with complexity stated
- Edge cases and the mistakes I made the first time

## Who this is for

- **Recruiters / hiring managers** — evidence of how I reason about problems and trade-offs, not just that I can produce a passing submission.
- **Anyone studying DSA** — especially if you're self-taught and want the concepts tied to real code instead of contest trivia.
- **Me, later** — the reference I'll open before an interview, or when a hot path needs the right structure.

## Status

Work in progress — notes get added as I work through each topic.

| Topic | Status |
| --- | --- |
| [Big O](01-big-o/README.md) | 🟨 In progress |
| [Classes & Pointers](02-classes-and-pointers/README.md) | ⬜ Not started |
| [Linked Lists](03-linked-lists/README.md) | ⬜ Not started |
| [Doubly Linked Lists](04-doubly-linked-lists/README.md) | ⬜ Not started |
| [Stacks & Queues](05-stacks-and-queues/README.md) | ⬜ Not started |
| [Trees](06-trees/README.md) | ⬜ Not started |
| [Hash Tables](07-hash-tables/README.md) | ⬜ Not started |
| [Graphs](08-graphs/README.md) | ⬜ Not started |
| [Heaps](09-heaps/README.md) | ⬜ Not started |
| [Recursion](10-recursion/README.md) | ⬜ Not started |
| [Recursive Binary Search Trees](11-recursive-binary-search-trees/README.md) | ⬜ Not started |
| [Tree Traversal](12-tree-traversal/README.md) | ⬜ Not started |
| [Basic Sorts](13-basic-sorts/README.md) | ⬜ Not started |
| [Merge Sorts](14-merge-sorts/README.md) | ⬜ Not started |
| [Quick Sort](15-quick-sort/README.md) | ⬜ Not started |
| [Dynamic Programming](16-dynamic-programming/README.md) | ⬜ Not started |
| [Coding Exercises](17-coding-exercises/README.md) | ⬜ Not started |

## Goal

By the end of this: fluency with the core structures and patterns, a set of solved problems I can explain out loud, and a personal reference I'll actually use — which is worth considerably more than a streak count.