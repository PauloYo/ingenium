# Ingenium — Roadmap

This is a direction, not a contract. It evolves as we learn.

## Phase 1 — Genesis

Genesis is a phase name, not necessarily a module of the system. Its goal is to discover and validate Ingenium's first architectural DNA.

The smallest interesting version:

```text
User
  ↓
Ingenium
  ↓
finds a capability
  ↓
runs that capability
  ↓
returns the result
```

No LLM at first, on purpose: we want to prove that an extensible system exists.

### First imagined feature

```text
$ ingenium

Ingenium ready.

> status

CPU: 7%
Memory: 5.3 GB / 16 GB
Uptime: 02:14:32
```

Condition: `status` must not be implemented directly inside the main program. Conceptually:

```text
main → input → capability lookup → SystemStatusSkill → operating system → result
```

First important architectural test: **can we add a second skill without changing the central flow?**

### Milestones

| Id | Name          | Goal                                                          |
|----|---------------|---------------------------------------------------------------|
| G0 | Foundation    | The repository exists and Python can run the project.         |
| G1 | Input         | Ingenium receives text commands.                              |
| G2 | First Skill   | Ingenium runs an isolated capability (candidate: `system_status`). |
| G3 | Extensibility | A second skill can be added without changing the main flow.   |

Later, Genesis may explore: skill discovery, a skill registry, automated tests, architectural review and learning checkpoints.

## Beyond Genesis

Not planned yet. Candidates from the long-term vision (see [PROJECT.md](PROJECT.md)) will be considered only when a real need appears.

## Infrastructure

No hardware will be bought based on imaginary requirements. Ingenium first runs on existing hardware. A dedicated Linux server (for example Ubuntu Server LTS) becomes a real concern only with real workloads: a permanent local LLM, 24/7 services, vision, audio, multiple agents or continuous processing. For local AI, GPU and especially VRAM matter more than many CPU cores.
