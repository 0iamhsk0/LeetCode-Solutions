-- Last updated: 11/14/2025, 11:34:32 PM
-- Write your PostgreSQL query statement below
SELECT email FROM Person
GROUP BY email
HAVING COUNT(email) > 1