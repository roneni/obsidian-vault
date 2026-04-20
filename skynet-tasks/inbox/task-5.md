---
task_id: 5
agent: claude_code
priority: 1
task_type: code
created_at: 2026-04-20T11:35:23.849Z
---

# API hardening · zod validation + JSDoc לסמנטיקת priority

הקוד משתמש ב-ORDER BY priority ASC (1 = דחוף, 3 = נמוך) — הפוך מהאינטואיציה של רוב המפתחים. (1) JSDoc מפורט על הנדלר של POST /api/tasks ב-server/routes.ts שמסביר את הסמנטיקה. (2) zod refinement על priority: חייב להיות integer בטווח 1-3, הודעת שגיאה מסבירה '1=urgent, 2=normal, 3=low'. (3) אם מישהו שולח priority מחוץ לטווח — 400 עם ההודעה הזו. (4) ולידציה קיימת גם ב-PATCH.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-5.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
