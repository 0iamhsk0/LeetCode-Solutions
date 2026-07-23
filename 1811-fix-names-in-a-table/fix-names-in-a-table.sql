-- SELECT user_id,
--        UPPER(LEFT(LOWER(name), 1)) || SUBSTRING(LOWER(name) FROM 2) AS name
-- FROM Users
-- ORDER BY user_id;

SELECT user_id,
       CONCAT(UPPER(LEFT(LOWER(name), 1)), SUBSTRING(LOWER(name) FROM 2)) AS name
FROM Users
ORDER BY user_id;
