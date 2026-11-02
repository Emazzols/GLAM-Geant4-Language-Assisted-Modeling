# ex04 – Pinocchio

## Purpose

This example demonstrates how to construct a complex,
recognizable geometry by composing multiple primitive shapes
and placing them explicitly in space.

It teaches reasoning about positions, distances,
and orientations in Geant4-style geometry,
not visual attachment or automatic containment.

## Geometry description

The geometry represents a stylized Pinocchio composed of:

- A spherical head acting as the main reference volume
- Two flat cylindrical eyes
- A thin box representing the mouth
- A conical nose
- A conical hat rotated to point upward

All components are placed manually in the global reference frame.
No assumptions are made about containment or snapping.

## Geometric principle

Geant4 evaluates spatial relationships using
center-to-center distances.

Placing an object “on top of” another one
requires explicit computation of placement offsets.

This rule is reflected directly in the placement coordinates.

## Source description

A spherical electron source with finite spatial extent
is placed at the origin.

The source is monoenergetic and isotropic.
It is explicitly not point-like.

## Scoring strategy

Energy deposition is recorded only in the head volume.

All other volumes are passive
and affect transport without producing scoring output.

## What this example teaches

- Composition of complex geometries from primitives
- Manual placement in the global reference frame
- Center-based distance reasoning
- Use of rotations to orient solids
- Separation between geometry, source, and scoring
