# Power BI dashboard guide

Use Power BI Desktop → Get data → Text/CSV and import `data/test_cases.csv`, `data/requirements.csv`, `data/defects.csv`, `data/risks.csv` and `data/test_executions.csv`.

Relationships (one-to-many): Requirements[requirement_id] → TestCases[requirement_id]; TestCases[test_id] → Defects[test_id]; TestCases[test_id] → TestExecutions[test_id]. Keep Risk links as text unless normalized into a separate bridge table.

Example DAX measures:
```dax
Total Tests = COUNTROWS('TestCases')
Passed Tests = CALCULATE([Total Tests], 'TestCases'[status] = "Passed")
Failed Tests = CALCULATE([Total Tests], 'TestCases'[status] = "Failed")
Executed Tests = CALCULATE([Total Tests], 'TestCases'[status] IN {"Passed", "Failed"})
Execution % = DIVIDE([Executed Tests], [Total Tests], 0)
Pass % = DIVIDE([Passed Tests], [Executed Tests], 0)
```

Recommended visuals: KPI cards (total/executed/pass rate), status donut, requirements-to-tests table, defect severity/status matrix, risk heat map and a release gate summary. The HTML dashboard is provided for immediate browser preview; a `.pbix` file is **not** included.
