-- Last updated: 11/21/2025, 7:23:43 PM
# Write your MySQL query statement below
SELECT customer_number
FROM Orders 
GROUP BY customer_number 
ORDER BY COUNT(*) DESC
LIMIT 1;