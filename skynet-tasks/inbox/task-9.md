---
task_id: 9
agent: claude_code
priority: 3
task_type: code
created_at: 2026-04-20T11:35:28.747Z
---

# UI · empty states משופרים + demo seed endpoint

כשהמסכים ריקים, מבקרים חדשים לא מבינים את הערך. (1) POST /api/demo/seed שמזרים 2 ideas ו-2 tasks בסטטוסים שונים (agents כבר seed'ים). מוגן ע"י טוקן (אחרי משימה 01) או ע"י NODE_ENV!==production. (2) ב-empty state של TaskQueue ו-IdeaInbox — כפתור 'טען דוגמה'. (3) טקסטים ידידותיים שמסבירים את ה-flow: 'רעיון → משימה → ביצוע ע"י סוכן'. (4) לא לרוץ אוטומטית ב-production. (5) קישור קטן 'נקה דוגמה' שמוחק רק את פריטי ה-demo.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-9.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
