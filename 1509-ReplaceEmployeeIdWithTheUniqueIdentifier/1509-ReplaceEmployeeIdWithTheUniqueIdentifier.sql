-- Last updated: 11/1/2025, 9:32:57 PM
SELECT COALESCE(EmployeeUNI.unique_id, NULL) AS unique_id, Employees.name
-- COALESCE is unnessary, since joins by default gives NULL for empty values
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
