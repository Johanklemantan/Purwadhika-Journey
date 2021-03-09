USE sql_store;
select * from customers;
SELECT * FROM customers where birth_date > '1990-01-01' and points>1000;
SELECT * FROM customers where birth_date > '1990-01-01' or points>1000;
-- WHERE > AND > OR
-- ini
SELECT * FROM customers where birth_date > '1990-01-01' or points>1000 and state='VA';
-- dan ini hasilnya sama aja
SELECT * FROM customers where birth_date > '1990-01-01' or (points>1000 and state='VA ');

SELECT * FROM customers where (birth_date > '1990-01-01' or points>1000) and state='VA';

SELECT * FROM customers where birth_date > '1990-01-01';

SELECT * from customers where birth_date < '1990-01-01';

-- ini sama aja
SELECT * from customers where not (birth_date > '1990-01-01' or points > 1000);
-- not itu negasi 
-- (< menjadi >=)
-- (> menjadi <=)
-- (= menjadi !=)
-- (OR menjadi AND)
-- dengan ini
Select * from customers where birth_date <= '1990-01-01' and points <=1000;

 -- QUIZ
 Select * from order_items;
 
 Select * from order_items where (unit_price*quantity)>30;