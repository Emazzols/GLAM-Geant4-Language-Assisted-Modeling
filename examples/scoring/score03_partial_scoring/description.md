# score03 – Partial scoring

## Purpose

This example demonstrates selective scoring in a geometry
containing multiple volumes.

It shows how to record energy deposition only in a chosen
subset of existing volumes.

## What this example demonstrates

- Partial scoring based on explicit volume selection
- Decoupling between geometry definition and scoring configuration
- Fine-grained control over which regions are sensitive

## What this example does NOT demonstrate

- Geometry construction techniques
- Source configuration
- Conditional, dynamic, or event-dependent scoring

No assumptions are made about the particle source.
The source configuration is intentionally left empty.

## Conceptual focus

Scoring is selective by design.

Volumes not listed in the scoring configuration are completely ignored,
even if particles pass through them and deposit energy.

## Why this example exists

Realistic detector geometries often contain both active and passive regions.

This example reinforces that scoring is not determined by geometry alone,
but exclusively by explicit user intent.
