# Jira-style defect lifecycle (simulated)

`New → Triage → In Progress → Ready for Retest → Resolved → Closed` with `Reopened` for unsuccessful retests.

## QA-102 — High — Open
**Summary:** Transfer above configured daily limit is incorrectly accepted in a hypothetical build.
**Linked test:** TC-003; **requirement:** REQ-003; **expected:** reject amount > 5000; **observed (simulated):** accepted.
**Impact:** financial control bypass; **decision:** release blocker. **Evidence:** authored scenario only, not a captured real execution.

## QA-103 — Medium — In Progress
TC-007 blocked due to synthetic environment availability. Escalate environment dependency and rerun once available.

## QA-101 — Low — Closed
Minor UI text issue in TC-001, treated as resolved in the demonstration snapshot.
