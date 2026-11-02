# score04 – Scoring order permutation

## Purpose

This example demonstrates that the order of volume names in the scoring list
has no semantic meaning.

It shows that scoring is defined purely by the set of selected volumes,
independently of their ordering.

## What this example demonstrates

- Order invariance in scoring configuration  
- Selective scoring based on explicit volume selection  
- Decoupling between geometry definition and scoring configuration  

## What this example does NOT demonstrate

- Geometry construction techniques  
- Source configuration  
- Conditional, dynamic, or event-dependent scoring  

No assumptions are made about the particle source.  
The source configuration is intentionally left empty.

## Conceptual focus

The scoring list is **unordered**.

Changing the order of volume names does not affect which regions are scored
or how energy deposition is recorded.

## Why this example exists

Without explicit counterexamples, an LLM may incorrectly infer that the order
of volumes in the scoring list reflects geometry structure or placement order.

This example explicitly removes that ambiguity.