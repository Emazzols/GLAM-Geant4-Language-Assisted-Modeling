# Expected Output – score01

## Qualitative behavior

- Energy deposition is recorded only in the volume named `cube_2`.
- Volumes `cube_1` and `cube_3` do not produce any scoring output.

## Observable consequences

- All recorded hits are associated with the logical volume `cube_2`.
- No entries exist for `cube_1` or `cube_3`.

## Diagnostic interpretation

- If hits appear for `cube_1` or `cube_3`, the scoring configuration is incorrect.
- If no hits appear at all, either no particles intersect `cube_2`
  or scoring is not properly enabled.

This example serves as a baseline validation of scoring behavior.

There are no ssumptions on the source.