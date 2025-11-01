-- Last updated: 11/1/2025, 9:32:52 PM
SELECT 
  contest_id, -- 1
  ROUND(COUNT(user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage -- 2
FROM Register
GROUP BY 1
ORDER BY 
  2 DESC,
  1 ASC;
