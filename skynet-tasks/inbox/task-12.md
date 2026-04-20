---
task_id: 12
agent: claude_code
priority: 3
task_type: code
created_at: 2026-04-20T11:35:32.330Z
---

# A11y · שיפור ניגודיות muted-foreground ב-dark mode

ב-dark: --muted-foreground: 220 10% 65% על --background: 222 25% 6% — גבולי לטקסט קטן (empty states, תיאורי סוכנים, metadata). (1) להריץ contrast check על כל הצבעים ב-client/src/index.css. (2) להעלות lightness של muted-foreground ל-75-78% ב-dark mode. (3) לוודא שלא שובר primary/chart-*. (4) לבדוק גם את הטקסט של 'הטרי למעלה' ו-empty state copy. (5) צילומי מסך לפני/אחרי ב-commit message.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-12.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
