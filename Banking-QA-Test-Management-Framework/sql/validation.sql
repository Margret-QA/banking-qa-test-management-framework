-- SQL examples for data validation and reconciliation
SELECT transfer_id, amount_cents FROM transfers WHERE status='COMPLETED' AND amount_cents<=0;
SELECT transfer_id FROM transfers WHERE source_account=destination_account;
SELECT transfer_id FROM transfers WHERE status='COMPLETED' AND amount_cents>500000;
SELECT account_id,balance_cents FROM accounts WHERE balance_cents<0;
SELECT t.transfer_id FROM transfers t LEFT JOIN accounts a ON a.account_id=t.source_account WHERE a.account_id IS NULL;
-- All queries should return zero rows for the sample data.
