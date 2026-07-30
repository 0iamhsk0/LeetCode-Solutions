-- MySQL:
-- select *, if(x+y>z and y+z>x and x+z>y, "Yes","No") as triangle from triangle

-- PostgreSQL:
SELECT *,
    CASE 
        WHEN(x+y>z AND x+z>y AND y+z>x)
        THEN 'Yes' ELSE 'No' 
    END AS triangle 
FROM triangle;
