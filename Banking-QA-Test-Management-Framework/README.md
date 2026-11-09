# Banking QA Test Management Framework

**Independent portfolio demonstration using entirely synthetic banking data.** Shows a test manager's end-to-end approach to risk, coverage, defects, SQL data integrity and release readiness. This is **not** a production banking application and the manually authored test-execution snapshot is **not** evidence of executing a real banking system.

## What's included
- `docs/test-strategy.md` — scope, risks, entry/exit criteria and governance
- `docs/requirements-and-acceptance.md` — six banking requirements
- `docs/traceability.md` — requirement → test coverage
- `docs/defect-lifecycle.md` — Jira-style fictional defect records
- `docs/release-readiness.md` — NO-GO recommendation and remediation plan
- `data/*.csv` — requirements, tests, executions, risks, defects
- `sql/schema.sql`, `sql/validation.sql` — reproducible SQLite data and validation queries
- `scripts/validate.py` — referential integrity and SQL checks
- `scripts/report.py` — release gate calculations and KPI CSV/JSON
- `dashboard/index.html` — interactive status filter and KPI view
- `docs/powerbi-guide.md` — Power BI data model and example DAX

## Quick start (Python 3.9+, no third-party packages)
```bash
python scripts/validate.py
python scripts/report.py
python -m unittest discover -s tests -v
```
Open `dashboard/index.html` in Chrome or Edge. For Power BI, import the files in `data/` and follow `docs/powerbi-guide.md`.

## Seeded sample results
6 of 8 tests passed, 1 failed, 1 blocked. Execution 87.5%; pass rate among executed tests 85.7%. Six of six requirements have test coverage. High-severity open defect QA-102 triggers **NO-GO**.

## GitHub publication
Create a new repository named `banking-qa-test-management-framework`, upload the extracted contents, and link the repository from your portfolio's `banking-qa.html`. Add a screenshot of the dashboard and a sample release summary to make the project easier for recruiters to evaluate.

## Scope / honesty
The automated Python checks verify synthetic dataset integrity and traceability. They do not implement or run a real banking transfer service. The dashboard is a snapshot; rerun the reporting script after data changes. A native Power BI `.pbix` file is not included; CSVs and DAX instructions are provided.
