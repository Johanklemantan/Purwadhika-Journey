SELECT * FROM bonus;
SELECT * FROM worker;
SELECT * FROM title;
-- Q-1. Write an SQL query to fetch “FIRST_NAME” from Worker table using the alias name as <WORKER_NAME>.
SELECT FIRST_NAME AS WORKER_NAME FROM worker;

-- Q-2. Write an SQL query to fetch “FIRST_NAME” from Worker table in upper case.
SELECT upper(FIRST_NAME) from worker;

-- Q-3. Write an SQL query to fetch unique values of DEPARTMENT from Worker table.
SELECT DISTINCT(DEPARTMENT) from worker;

-- Q-4. Write an SQL query to print the first three characters of  FIRST_NAME from Worker table.
SELECT substring(FIRST_NAME,1,3) FROM worker;

-- Q-5. Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
SELECT instr(FIRST_NAME,Binary'a') from worker
WHERE FIRST_NAME = 'Amitabh';

-- Q-6. Write an SQL query to print the FIRST_NAME from Worker table after removing white spaces from the right side.
Select RTRIM(FIRST_NAME) from Worker;

-- Q-7. Write an SQL query to print the DEPARTMENT from Worker table after removing white spaces from the left side.
Select LTRIM(DEPARTMENT) from Worker;

-- Q-8. Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length.
Select distinct length(DEPARTMENT) from Worker;

-- Q-9. Write an SQL query to print the FIRST_NAME from Worker table after replacing ‘a’ with ‘A’.
Select REPLACE(FIRST_NAME,'a','A') from Worker;

-- Q-10. Write an SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. A space char should separate them.
Select CONCAT(FIRST_NAME, ' ', LAST_NAME) AS 'COMPLETE_NAME' from Worker;

-- Q-11. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending.
SELECT * FROM worker
ORDER BY FIRST_NAME ASC;

-- Q-12. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending.
SELECT * FROM worker
ORDER BY FIRST_NAME ASC, DEPARTMENT DESC;

-- Q-13. Write an SQL query to print details for Workers with the first name as “Vipul” and “Satish” from Worker table.
SELECT * FROM worker
WHERE FIRST_NAME IN ('Vipul','Satish');

-- Q-14. Write an SQL query to print details of workers excluding first names, “Vipul” and “Satish” from Worker table.
SELECT * FROM worker
WHERE FIRST_NAME NOT IN ('Vipul','Satish');

-- Q-15. Write an SQL query to print details of Workers with DEPARTMENT name as “Admin”.
SELECT * FROM worker
WHERE DEPARTMENT LIKE 'Admin%';

-- Q-16. Write an SQL query to print details of the Workers whose FIRST_NAME contains ‘a’.
SELECT * FROM worker
WHERE FIRST_NAME LIKE '%a%';

-- Q-17. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘a’.
SELECT * FROM worker
WHERE FIRST_NAME LIKE '%a';

-- Q-18. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets.
SELECT * FROM worker
WHERE FIRST_NAME LIKE '%h'
AND length(FIRST_NAME)=6;

Select * from Worker where FIRST_NAME like '_____h';

-- Q-19. Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000.
SELECT * FROM worker
WHERE SALARY between 100000 and 500000;

-- Q-20. Write an SQL query to print details of the Workers who have joined in Feb’2014.
SELECT * FROM worker
WHERE JOINING_DATE LIKE '2014-02%';

Select * from Worker where year(JOINING_DATE) = 2014 and month(JOINING_DATE) = 2;

-- Q-21. Write an SQL query to fetch the count of employees working in the department ‘Admin’.
SELECT COUNT(DEPARTMENT) FROM Worker
WHERE DEPARTMENT = 'Admin';

-- Q-22. Write an SQL query to fetch worker names with salaries >= 50000 and <= 100000.
SELECT CONCAT(FIRST_NAME,' ',LAST_NAME) AS NAME, SALARY FROM worker
WHERE SALARY between 50000 and 100000;

SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) As Worker_Name, Salary
FROM worker 
WHERE WORKER_ID IN 
(SELECT WORKER_ID FROM worker 
WHERE Salary BETWEEN 50000 AND 100000);

-- Q-23. Write an SQL query to fetch the no. of workers for each department in the descending order.
SELECT COUNT(DEPARTMENT) JUMLAH, DEPARTMENT FROM worker
GROUP BY DEPARTMENT
ORDER BY JUMLAH DESC;

-- Q-24. Write an SQL query to print details of the Workers who are also Managers.
SELECT * FROM title;
SELECT * FROM worker;
SELECT * FROM worker w
JOIN title t
on w.WORKER_ID = t.worker_ref_id
WHERE WORKER_TITLE = 'Manager';

-- Q-25. Write an SQL query to fetch duplicate records having matching data in some fields of a table.
SELECT WORKER_TITLE, AFFECTED_FROM, COUNT(*)
FROM Title
GROUP BY WORKER_TITLE, AFFECTED_FROM
HAVING COUNT(*) > 1;

-- Q-26. Write an SQL query to show only odd rows from a table.
SELECT * FROM worker;
SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) != 0;

-- Q-27. Write an SQL query to show only even rows from a table.
SELECT * FROM worker;
SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) = 0;

-- Q-28. Write an SQL query to clone a new table from another table.
CREATE TABLE WorkerClone LIKE Worker;

-- Q-29. Write an SQL query to fetch intersecting records of two tables.
SELECT * FROM worker
INTERSECT
SELECT * FROM title;

-- Q-30. Write an SQL query to show records from one table that another table does not have.
SELECT * FROM Worker
MINUS
SELECT * FROM Title;

