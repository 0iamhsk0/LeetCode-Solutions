-- Last updated: 11/1/2025, 9:33:14 PM
SELECT 
  p.project_id, 
  ROUND(AVG(e.experience_years), 2)::NUMERIC AS average_years
FROM Project p
INNER JOIN Employee e
USING (employee_id)
GROUP BY p.project_id;
