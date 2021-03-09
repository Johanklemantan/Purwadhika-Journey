USE sql_store;

SELECT * FROM order_items;

SELECT * FROM order_items oi JOIN sql_inventory.products sqip ON oi.product_id = sqip.product_id;

USE sql_inventory;

SELECT * FROM products;