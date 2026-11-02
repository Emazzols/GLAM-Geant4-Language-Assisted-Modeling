# ex02 – Stacked collimators with disk source and downstream detector

## Purpose

This example demonstrates a complete simulation in which
collimation is produced exclusively by geometry
and observed through a downstream detector.

The setup consists of an extended particle source,
a sequence of passive collimators,
and a sensitive detector.

## What this example demonstrates

- Cylindrical collimators with decreasing inner radius
- Sequential placement using stacked geometry
- Collimation achieved purely through absorption and geometry
- Use of a large disk-shaped particle source
- Separation between passive elements and sensitive detector
- Scoring enabled only on the detector volume

## What this example does NOT demonstrate

- Boolean solids
- Detector segmentation
- Scoring inside collimators
- Non-geometrical filtering or selection logic

## Conceptual focus

Collimators are passive volumes.

They modify the particle flux through geometrical acceptance
but are not sensitive themselves.

The effect of collimation is observed only by measuring
energy deposition in a downstream detector.

## Geometry overview

Three cylindrical collimators are defined with identical
outer radius and thickness, but decreasing inner radius.

They are placed sequentially along the global z axis
using a stacked placement with fixed spacing.

A box-shaped detector is placed downstream
as an independent volume.

## Source configuration

Particles are generated from a disk-shaped source
located upstream of the collimator stack.

The source emits particles along the +z direction,
allowing collimation effects to be clearly observed.

## Scoring configuration

Scoring is enabled exclusively on the detector volume.

No energy deposition is recorded in the collimators.
