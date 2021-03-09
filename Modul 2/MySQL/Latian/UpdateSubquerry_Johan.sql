USE sql_invoicing;

SELECT * FROM invoices;

SELECT * FROM clients;

UPDATE invoices SET payment_total = invoice_total * 0.75 
WHERE client_id = (SELECT client_id FROM clients WHERE name = 'Myworks');

UPDATE invoices SET payment_total = invoice_total * 0.1
WHERE client_id = (SELECT client_id FROM clients WHERE name = 'Topiclounge') AND invoice_total = 180.17;