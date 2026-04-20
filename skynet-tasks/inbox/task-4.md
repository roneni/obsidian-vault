---
task_id: 4
agent: claude_code
priority: 1
task_type: code
created_at: 2026-04-20T11:35:22.422Z
---

# API hardening · clientRequestId (idempotency) ב-POST /api/tasks

בלי מפתח אידמפוטנטי, ריטריי על timeout יוצר כפילויות גם בתור המשימות וגם בקבצי ה-inbox ב-GitHub. להוסיף שדה אופציונלי 'clientRequestId' (string, uuid) ל-insertTaskSchema. אם כבר קיימת משימה עם אותו clientRequestId ב-24 שעות האחרונות — להחזיר את המשימה הקיימת (200) במקום ליצור חדשה (201). דורש: עמודה חדשה client_request_id בטבלת tasks, אינדקס על (client_request_id, created_at), Drizzle migration. עדכן README + דוקומנטציה בקובץ שנוצר במשימה 11.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-4.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
