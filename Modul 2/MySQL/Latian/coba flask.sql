SELECT * FROM user_tab_new;

SELECT * FROM sopi_order;

SELECT COUNT(userid) from user_tab_new;
-- 1) Write an SQL statement to count the number of users per country (5 marks) 
SELECT country, count(userid) AS haha from user_tab_new GROUP BY country;
-- 2) Write an SQL statement to count the number of orders per country (10 marks)
SELECT * FROM user_tab_new ut JOIN sopi_order so USING(userid);
SELECT country, count(orderid) FROM user_tab_new ut JOIN sopi_order so USING(userid) GROUP BY country;
-- 3) Write an SQL statement to find the first order date of each user (10 marks)
SELECT * FROM user_tab_new ut JOIN sopi_order so USING(userid);
SELECT userid, min(order_time)
FROM user_tab_new ut JOIN sopi_order so
USING(userid)
GROUP BY userid;
-- 4) Write an SQL statement to find the number of users who made their first order in each country, each day (25 marks)
SELECT * FROM user_tab_new ut JOIN sopi_order so USING(userid);
SELECT  country,order_time, count(userid) 
FROM user_tab_new ut JOIN sopi_order so 
USING(userid)
GROUP BY country, order_time;
-- 5) Write an SQL statement to find the first order GMV of each user. If there is a tie, use the order with the lower orderid (30 marks)
SELECT userid, min(order_time) AS 'first order',gmv,orderid
FROM user_tab_new ut JOIN sopi_order so
USING(userid)
GROUP BY userid;
-- ORDER BY orderid ASC; 
-- 6) Find out what is wrong with the sample data (20 marks)	


Select * from no2;
Select * from no1;
Delete from no1 Where kuis110 = '8'






















