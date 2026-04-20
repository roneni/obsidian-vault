---
task_id: 11
agent: claude_code
priority: 2
task_type: code
created_at: 2026-04-20T11:35:31.133Z
---

# פיצ'ר · Activity Detail drawer לכל משימה

לוג הפעילות הוא flat list גלובלי — אין דרך לראות את הציר הזמן המלא של משימה בודדת. (1) כפתור/אייקון info על כל task ב-TaskQueue. (2) לחיצה פותחת Sheet מ-shadcn/ui עם: title, description מלא, assignedAgentId (עם אייקון וצבע), status, priority, createdAt/updatedAt, routingReason, routingConfidence. (3) Timeline של הפעילויות מ-GET /api/tasks/:id/activities (כבר קיים). (4) כפתורי פעולה: retry, re-dispatch, cancel, change agent. (5) ESC וקליק מחוץ סוגרים. (6) polling כל 4 שניות כמו ActivityLog. (7) keyboard accessible.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-11.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
