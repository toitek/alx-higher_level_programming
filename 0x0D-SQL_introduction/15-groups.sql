-- Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Don’t list rows without a name value
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
