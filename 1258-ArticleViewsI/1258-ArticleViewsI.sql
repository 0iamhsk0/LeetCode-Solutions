-- Last updated: 11/1/2025, 9:33:09 PM
-- Write your PostgreSQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;