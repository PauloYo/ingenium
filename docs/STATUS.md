# Ingenium — Status

_Where are we now? Read this first when resuming the project._

## Current phase

**Genesis — G0: Repository Foundation**

## Current objective

Close G0 by verifying the documented setup and first execution on Windows.

## What works

- The project pins Python 3.14.10 and uv 0.13.7.
- The Python 3.14.10 interpreter in the local virtual environment runs `src/main.py`, prints `Ingenium ready.` and exits successfully.

## In progress

- Verify the locked setup using the commands in the [README](../README.md).
- Confirm that the Windows smoke test passes on the G0 pull request.

## Next step

After G0 passes these checks, start G1 by adding a terminal loop that accepts multiple text commands, ignores empty input and exits on `exit`. Use a simple acknowledgement to verify input handling. The first isolated capability belongs to G2.