-- Q-31. Write an SQL query to show the current date and time.
SELECT CURDATE();
SELECT NOW();

-- 32. Write an SQL query to show the top n (say 10) records of a table.
SELECT * FROM Worker ORDER BY Salary DESC LIMIT 10;

-- 33. Write an SQL query to determine the nth (say n=5) highest salary from a table.
SELECT TOP 1 Salary
FROM (
 SELECT DISTINCT TOP n Salary
 FROM Worker 
 ORDER BY Salary DESC
 )
ORDER BY Salary ASC;

-- Q-34. Write an SQL query to determine the 5th highest salary without using TOP or limit method.
SELECT *
FROM Worker W1
WHERE 5 = (
 SELECT COUNT( DISTINCT ( W2.Salary ) )
 FROM Worker W2
 WHERE W2.Salary >= W1.Salary
 );
 SELECT * FROM Worker
 WHERE WORKER_ID = 1
  order by salary desc;
  
  -- Q-35. Write an SQL query to fetch the list of employees with the same salary.
  SELECT * FROM worker w1, worker w2
  WHERE w1.SALARY=w2.SALARY
  AND w1.WORKER_ID!=w2.WORKER_ID;
 
 -- Q-36. Write an SQL query to show the second highest salary from a table.
 Select max(Salary) from Worker 
where Salary not in (Select max(Salary) from Worker);

-- Q-37. Write an SQL query to show one row twice in results from a table.
select FIRST_NAME, DEPARTMENT from worker W where W.DEPARTMENT='HR' 
union all 
select FIRST_NAME, DEPARTMENT from Worker W1 where W1.DEPARTMENT='HR';

-- Q-38. Write an SQL query to fetch intersecting records of two tables.
(SELECT * FROM Worker)
INTERSECT
(SELECT * FROM WorkerClone);

-- Q-39. Write an SQL query to fetch the first 50% records from a table.
SELECT *
FROM WORKER
WHERE WORKER_ID <= (SELECT count(WORKER_ID)/2 from Worker);

-- Q-40. Write an SQL query to fetch the departments that have less than five people in it.
SELECT * FROM worker;
SELECT DEPARTMENT, COUNT(WORKER_ID) as 'Number of Workers' FROM Worker GROUP BY DEPARTMENT HAVING COUNT(WORKER_ID) < 5;

-- Q-41. Write an SQL query to show all departments along with the number of people in there.
SELECT DEPARTMENT, COUNT(WORKER_ID) as 'Number of Workers' FROM Worker GROUP BY DEPARTMENT;

-- Q-42. Write an SQL query to show the last record from a table.
SELECT * FROM worker
WHERE WORKER_ID=(SELECT COUNT(FIRST_NAME) FROM worker);

-- Q-43. Write an SQL query to fetch the first row of a table.
SELECT * FROM worker
WHERE WORKER_ID=(SELECT min(worker_id) FROM worker);

-- Q-44. Write an SQL query to fetch the last five records from a table.
SELECT * FROM Worker WHERE WORKER_ID <=5
UNION
SELECT * FROM (SELECT * FROM Worker W order by W.WORKER_ID DESC) AS W1 WHERE W1.WORKER_ID <=5;

-- Q-45. Write an SQL query to print the name of employees having the highest salary in each department.
SELECT Concat(FIRST_NAME,' ',LAST_NAME) AS nama_gabung, max(salary), department
FROM worker
group by DEPARTMENT;

SELECT * FROM worker;

SELECT t.DEPARTMENT,t.FIRST_NAME,t.Salary from(SELECT max(Salary) as TotalSalary,DEPARTMENT from Worker group by DEPARTMENT) as TempNew 
Inner Join Worker t on TempNew.DEPARTMENT=t.DEPARTMENT 
 and TempNew.TotalSalary=t.Salary;
 
 -- Q-46. Write an SQL query to fetch three max salaries from a table.
 SELECT distinct SALARY FROM worker ORDER BY SALARY DESC LIMIT 3;
 SELECT distinct Salary from worker a WHERE 3 >= (SELECT count(distinct Salary) from worker b WHERE a.Salary <= b.Salary) order by a.Salary desc;
 
 -- Q-47. Write an SQL query to fetch three min salaries from a table.
  SELECT distinct SALARY FROM worker ORDER BY SALARY asc LIMIT 3;
  SELECT distinct Salary from worker a WHERE 3 >= (SELECT count(distinct Salary) from worker b WHERE a.Salary >= b.Salary) order by a.Salary desc;
  
  -- Q-48. Write an SQL query to fetch nth max salaries from a table.
  SELECT distinct Salary from worker a WHERE n >= (SELECT count(distinct Salary) from worker b WHERE a.Salary <= b.Salary) order by a.Salary desc;
  
  -- Q-49. Write an SQL query to fetch departments along with the total salaries paid for each of them.
  SELECT * FROM worker;
  SELECT DEPARTMENT, SUM(SALARY) FROM worker GROUP BY DEPARTMENT;
  
  -- Q-50. Write an SQL query to fetch the names of workers who earn the highest salary.
  SELECT CONCAT(FIRST_NAME,' ',LAST_NAME) AS NaMa, salary
  FROM worker
  ORDER BY SALARY DESC
  LIMIT 2;
  
  SELECT FIRST_NAME, SALARY from Worker WHERE SALARY=(SELECT max(SALARY) from Worker);
  
  SELECT CONCAT(FIRST_NAME,' ',LAST_NAME) AS NaMa, salary
  FROM worker
WHERE salary = (SELECT MAX(SALARY) FROM worker);