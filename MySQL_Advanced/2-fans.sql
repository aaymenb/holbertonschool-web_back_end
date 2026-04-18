-- Selects the origin and the sum of fans for each country
-- Grouped by origin and ordered by the total number of fans (descending)
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
