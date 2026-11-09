-- SYNTHETIC DEMONSTRATION DATA ONLY
CREATE TABLE IF NOT EXISTS accounts (account_id INTEGER PRIMARY KEY, customer_label TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('ACTIVE','INACTIVE')), balance_cents INTEGER NOT NULL CHECK(balance_cents>=0));
CREATE TABLE IF NOT EXISTS transfers (transfer_id TEXT PRIMARY KEY, source_account INTEGER NOT NULL REFERENCES accounts(account_id), destination_account INTEGER NOT NULL REFERENCES accounts(account_id), amount_cents INTEGER NOT NULL CHECK(amount_cents>0), status TEXT NOT NULL CHECK(status IN ('COMPLETED','REJECTED')), created_at TEXT NOT NULL);
DELETE FROM transfers; DELETE FROM accounts;
INSERT INTO accounts VALUES (101,'Synthetic Customer A','ACTIVE',125000),(102,'Synthetic Customer B','ACTIVE',75000),(103,'Synthetic Customer C','INACTIVE',30000);
INSERT INTO transfers VALUES ('TRX-001',101,102,25000,'COMPLETED','2026-11-09T09:00:00'),('TRX-002',101,102,800000,'REJECTED','2026-11-09T10:00:00');
