# Expected Output

Several identical elongated volumes are visible inside the world volume,
each with a different orientation.

### Reference placement
- One volume appears unrotated and serves as a visual reference.

### Single-axis rotations
- Volumes rotated around the X and Y axes show clear changes in orientation.
- A rotation around the Z axis may appear subtle or visually unchanged due
  to the axial symmetry of the shape.

### Mixed rotations
- One volume is rotated using a sequence of rotations around multiple axes.
- The final orientation does not visually decompose into separate rotations.

This behavior is expected and correct.

Key observations illustrated by this example:
- Any sequence of rotations is equivalent to a single rotation around an
  arbitrary axis.
- Rotations are applied around local axes, which change after each step.
- The order of rotations matters.
- Visual intuition about multi-axis rotations is unreliable.

No assumptions are made about particle sources or scoring.
