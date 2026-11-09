"""Generate inspectable release-readiness metrics and Power BI-friendly CSV."""
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(n):
 with (ROOT/'data'/n).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def generate():
 req=read('requirements.csv');tests=read('test_cases.csv');defects=read('defects.csv')
 counts=Counter(x['status'] for x in tests)
 total=len(tests);executed=counts['Passed']+counts['Failed'];passed=counts['Passed']
 covered={t['requirement_id'] for t in tests}
 critical=[t for t in tests if t['priority']=='Critical']
 open_high=[d for d in defects if d['status'] not in ('Closed','Resolved') and d['severity'] in ('High','Critical')]
 criteria={'all_requirements_covered':len(covered)==len(req),'execution_at_least_95pct':executed/total>=.95,'pass_rate_at_least_95pct':passed/executed>=.95 if executed else False,'all_critical_tests_pass':all(t['status']=='Passed' for t in critical),'no_open_high_or_critical_defects':not open_high,'no_blocked_tests':counts['Blocked']==0}
 metrics={'requirements':len(req),'requirements_covered':len(covered),'test_cases':total,'passed':passed,'failed':counts['Failed'],'blocked':counts['Blocked'],'not_run':counts['Not Run'],'execution_pct':round(executed/total*100,1),'pass_pct':round(passed/executed*100,1) if executed else 0,'open_high_critical_defects':len(open_high),'criteria':criteria,'release_decision':'GO' if all(criteria.values()) else 'NO-GO','data_note':'Synthetic demonstration, not production results'}
 (ROOT/'reports/metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
 with (ROOT/'reports/kpi_summary.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(['metric','value']);w.writerows((k,v) for k,v in metrics.items() if isinstance(v,(int,float,str)))
 print(json.dumps(metrics,indent=2));return metrics
if __name__=='__main__':generate()
