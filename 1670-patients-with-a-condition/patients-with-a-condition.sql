SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%'        -- starts at the very beginning
   OR conditions LIKE '% DIAB1%';     -- or starts right after a space
-- or using regex
-- WHERE conditions ~ '(^|\s)DIAB1'