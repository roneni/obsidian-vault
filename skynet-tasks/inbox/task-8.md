---
task_id: 8
agent: claude_code
priority: 2
task_type: code
created_at: 2026-04-20T11:35:27.442Z
---

# UI · מעבר מ-hash routing ל-browser history routing

כרגע ה-URL הוא https://skynet-teal.vercel.app/#/ — פוגע בשיתוף. לעבור ל-browser history עם wouter. (1) client/src/App.tsx — להסיר את ה-hash base של wouter ולהשתמש ב-default history. (2) ליצור/לעדכן vercel.json עם SPA rewrite שלא תופס את ה-API: { "rewrites": [{ "source": "/((?!api/).*)", "destination": "/" }] }. (3) לוודא ש-deep links עובדים: /, /architecture, /datacenter, ואם קיים /task/:id. (4) לבדוק ש-/api/* לא נשבר. (5) אופציונלי: הפניה 301 מ-/#/path ל-/path לתאימות לאחור.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-8.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
