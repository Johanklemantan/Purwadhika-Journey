USE sql_store;

SELECT * FROm customers LIMIT 4;

-- Limit (melompati data sebanyak berapa),(berapa yang mau ditampilkan)
SELECT * FROM customers LIMIT 3, 4;

-- QUIZ
SELECT * FROM customers 
order by points desc 
limit 3;

DESC customers