-- Last updated: 11/12/2025, 11:32:53 PM
-- Write your PostgreSQL query statement below
SELECT 
    e1.name AS Employee
FROM 
    Employee AS e1
INNER JOIN 
    Employee e2 ON e1.managerID = e2.id
WHERE
    e1.salary > e2.salary


