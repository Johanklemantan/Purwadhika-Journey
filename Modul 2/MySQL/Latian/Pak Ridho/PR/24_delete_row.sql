USE sql_store;

SELECT * FROM customers;

DELETE FROM customers WHERE customer_id = 23;

DELETE FROM customers WHERE customer_id IN (19,20,22);

-- DELETE FROM customers WHERE customer_id = (SELECT customer_id FROM customers WHERE first_name = 'Caca');


