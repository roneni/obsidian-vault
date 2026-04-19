# Skynet ↔ Nex Bridge

Skynet writes task files to `inbox/`.
Nex (and Eve/Venus) read from `inbox/`, execute, and write responses to `outbox/` with the same filename.
Once processed, Skynet moves the task file to `archive/`.

## Task file format (inbox/task-<id>.md)
```yaml
---
task_id: 42
agent: nex | eve | venus
priority: 1 | 2 | 3
task_type: code | research | creative | analysis | general
routing_reason: "Why Skynet picked this agent"
routing_confidence: 92
created_at: 2026-04-19T07:00:00Z
---
# <title>

<full task description with context items attached>

## Context from Data Center
- [Item 1 title](url)
- [Item 2 title](url)
```

## Response file format (outbox/task-<id>.md)
```yaml
---
task_id: 42
agent: nex
status: done | blocked | partial
duration_sec: 120
---
# Response

<Nex's full reply here — markdown is fine>
```

## Nex instructions
Add to your CLAUDE.md:
> Check `skynet-tasks/inbox/` every time you start. Process any files assigned to you (agent: nex/eve/venus matching your role). Write replies to `skynet-tasks/outbox/` with the same filename and push.
