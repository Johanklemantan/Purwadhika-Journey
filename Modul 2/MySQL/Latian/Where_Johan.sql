-- > greater than 
-- >= greater than or equal
-- <= smaller than
-- <= smaller than or equal
-- = equal
-- != not equal
-- <> not equal

USE sql_store;

SELECT * from customers; 

SELECT * FROM customers where state='VA';

SELECT * FROM customers where state!='VA';

SELECT * FROM customers where state<>'VA';

SELECT * FROM customers where birth_date > '1990-01-01';

SELECT * FROM customers where phone = '804-427-9456';

SELECT * FROM customers where first_name = 'Elka';
-- QUIZ 
SELECT * FROM orders;

SELECT * FROM orders where order_date >='2019-01-01';

SELECT * FROM kuis1;
SELECT * FROM coba;