-- Lists all bands with 'Glam rock' as their main style
-- Ranked by longevity (lifespan) up to the year 2024
-- Column names: band_name and lifespan
SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
