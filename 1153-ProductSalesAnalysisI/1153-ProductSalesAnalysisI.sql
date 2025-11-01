-- Last updated: 11/1/2025, 9:33:17 PM
-- Write your PostgreSQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p 
USING(product_id) 