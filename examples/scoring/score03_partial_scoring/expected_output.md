# Expected Output – score03

## Qualitative behavior

- Energy deposition is recorded only in the selected subset of volumes.
- Other volumes may receive energy, but no data is stored for them.

## Observable consequences

- The output contains entries only for `cube_1` and `cube_3`.
- `cube_2` never appears in the scoring output.

## Diagnostic interpretation

- If `cube_2` appears in the output, the scoring configuration is incorrect.
- If either `cube_1` or `cube_3` produces no output despite particle traversal,
  the scoring configuration or volume naming is wrong.

There are no assumpitons on the source.
