WITH numbered AS (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num,
        LEAD(num, 2) OVER (ORDER BY id) AS next_num2
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM numbered
WHERE num = next_num AND num = next_num2;