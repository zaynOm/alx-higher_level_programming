-- lists all the tables of a database
-- The database name will be passed as argument of mysql command
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();
