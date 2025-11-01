-- Last updated: 11/1/2025, 9:33:31 PM
-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE COALESCE(referee_id, 0) != 2;