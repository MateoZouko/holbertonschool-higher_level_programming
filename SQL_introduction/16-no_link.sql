-- script that lists all records of the table

-- script that lists the number of records with the same score in the table

SELECT *, COUNT(*) AS name
FROM second_table
ORDER BY score DESC;
