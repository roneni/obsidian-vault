---
task_id: 3
agent: claude_code
priority: 1
task_type: code
created_at: 2026-04-20T11:35:21.136Z
---

# API hardening · X-Skynet-Token על /api/tasks ו-/api/tasks/:id/dispatch-nex

ה-endpoints ציבוריים לגמרי — כל מי שיש לו את ה-URL יכול ליצור משימות ולדחוף קבצים ל-inbox הפרטי של Obsidian ב-GitHub. לפני שיתוף רחב יותר: (1) middleware שמחייב header X-Skynet-Token על כל הבקשות הלא-GET ל-/api/tasks, /api/tasks/:id, /api/tasks/:id/dispatch-nex. (2) הטוקן נשמר ב-env var SKYNET_API_TOKEN ב-Vercel. (3) מחזיר 401 עם הודעה ברורה אם חסר/לא תקין. (4) ה-dashboard עצמו שולח את הטוקן מה-client (env var VITE_SKYNET_API_TOKEN ב-build time, או fetch proxy פשוט דרך /api/_internal שמכיר את ה-session). (5) לעדכן את הדוקומנטציה + להוסיף בדיקה ב-tests. קבצים: server/routes.ts, server/index.ts, client/src/lib/queryClient.ts.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-3.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
