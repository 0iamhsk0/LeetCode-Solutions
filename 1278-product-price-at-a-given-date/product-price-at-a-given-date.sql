WITH latest_prices AS (
    SELECT
        DISTINCT ON(product_id) product_id, 
        new_price as price
    FROM Products
    WHERE change_date <= '2019-08-16'
    ORDER BY product_id, change_date DESC
)

SELECT 
    DISTINCT p.product_id,
    COALESCE(lp.price, 10) as price
FROM 
    Products p
LEFT JOIN 
    latest_prices lp ON p.product_id = lp.product_id;