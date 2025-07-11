-- Lists all records of second_table with specific score values
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
