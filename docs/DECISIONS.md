# Ingenium — Decisions

Relevant project decisions. A single file for now; if it grows too much, it may move to individual ADRs.

Format: id, title, status, context, decision, consequences.

---

## D-001 — Learning-first development

- **Status:** Accepted
- **Context:** Ingenium is both a software project and a learning project. AI can generate a lot of code that is copied without being understood.
- **Decision:** A step is complete only when it works and is understood, explainable and changeable. Learning pauses are part of progress.
- **Consequences:** Slower raw output, deeper understanding. AI is used to teach, review and accelerate, not to dump finished applications.

## D-002 — Repository as project memory

- **Status:** Accepted
- **Context:** The project may last months or years. Long chats lose context.
- **Decision:** The repository is the official memory. Conclusions from conversations are consolidated in `docs/`.
- **Consequences:** Documentation must be kept current, especially `STATUS.md`. Chat history is never required to resume the project.

## D-003 — Start without an LLM

- **Status:** Accepted
- **Context:** The first goal is to prove an extensible system exists.
- **Decision:** Genesis starts without any LLM.
- **Consequences:** Early capabilities are deterministic skills such as `system_status`. No AI provider keys or SDKs are needed yet.

## D-004 — Initial language: Python

- **Status:** Accepted
- **Context:** Ingenium will explore AI, vision, audio, automation, APIs and hardware.
- **Decision:** Python is the initial implementation language.
- **Consequences:** Other languages (for example C/C++ for firmware, Rust where justified) may be introduced when a concrete need appears.

## D-005 — Avoid premature infrastructure decisions

- **Status:** Accepted
- **Context:** Heavy infrastructure and hardware purchases based on imagined needs add cost and complexity.
- **Decision:** Ingenium runs on existing hardware until real workloads justify more. The architecture should not assume everything runs on one machine, but should not build distribution early either.
- **Consequences:** Server, GPU and multi-node decisions are deferred.
