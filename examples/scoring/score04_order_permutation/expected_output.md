# Expected Output – score04

## Qualitative behavior

- Energy deposition is recorded only in the selected subset of volumes.
- The order of volume names in the scoring list does not affect the output.

## Observable consequences

- The output contains entries only for `cube_1` and `cube_3`.
- `cube_2` never appears in the scoring output.
- The output is identical to any configuration where the same volumes
  are listed in a different order.

## Diagnostic interpretation

- If `cube_2` appears in the output, the scoring configuration is incorrect.
- If either `cube_1` or `cube_3` produces no output despite particle traversal,
  the scoring configuration or volume naming is wrong.
- If changing the order of the scoring list alters the output,
  the implementation is incorrect.

There are no assumptions on the source.