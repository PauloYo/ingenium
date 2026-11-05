# Ingenium — Principles

How Ingenium is developed.

## 1. Understanding is a requirement

Working code is not enough. A step is only really done when:

```text
IT WORKS
+ I UNDERSTAND IT
+ I CAN EXPLAIN IT
+ I CAN CHANGE IT
```

## 2. Learning is part of the project

If an important prerequisite is missing, implementation may pause so the concept can be studied. This is not a detour. Learning is progress.

## 3. AI does not replace understanding

AI assistance is a tool for learning, review and acceleration. It should explain, suggest, review, debug, ask questions and show small examples, not turn development into a sequence of "copy this code".

The intended working loop:

```text
Problem → Concept → Architectural discussion → Small implementation
→ Explanation → Test → I explain what happened → Review → Next step
```

Useful questions to ask along the way:

- Why does this class exist?
- Who owns this responsibility?
- What would break if this interface were removed?
- How coupled are these modules?
- How does this request travel through the system?
- Could you add another implementation on your own?

## 4. Complexity must be earned

Do not introduce technologies or patterns because they are popular. Examples of things not to add too early: Kubernetes, Kafka, Redis, vector databases, microservices, complex agent frameworks, distributed architectures, heavy infrastructure.

Every new abstraction or tool must answer:

- What problem does it solve?
- Why do we need it now?
- What cost does it add?
- What would happen without it?

## 5. Architecture before frameworks

Ingenium must not become a wrapper around an agent or AI framework. Frameworks may be used later, but the architecture should be understood independently of them.

## 6. Start small

Prefer small, visible wins. "Ingenium receives a command" comes before "autonomous multi-agent system with memory, vision and robotics".

## 7. Separation of responsibilities

Build understanding of responsibility, cohesion, coupling, interfaces, dependencies, state, events and modularity, without speculative abstractions before a real problem exists.

## 8. The core should know little

The central flow should know as little as possible about specific implementations. Adding a new skill should ideally not require changing the central logic.

## 9. Structure emerges from real responsibilities

Directories, modules and abstractions appear when a real responsibility justifies them. Do not create folders such as `agents/`, `cores/`, `plugins/`, `event_bus/` or `workers/` because they might be useful someday.

## 10. Documentation is memory

The repository is the official memory of the project. Chats are workspaces; documentation holds the consolidated results. Document separately what actually exists and what is only future vision.

## 11. The project must always be resumable

At any stable point it should be possible to leave the project for months and then understand, without rereading old conversations: what Ingenium is, how it is developed, which decisions were made, which architecture really exists, what works, what does not, and what the next action is.

## 12. Always leave a clear next step

Do not end an important session without a clear next step recorded in [STATUS.md](STATUS.md).

## Planning

Ingenium does not depend on a specific project management tool. Planning should remain lightweight and may evolve over time. Regardless of the tool used, development should preserve:

- small milestones;
- a clear current objective;
- limited parallel work;
- explicit next actions;
- learning checkpoints.
