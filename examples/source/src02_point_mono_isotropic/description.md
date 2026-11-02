# exS02 – Point-like monoenergetic isotropic source

## Purpose

This example introduces isotropic emission for a point-like source.

It isolates the angular behavior, without modifying energy, position,
or spatial extent.

## What this example demonstrates

- Point-like source with zero spatial extent
- Monoenergetic emission
- Isotropic angular distribution

## What this example does NOT demonstrate

- Any geometry definition
- Any scoring configuration
- Extended sources (disk or volume)
- Energy or angular distributions beyond isotropy

No assumptions are made about geometry or scoring.
Both are intentionally left empty.

## Conceptual focus

Isotropic emission is an explicit choice.

When a source is isotropic:
- no direction vector is defined
- particles are emitted uniformly over solid angle

The source position and energy remain unchanged.

## Why this example exists

This example prevents implicit assumptions about angular behavior.

Isotropy is not a default.
It must be explicitly requested.
