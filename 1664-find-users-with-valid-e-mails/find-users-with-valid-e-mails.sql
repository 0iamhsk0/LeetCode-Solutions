-- Write your PostgreSQL query statement below
SELECT 
    *
FROM 
    Users
WHERE 
    mail ~ '^[A-Za-z]+[A-Z0-9a-z\_\.\-]*@leetcode\.com$'