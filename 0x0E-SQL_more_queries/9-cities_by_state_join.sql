-- lists all cities contained in the database hbtn_0d_usa.
SELECT id, name
FROM cities
INNER JOIN states
ON states.name = states.name ORDER BY cities.id;
