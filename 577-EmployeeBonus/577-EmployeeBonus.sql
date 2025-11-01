-- Last updated: 11/1/2025, 9:33:34 PM
-- Write your PostgreSQL query statement below
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
ON b.empID = e.empID
WHERE b.bonus < 1000
OR b.bonus IS NULL