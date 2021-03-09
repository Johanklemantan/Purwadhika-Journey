USE sql_store;

SELECT order_id, order_date, c.customer_id, c.first_name, c.last_name, o.status, os.name as status
FROM orders o JOIN customers c ON o.customer_id = c.customer_id
JOIN order_statuses os ON o.status = os.order_status_id;

select * from order_statuses;