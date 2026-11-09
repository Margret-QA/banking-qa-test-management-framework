# Synthetic banking requirements and acceptance criteria

- **REQ-001**: Active sender and receiver required. Given both accounts active and funds sufficient, when a valid transfer is submitted, then it is eligible to complete.
- **REQ-002**: Reject insufficient funds. Given balance below transfer amount, when transfer is submitted, then no debit occurs and attempt is rejected.
- **REQ-003**: Daily limit 5,000 units. Given a transfer above limit, when submitted, then reject; at the exact limit, allow if other rules pass.
- **REQ-004**: Atomic update. Given a valid transfer, when committed, then source decreases and recipient increases by the same amount exactly once.
- **REQ-005**: Audit. Given any transfer attempt, when processed, then record reference, timestamp, amount and outcome.
- **REQ-006**: Amount validation. Given amount <= 0, when submitted, then reject without balance changes.

All amounts and rules are **illustrative**, not real banking policy. Test case mapping is in `data/test_cases.csv`.
