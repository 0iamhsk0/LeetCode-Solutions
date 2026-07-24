-- 1. using plain query
-- SELECT 
--     p.product_name, SUM(o.unit) as unit
-- FROM 
--     Products as p
-- JOIN
--     Orders as o
-- ON
--     p.product_id = o.product_id
-- WHERE 
--     o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
-- GROUP BY 
--     1
-- HAVING 
--     SUM(o.unit) >= 100

-- 2. Using CTE (creating temp table to extract items of february)
WITH feb_orders as (
    SELECT 
        product_id,
        SUM(unit) as total_units
    FROM Orders
    WHERE TO_CHAR(order_date, 'YYYY-MM') = '2020-02'
    GROUP BY 1
)

SELECT 
    p.product_name, 
    fb.total_units as unit
FROM Products as p
JOIN feb_orders as fb
ON fb.product_id = p.product_id
WHERE fb.total_units >= 100;