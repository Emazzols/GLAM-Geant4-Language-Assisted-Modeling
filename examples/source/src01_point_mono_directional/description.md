# exS01 – Point-like monoenergetic directional source

## Purpose

This example introduces the simplest possible source configuration.

It defines a source in complete isolation, without assuming any geometry,
scoring, or detector setup.

## What this example demonstrates

- Definition of a point-like source
- Monoenergetic emission
- Fixed emission direction
- Explicit non-isotropic behavior

## What this example does NOT demonstrate

- Any geometry definition
- Any scoring configuration
- Extended sources (disk or volume)
- Energy or angular distributions

No assumptions are made about geometry or scoring.
Both are intentionally left empty.

## Conceptual focus

A source is a self-contained concept.

The source definition does not depend on:
- detector geometry
- scoring volumes
- materials

All parameters are explicit.
Nothing is implicit or inferred.

## Why this example exists

This example is the absolute baseline for all source configurations.

Every other source example is a controlled deviation from this one.
