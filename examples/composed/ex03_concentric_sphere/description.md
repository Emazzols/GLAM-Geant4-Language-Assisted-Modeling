# ex03 – Concentric spheres with internal isotropic source

## Purpose

This example demonstrates how to combine:

- hierarchical concentric geometry
- an internal isotropic point source
- multi-volume energy scoring

It is designed to teach correct volume containment
and source placement logic within the DSL.

## Geometry description

Three solid spheres are defined with decreasing radii
and placed using a strict mother–daughter hierarchy:

- Outer sphere (`layer2`)
  - Material: Lead
  - Mother: world
- Middle sphere (`layer1`)
  - Material: Aluminum
  - Mother: layer2
- Inner sphere (`core`)
  - Material: PbWO4
  - Mother: layer1

Each inner volume is fully contained within its mother volume.
No assumptions are made about source behavior or scoring
beyond what is explicitly defined.

## Source description

A monoenergetic gamma point source is placed
at the exact geometric center.

The emission is isotropic,
with no preferred direction.

## Scoring strategy

Energy deposition is recorded independently
in all three volumes.

Scoring configuration is explicit
and independent from geometry definition.

## What this example teaches

- Concentric volumes require hierarchical placement
- Internal isotropic sources
- Multi-volume scoring
- Clear separation between geometry, source, and scoring
