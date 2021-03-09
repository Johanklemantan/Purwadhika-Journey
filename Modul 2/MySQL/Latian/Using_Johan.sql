USE sql_store;

SELECT * FROM orders;
SELECT * FROM customers;

-- USING ( Harus sama persis nama kolomnya ).
SELECT * FROM orders JOIN customers USING (customer_id);
SELECT * FROM customers JOIN orders USING (customer_id)
JOIN shippers USING(shipper_id);

-- Using
SELECT * FROM clients;
SELECT * FROM invoices;
SELECT * FROM payment_methods;
SELECT * FROM payments;


-- QUIZ AZKAA
-- tampilkan semua client yang sudah melakukan pembayaran gunakan USING dalam query
SELECT p.date, c.name, p.amount, pm.name AS payment_method
FROM payments p JOIN clients c USING (client_id)
JOIN payment_method pm 
ON p.payment_method = pm.payment_method_id;

SELECT p.date,c.name,p.amount,pm.name AS payment_method
FROM payments p
JOIN clients c
	USING (client_id)
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id;