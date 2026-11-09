# Test Strategy — Simulated Internal Banking Transfers

## Objective and scope
Validate a synthetic internal transfer workflow for active accounts: eligibility, amount validation, limit enforcement, atomic ledger effects and audit trail. This is a demonstration of QA governance, not a real banking system.

## Test levels and types
Functional positive/negative, boundary, integration, data reconciliation, audit, and regression. Security, performance, accessibility and production integrations are **out of scope** for this limited simulation.

## Risk-based prioritization
Critical: insufficient funds and atomic updates. High: account state, daily limits and audit trail. Medium: invalid amount. Refer to `data/risks.csv` for likelihood, impact, mitigations and linked tests.

## Environments and data
SQLite in-memory database; deterministic synthetic customers and transactions; no customer data or real credentials. Execution catalog represents a **manually authored demonstration snapshot**, not automatically executed end-to-end banking tests.

## Entry criteria
Requirements approved for demonstration, synthetic database available, test cases reviewed, environment accessible, defect tracking in place.

## Exit criteria / release gates
100% requirements mapped; at least 95% execution; at least 95% pass rate among executed; all critical tests passed; no open high/critical defects; zero blocked tests. All conditions required for GO.

## Defect governance
Log → Triage → In Progress → Ready for Retest → Resolved → Closed, with Reopened where needed. Record priority, severity, reproducibility, affected build and retest evidence. The CSV contains a simplified status snapshot.

## Responsibilities
Test Manager owns plan, risk and go/no-go recommendation; QA analyst authors cases and evidence; developer investigates defects; business owner approves requirements; release owner makes final release decision.

## Reporting
Generate `reports/metrics.json` and `reports/kpi_summary.csv` with `python scripts/report.py`. Import CSV data into Power BI or open `dashboard/index.html` for interactive visual reporting.
