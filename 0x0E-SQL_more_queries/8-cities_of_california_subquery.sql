-- Lists all the citites of California that can be found in database hbtn_0d_usa

SELECT * FROM cities
WHERE state_id=1
ORDER BY name ASC;