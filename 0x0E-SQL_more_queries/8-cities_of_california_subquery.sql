-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Find the state_id for California
SELECT @california_id := id FROM states WHERE name = 'California';

-- List all cities of California
SELECT id, name
FROM cities
WHERE state_id = @california_id
ORDER BY id;

