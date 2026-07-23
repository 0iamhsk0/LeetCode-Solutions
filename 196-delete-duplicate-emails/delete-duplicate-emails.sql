-- delete from person d
-- using person k
-- where d.email = k.email 
--     and d.id > k.id

-- or CTE method using window function to handle duplicates
-- WITH RankedMails as (
--     SELECT id,
--         ROW_NUMBER() OVER (PARTITION BY email ORDER BY id ASC) as rm
--     FROM Person
-- )
-- DELETE FROM Person
-- WHERE id in (
--     SELECT id
--     FROM RankedMails
--     WHERE rm > 1
-- )

-- Another way is to use subquery and remove the NON min ids
DELETE from person
WHERE id not in (
    SELECT min_id from (
        SELECT MIN(id)as min_id, email
        FROM person
        group by email
    ) as temp
);