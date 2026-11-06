# Ingenium

> A modular personal AI platform for agents, local intelligence, automation, hardware integration and robotics.

Ingenium is a long-term engineering project focused on building a modular system capable of coordinating intelligent agents, AI models, software integrations and physical devices.

The project is intentionally designed to evolve incrementally, allowing new capabilities to be added without turning the entire system into a tightly coupled monolith.

At the same time, Ingenium is also a learning project. Its development prioritizes not only working software, but also a deep understanding of the architecture, code and engineering decisions behind it.

## Why "Ingenium"?

*Ingenium* comes from Latin and is associated with ideas such as:

- innate quality;
- natural capacity;
- talent;
- genius.

It is also historically related to the linguistic roots that eventually contributed to words such as *engineer*.

The name reflects the central idea behind the project:

> Build a system capable of acquiring and combining new capabilities through engineering.

Major components may also receive names inspired by Latin, Ancient Greek, Hebrew or other historical languages, always with a meaningful relationship to their responsibility.

## Vision

Ingenium is intended to evolve into a personal platform capable of coordinating multiple types of intelligent and automated systems.

Possible capabilities include:

- local Large Language Models;
- specialized AI agents;
- computer vision;
- image recognition;
- speech recognition;
- speech synthesis;
- audio processing;
- music-related agents;
- persistent memory;
- software automation;
- Arduino and ESP32 integration;
- sensors;
- cameras;
- electrical and mechanical control;
- home automation;
- robotics;
- distributed workloads across multiple machines.

These capabilities are expected to emerge gradually as the project evolves.

## Development Philosophy

Ingenium is both:

- a software engineering project;
- a learning project.

A core principle of the project is:

> Working code is not enough.

Important parts of the system should be understood well enough to be explained, modified and maintained without depending blindly on generated code or external frameworks.

The project favors:

- small and understandable increments;
- explicit responsibilities;
- modular growth;
- low coupling;
- cohesive components;
- architecture driven by real problems;
- abstractions with clear justification;
- technologies chosen for a reason;
- learning whenever an important prerequisite is missing.

AI assistance is used as a tool for learning, review and acceleration, not as a replacement for understanding.

## Architectural Direction

Ingenium is designed around the idea of independent capabilities that can be connected to a central system.

Conceptually, the project may evolve toward a structure similar to:

```text
                         INGENIUM
                            │
                    Orchestration Layer
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   Language AI          Perception           Automation
        │                   │                   │
       LLM              Vision/Audio         IoT/Hardware
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                          Agents
                            │
                    Skills / Integrations
```

This diagram represents the general direction of the project rather than a fixed implementation.

Actual architecture should emerge from real needs instead of being fully designed in advance.

## Project Structure

The repository is expected to grow incrementally.

The initial organization follows a simple structure:

```text
ingenium/
├── docs/
├── src/
├── tests/
├── README.md
└── .gitignore
```

### `docs/`

Contains the persistent knowledge of the project, including:

- project vision;
- engineering principles;
- architecture;
- important decisions;
- learning notes;
- historical development context.

### `src/`

Contains the Ingenium implementation.

Its internal structure should evolve as real responsibilities and modules emerge.

### `tests/`

Contains automated tests used to validate behavior and protect architectural expectations as the system grows.

## Project Memory

The repository is the authoritative source of project knowledge.

Development conversations and AI sessions may be used for exploration, but important conclusions should be persisted in documentation.

```text
docs/
├── PROJECT.md
├── PRINCIPLES.md
├── ARCHITECTURE.md
├── STATUS.md
├── ROADMAP.md
├── LEARNING.md
├── DECISIONS.md
└── sessions/
```

These documents exist to make the project understandable and resumable even after long periods without development.

Chat history should never be required to reconstruct the state or philosophy of Ingenium.

## Run locally

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) version 0.13.7. Open PowerShell in the repository root and run:

```powershell
uv sync --locked
uv run --locked python --version
uv run --locked python src/main.py
```

The last two commands should print `Python 3.14.10` and `Ingenium ready.`, respectively. The program then exits.

The Python version comes from `.python-version`. The `uv sync --locked` command creates the local `.venv/` environment and checks that `uv.lock` matches the project configuration.

## Technology Direction

Python is the initial implementation language due to its ecosystem and low friction for areas that Ingenium is expected to explore, including:

- artificial intelligence;
- automation;
- computer vision;
- audio;
- APIs;
- hardware integration.

This does not imply that every future component must use Python.

Other languages may be introduced when a concrete technical need justifies them.

## Infrastructure Direction

Ingenium is expected to eventually operate on dedicated local infrastructure, likely using Linux.

Future workloads may include:

- local AI inference;
- persistent services;
- GPU workloads;
- computer vision;
- audio processing;
- IoT communication;
- robotics.

Infrastructure should remain flexible enough to support multiple machines or specialized nodes if that becomes necessary.

The system should avoid assuming that every capability must execute on the same computer.

A possible future topology could resemble:

```text
                   Ingenium
                      │
          ┌───────────┼───────────┐
          │           │           │
       AI Node     Vision Node   IoT Node
          │           │           │
         GPU         GPU/CPU     CPU/MCU
```

## Hardware and Physical Systems

One of Ingenium's long-term goals is to bridge software intelligence with physical systems.

Potential integrations include:

```text
Ingenium
    │
    ├── ESP32
    ├── Arduino
    ├── Sensors
    ├── Cameras
    ├── Relays
    ├── Motors
    ├── Servos
    └── Robotic Systems
```

The goal is not merely to execute scripts, but to eventually allow intelligent agents to perceive, reason and interact with the physical environment through controlled integrations.

## Guiding Principle

Ingenium should become more capable over time.

But capability alone is not the goal.

The project should also produce better engineering understanding.

> Build it.
> Understand it.
> Explain it.
> Improve it.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
