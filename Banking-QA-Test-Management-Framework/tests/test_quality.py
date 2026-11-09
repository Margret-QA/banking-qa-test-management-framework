import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate import check
from report import generate
class QualityTests(unittest.TestCase):
 def test_traceability_and_sql_integrity(self):check()
 def test_release_gate_is_no_go_for_seeded_defect(self):
  metrics=generate()
  self.assertEqual(metrics['release_decision'],'NO-GO')
  self.assertEqual(metrics['open_high_critical_defects'],1)
  self.assertEqual(metrics['requirements_covered'],metrics['requirements'])
if __name__=='__main__':unittest.main()
