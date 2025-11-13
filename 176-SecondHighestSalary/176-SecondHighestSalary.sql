-- Last updated: 11/13/2025, 11:17:35 PM
-- Write your PostgreSQL query statement below
SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee 
WHERE salary < (SELECT MAX(salary) FROM Employee)