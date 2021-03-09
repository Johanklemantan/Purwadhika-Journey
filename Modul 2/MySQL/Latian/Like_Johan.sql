Use sql_store;

SELECT * FROM customers;

select * from customers where last_name like 'brush%' ;

SELECT * FROM customers WHERE last_name LIKE '%b%';

-- ada y nya
SELECT * FROM customers WHERE last_name LIKE '%y%';

-- diakhiri dengan y
SELECT * FROM customers WHERE last_name LIKE '%y';

-- diawali dengan y
SELECT * FROM customers WHERE last_name LIKE 'y%';

-- ada 5 huruf, gatau belakangnya y
SELECT * FROM customers WHERE last_name LIKE '_____y';

-- r, kosong 4, belakangnya y. 1 _ mewakili 1 huruf
SELECT * FROM customers WHERE last_name LIKE 'r____y';

-- QUIZ
SELECT * FROM customers where phone not like '%8%' and (address like '%trail%' or address like '%avenue%');


