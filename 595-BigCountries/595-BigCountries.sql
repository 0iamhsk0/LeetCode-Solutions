-- Last updated: 11/1/2025, 9:33:33 PM
-- Write your PostgreSQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;