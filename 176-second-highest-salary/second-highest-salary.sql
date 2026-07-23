-- Write your PostgreSQL query statement below
-- first way: using subquery
-- SELECT 
--     max(salary) as SecondHighestSalary
-- from 
--     Employee
-- WHERE
--     salary < (SELECT MAX(salary) from Employee)

-- 2nd method using limit and offset 
-- SELECT (
--     SELECT DISTINCT salary
--     from Employee
--     order by salary desc
--     limit 1
--     offset 1
-- ) as SecondHighestSalary

-- using CTE
WITH temp_rank_table as (
    SELECT salary,
        DENSE_RANK() OVER (ORDER BY salary desc) as tr
    FROM Employee
)
SELECT MAX(salary) as SecondHighestSalary
from temp_rank_table
WHERE tr = 2

