-- This SQL script ranks country origins of metal bands by the number of
-- (non-unique) fans.
-- Orders the results by the total number of fans in descending order

SELECT origin, SUM(fans) AS 'nb_fans'
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
