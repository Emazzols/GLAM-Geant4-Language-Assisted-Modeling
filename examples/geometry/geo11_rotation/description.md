# geom_rotations

This example demonstrates how 3D rotations affect volume placement in a
hierarchical geometry system.

Several identical elongated volumes are placed in the world volume with
different rotations applied. The purpose is to illustrate how rotations
compose in three dimensions and how visual intuition can be misleading.

The example highlights that:
- rotations are applied sequentially on the same object
- each rotation acts on the local coordinate system resulting from previous rotations
- the final orientation is always equivalent to a single rotation around a specific axis

This example focuses exclusively on geometric placement and orientation.
No assumptions are made about particle sources or scoring configuration.
