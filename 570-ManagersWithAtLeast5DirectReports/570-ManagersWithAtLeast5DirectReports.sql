-- Last updated: 11/1/2025, 9:33:35 PM
SELECT e1.name
FROM Employee e1
JOIN Employee e2 ON e1.id = e2.managerID
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) >= 5;
