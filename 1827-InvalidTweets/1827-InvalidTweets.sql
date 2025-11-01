-- Last updated: 11/1/2025, 9:32:49 PM
-- Write your PostgreSQL query statement below
SELECT tweet_id 
FROM Tweets
WHERE LENGTH(content) > 15;