# score02 – Scoring all volumes

## Purpose

This example demonstrates how to enable scoring on all volumes
present in the geometry.

It shows that global scoring is achieved by explicitly listing
every volume, not through implicit or default behavior.

## What this example demonstrates

- Scoring enabled on multiple volumes simultaneously
- Explicit enumeration of all volumes in the geometry
- One-to-one correspondence between volume names and scoring regions

## What this example does NOT demonstrate

- Geometry construction techniques
- Selective or conditional scoring
- Source configuration
- Physics processes

No assumptions are made about the particle source.
The source configuration is intentionally left empty.

## Conceptual focus

There is no implicit “score everything” mode.

Even when all volumes are meant to be sensitive,
they must be explicitly listed in the scoring configuration.

## Why this example exists

This example prevents a common misconception:
that all volumes are automatically scored by default.

It reinforces the rule that scoring is always an explicit decision,
even when applied globally.
