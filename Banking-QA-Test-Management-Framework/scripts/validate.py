"""Synthetic QA checks; uses only Python standard library."""
import csv, sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    with (ROOT/'data'/name).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def check():
    reqs=load('requirements.csv'); cases=load('test_cases.csv'); defects=load('defects.csv')
    req_ids={r['requirement_id'] for r in reqs}; case_ids={c['test_id'] for c in cases}
    assert all(c['requirement_id'] in req_ids for c in cases),'Orphan test requirement'
    assert all(d['test_id'] in case_ids for d in defects),'Orphan defect test'
    assert all(r in {c['requirement_id'] for c in cases} for r in req_ids),'Requirement without test coverage'
    assert all(c['status'] in ('Passed','Failed','Blocked','Not Run') for c in cases)
    db=sqlite3.connect(':memory:');db.executescript((ROOT/'sql/schema.sql').read_text())
    checks={'negative_balance':'SELECT count(*) FROM accounts WHERE balance_cents<0',
      'invalid_completed_amount':"SELECT count(*) FROM transfers WHERE status='COMPLETED' AND amount_cents<=0",
      'missing_source':'SELECT count(*) FROM transfers t LEFT JOIN accounts a ON a.account_id=t.source_account WHERE a.account_id IS NULL',
      'self_transfer':'SELECT count(*) FROM transfers WHERE source_account=destination_account'}
    for label,query in checks.items():
        n=db.execute(query).fetchone()[0];assert n==0,f'{label}: {n} invalid rows'
    print(f'PASS: {len(reqs)} requirements, {len(cases)} cases, {len(defects)} defects, {len(checks)} SQL integrity checks')
if __name__=='__main__':check()
