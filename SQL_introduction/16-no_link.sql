-- script that lists all records of the table

-- script that lists the number of records with the same score in the table

SELECT score name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
