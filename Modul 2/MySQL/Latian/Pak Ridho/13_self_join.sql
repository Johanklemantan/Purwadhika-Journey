USE sql_hr;

SELECT * FROM employees e JOIN employees m
ON e.reports_to = m.employee_id;

SELECT e.employee_id, e.first_name AS karyawan, m.first_name AS manager FROM employees e JOIN employees m
ON e.reports_to = m.employee_id;