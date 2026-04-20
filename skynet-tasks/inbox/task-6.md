---
task_id: 6
agent: claude_code
priority: 1
task_type: code
created_at: 2026-04-20T11:35:25.007Z
---

# תיעוד · עדכון README.md עם מפרט priority ו-API מלא

ה-bridge כבר בשימוש ע"י קוראים חיצוניים (בוט פרפלקסיטי וכו') ואין להם הסבר מסודר. ליצור/לעדכן README.md בשורש הריפו עם: (1) סקציית 'API' מלאה — כל endpoint, גוף הבקשה, דוגמת תגובה. (2) הבהרה מודגשת על priority: **1 = urgent/P0, 2 = normal, 3 = low** (ASC sort — מספר נמוך קודם). (3) דוגמאות curl לכל endpoint. (4) הסבר על autoRoute מול assignedAgentId ידני. (5) הסבר על dispatch-nex ו-GitHub inbox. (6) אזהרת אבטחה על authless state (ויוסר כשמשימה 01 תסגר).


## Response instructions
Write your reply to `skynet-tasks/outbox/task-6.md` then commit & push.
Use frontmatter: `task_id`, `agent`, `status` (done/blocked/partial), `duration_sec`.
