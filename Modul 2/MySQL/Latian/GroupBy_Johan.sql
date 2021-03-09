USE sql_store;

SELECT * FROM customers;
SELECT * FROM orders;
SELECT state, count(customer_id) AS total_Customer FROM customers GROUP BY state;

-- FL juga udah ke total
SELECT state, SUM(points) AS 'total points' FROM customers GROUP BY state;
-- Kalo mau di group by citynya aja.
SELECT state,city, SUM(points) AS 'total points' FROM customers GROUP BY city;

-- SAMA AJA
SELECT state,city, SUM(points) AS 'total points' FROM customers GROUP BY state,city;

SELECT state, SUM(points) AS total_points FROM customers GROUP BY state HAVING total_points > 1000
Order by total_points desc;
-- Setelah HAVING bsia pake apa aja.
SELECT state, SUM(points) AS total_points FROM customers GROUP BY state HAVING state REGEXP 'A$';

SELECT customer_id, COUNT(Order_id) AS 'Total Orders' FROM orders GROUP BY customer_id;

-- QUIZZ
SELECT * FROM clients;
SELECT * FROM invoinces;
SELECT * FROM payment_methods;
SELECT * FROM payments;

CREATE TABLE invoice_archived AS
SELECT 
	i.invoice_id,
    i.number,
    c.name AS client_name,
    i.invoice_total, 
    i.payment_total,
    i.invoice_date,
    i.due_date,
    i.payment_date
FROM invoices i
JOIN clients c
	USING (client_id)
WHERE payment_date IS NOT NULL;

SELECT * FROM invoice_archived;
SELECT * FROM customers;
desc customers;
