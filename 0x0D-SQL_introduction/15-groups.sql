-- list the number of records with the same score in second_table
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score;
