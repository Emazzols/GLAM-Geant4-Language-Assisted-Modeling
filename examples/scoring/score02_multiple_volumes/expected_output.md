# Expected Output – score02

## Qualitative behavior

- Energy deposition is recorded in every volume defined in the geometry.
- Each volume produces its own independent energy deposition data.

## Observable consequences

- The output contains entries associated with all volume names:
  `cube_1`, `cube_2`, and `cube_3`.
- No volume present in the geometry is missing from the scoring output.

## Diagnostic interpretation

- If any volume defined in the geometry does not appear in the output,
  the scoring configuration is incomplete or incorrect.
- If no volumes appear in the output, scoring may not be enabled
  or no particles intersect the geometry.

There are no asumptions on the source