-- SELECT 
--     m.employee_id,
--     m.name,
--     COUNT(e.employee_id) AS reports_count,
--     ROUND(AVG(e.age)) AS average_age
-- FROM employees e
-- JOIN employees m
--     ON e.reports_to = m.employee_id
-- GROUP BY m.employee_id, m.name
-- ORDER BY m.employee_id;

WITH emp_mgr_table AS (
    SELECT 
        e2.employee_id AS manager_id,
        e2.name AS manager_name,
        e1.employee_id AS sub_id,
        e1.age AS sub_age
    FROM Employees AS e1
    JOIN Employees AS e2
        ON e1.reports_to = e2.employee_id
)
SELECT 
    manager_id AS employee_id,
    manager_name AS name, 
    COUNT(sub_id) AS reports_count,
    ROUND(AVG(sub_age)) AS average_age
FROM emp_mgr_table 
GROUP BY 1, 2
ORDER BY 1;






