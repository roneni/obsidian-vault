---
task_id: 13
agent: claude_code
priority: 2
task_type: code
created_at: 2026-04-20T11:35:33.605Z
---

# פיצ'ר · Command Palette (Cmd+K / Ctrl+K)

command palette גלובלי לניווט ופעולות מהירות. (1) cmdk דרך shadcn/ui CommandDialog (אם לא מותקן — להוסיף). (2) Cmd+K / Ctrl+K פותח. (3) פעולות: ניווט (דאשבורד, ארכיטקטורה, דאטה סנטר), יצירת משימה מהירה (dialog עם title + description + taskType + priority + assignedAgentId), יצירת רעיון, קפיצה למשימה לפי id, רשימת סוכנים (לחיצה פותחת drawer מת. 09). (4) fuzzy search על 20 המשימות ו-20 הרעיונות האחרונים. (5) keyboard-navigable לחלוטין. (6) תלוי במשימה 09 (ה-drawer). סדר ביצוע: 09 לפני 11.


## Response instructions
Write your reply to `skynet-tasks/outbox/task-13.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
