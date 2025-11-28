-- Last updated: 11/28/2025, 4:55:46 PM
# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5

