USE sql_store;

SELECT * FROM orders JOIN customers USING (customer_id)
JOIN shippers USING (shipper_id);

-- tampilkan semua client yang sudah melakukan pembayaran gunakan USING dalam query

SELECT p.date, c.name, p.amount, pm.name AS payment_method
FROM payments p
JOIN clients c
	USING (client_id)
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id;
    
SELECT * FROM payments;
SELECT * FROM clients;

