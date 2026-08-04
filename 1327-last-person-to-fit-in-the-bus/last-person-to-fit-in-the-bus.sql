-- Write your PostgreSQL query statement below
WITH boarding as (
    SELECT person_name,
    SUM(weight) OVER (Order by turn) as bus_q_weight
    FROM Queue
)

-- SELECT person_name
-- FROM boarding
-- WHERE bus_q_weight <= 1000
-- ORDER BY bus_q_weight DESC
-- LIMIT 1
SELECT person_name
FROM boarding
WHERE bus_q_weight = (
    SELECT MAX(bus_q_weight)
    FROM boarding
    WHERE bus_q_weight <= 1000
)