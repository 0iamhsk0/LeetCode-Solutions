-- Last updated: 11/1/2025, 9:32:40 PM
-- Write your PostgreSQL query statement below
SELECT 
    teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM 
    Teacher 
GROUP BY
    1;