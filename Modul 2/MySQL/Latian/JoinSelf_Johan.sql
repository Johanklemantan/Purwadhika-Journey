USE sql_hr;

SELECT * FROM employees;

-- Yovonda gak muncul karena gaada pasangannya
SELECT * FROM employees e JOIN employees m
ON e.reports_to = m.employee_id;

-- Yovondanya muncul juga walaupun gaada pasangannya
SELECT * FROM employees e LEFT JOIN employees m
ON e.reports_to = m.employee_id;

Select e.employee_id, e.first_name as karyawan, m.first_name as manager 
From employees e JOIN employees m
ON e.reports_to = m.employee_id;





SELECT e.employee_id, e.first_name AS karyawan, m.first_name AS manager 
FROM employees e JOIN employees m
ON e.reports_to = m.employee_id;