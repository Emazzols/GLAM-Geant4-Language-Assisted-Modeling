# score01 – Single scoring volume

## Purpose

This example introduces scoring in its simplest explicit form.

It demonstrates that energy deposition is recorded **only** in volumes
that are explicitly selected for scoring, even when multiple volumes
exist in the geometry.

## What this example demonstrates

- A geometry containing multiple independent volumes
- Explicit selection of a single scoring volume by name
- Scoring as an opt-in mechanism

## What this example does NOT demonstrate

- Geometry construction techniques
- Source configuration
- Physics processes or particle types
- Multiple or conditional scoring logic

No assumptions are made about the particle source.
The source configuration is intentionally left empty.

## Conceptual focus

Scoring is **volume-specific** and **name-based**.

Only volumes explicitly listed in the scoring configuration
produce output.

All other volumes are ignored, even if particles traverse them
or deposit energy inside them.

## Why this example exists

This example establishes the fundamental rule:

**A volume is scored only if it is explicitly listed.**

This rule underlies all more advanced scoring configurations.
