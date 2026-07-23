-- Write your PostgreSQL query statement belo
SELECT 
    sell_date, COUNT(DISTINCT product) as num_sold, STRING_AGG(DISTINCT product, ',' ORDER BY product) as products
FROM 
    Activities
GROUP BY 
    sell_date
ORDER BY
    sell_date asc