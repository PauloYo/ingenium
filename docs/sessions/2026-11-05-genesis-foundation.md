# 2026-11-05 — Genesis foundation

## Discussed

- Ingenium's vision, identity, naming convention and private/public strategy.
- Development philosophy: learning-first, complexity must be earned, architecture before frameworks, the core should know little.
- Provisional concepts (may evolve; not a final architecture):
  - **Core:** specialized infrastructure for a domain (LLM execution, vision, audio, memory, communication).
  - **Agent:** an entity with a goal, context and a set of available capabilities.
  - **Skill:** a reusable capability (for example `get_system_status`, `turn_light_on`, `identify_person`, `play_audio`, `search_notes`).
  - **Integration:** a bridge to an external system (ESP32, Arduino, camera, API, Home Assistant).
  - **Plugin:** a package that could register one or more skills and integrations.
- Documentation structure for project memory.
- Planning stays tool-agnostic (GitHub Projects/Kanban dropped as an official commitment).

## Decisions

D-001 to D-006, recorded in [DECISIONS.md](../DECISIONS.md).

## Done

- Repository restarted from scratch: previous prototype files removed.
- Base structure created: `docs/`, `src/`, `tests/`, `README.md`, `.gitignore`.

## Open questions

- What is the minimal Python setup for G0 (entry point, packaging, how to run)?

## Next step

Genesis G0: discuss and create the first minimal Python execution inside `src/`.
