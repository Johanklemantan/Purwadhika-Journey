USe sql_store;

SELECT * FROM customers ORDER BY first_name;

SELECT * From customers order by first_name desc;

SELECT * FROM customers order by state desc, points;

SELECT * FROM customers order by birth_date;

-- QUIZ
SELECT * FROM order_items;

SELECT *, quantity * unit_price as total_price FROM order_items where order_id = 2 order by total_price desc