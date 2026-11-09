# Ingenium — Status

_Where are we now? Read this first when resuming the project._

## Current phase

**Genesis — G2: First Skill** (G1 concluído, aguardando merge do PR para `main`)

## Current objective

Run an isolated capability (candidate: `system_status`) from the terminal loop, without putting its logic inside `src/main.py`.

## What works

- G0 landed on `main` in PR #2. The reference environment pins Python 3.14.10 and uv 0.13.7.
- G1 is implemented on `genesis/g1-input`: `src/main.py` prints `Ingenium ready.` once, accepts multiple non-empty commands in the same session, ignores blank input and exits on `exit` or end of input. Both tests in `tests/test_cli.py` pass.
- The merged GitHub Actions workflow runs the Windows smoke test and uses Claude Code to provide advisory PR reports and documentation patches as downloadable artifacts.

## Pending workflow change

The merged workflow still requests a Claude review on eligible PR pushes. The agreed simplification is to keep CI on each PR push and run Claude when a PR is ready for review or on demand. Track this as a separate workflow change.

## Next step

Merge the G1 PR into `main`. Then implement the first isolated capability (`system_status`) behind a lookup, so the main flow does not change. The architectural test for G3 is adding a second skill without changing the central flow.
