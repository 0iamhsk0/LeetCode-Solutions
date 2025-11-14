-- Last updated: 11/14/2025, 11:33:41 PM
-- Write your PostgreSQL query statement below
SELECT employee_id
FROM Employees
WHERE salary < 30000
AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id