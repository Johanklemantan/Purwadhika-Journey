USE sql_store;

SELECT * FROM customers;

SELECT state, COUNT(customer_id) AS total_customer FROM customers GROUP BY state; 

SELECT state, city, SUM(points) AS total_points FROM customers GROUP BY state, city HAVING total_points > 1000;

SELECT customer_id, COUNT(order_id) AS 'total orders' FROM orders GROUP BY customer_id;