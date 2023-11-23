-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT cities.id AS id, cities.name AS name, states.name as name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
