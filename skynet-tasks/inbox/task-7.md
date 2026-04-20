---
task_id: 7
agent: claude_code
priority: 2
task_type: code
created_at: 2026-04-20T11:35:26.276Z
---

# UI · תיקון ערבוב RTL/LTR בכל ה-dashboard

טוקנים באנגלית בתוך משפטים בעברית שוברים כיווניות. דוגמאות על ה-site החי: 'Inbox · לכידת רעיונות', '(Ctrl+Enter) שמור', 'ה-Inbox ריק', 'אסוף מ-Nex'. פתרון: (1) לעטוף כל טוקן אנגלי בתוך טקסט עברי ב-<bdi> או <span dir="ltr" className="inline-block">. (2) במקומות שאפשר — תרגום טבעי: 'תיבת רעיונות', 'שמור (Ctrl+Enter)' כש-Ctrl+Enter ב-<bdi>, 'שליחה ל-Nex'. (3) לעבור שיטתית על client/src/components/**/*.tsx ו-client/src/pages/**/*.tsx. (4) לוודא שאין ערבוב שבור גם ב-placeholder, title, aria-label, tooltip.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-7.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
