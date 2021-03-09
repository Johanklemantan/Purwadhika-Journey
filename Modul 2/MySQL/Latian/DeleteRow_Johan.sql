USE sql_store;

SELECT * FROM customers;

DELETE FROM customers WHERE customer_id = 15;

DELETE FROM customers WHERE customer_id IN (17,18,19);

DELETE FROM customers WHERE first_name = 'Thacher';


SELECT customer_id FROM customers WHERE first_name = 'Baliho'
AND last_name = 'Tompel'

