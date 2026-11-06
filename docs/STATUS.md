# Ingenium — Status

_Where are we now? Read this first when resuming the project._

## Current phase

**Genesis — G1: Input**

## Current objective

Turn the one-shot entry point into a terminal session that accepts multiple text commands.

## What works

- G0 landed on `main` in PR #2. The reference environment pins Python 3.14.10 and uv 0.13.7.
- The current entry point, `src/main.py`, prints `Ingenium ready.` and exits. This was verified locally with Python 3.14.10.
- The merged GitHub Actions workflow runs the Windows smoke test and uses Claude Code to provide advisory PR reports and documentation patches as downloadable artifacts.

## Pending workflow change

The merged workflow still requests a Claude review on eligible PR pushes. The agreed simplification is to keep CI on each PR push and run Claude when a PR is ready for review or on demand. Track this as a separate workflow change.

## Next step

Implement a terminal loop that prints the startup message once, acknowledges multiple non-empty commands in the same session, ignores blank input and exits cleanly on `exit` or end of input. Update the Windows smoke test to feed commands and `exit` through standard input. The first isolated capability belongs to G2.
