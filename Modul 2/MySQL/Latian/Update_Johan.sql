USE sql_invoicing;

SELECT * FROM invoices;

UPDATE invoices SET payment_date = '2020-03-04' WHERE invoice_id = 5;

DESC invoices;

UPDATE invoices SET payment_total = DEFAULT, payment_date = DEFAULT WHERE invoice_id = 6;
-- INvoice no 2 kelebihan 10 dollar di invoice totalnya dan due datenya mau dikurangin 1 hari.
UPDATE invoices SET invoice_total = invoice_total-10, due_date = due_date-1 WHERE invoice_id = 2;
UPDATE invoices SET invoice_total = invoice_total-0, due_date = '2019-06-30' WHERE invoice_id = 2;

-- Invoice No 7 dibikin payment total sama kayak invoice total. dan due datenya sama kayak payment datenya
UPDATE invoices SET payment_total = invoice_total, payment_date = due_date WHERE invoice_id = 7;

-- QUIZZZ
