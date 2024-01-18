-- 3-glam_rock.sql

-- Use the database
USE holberton;

-- Select the bands with Glam rock as their main style, ranked by longevity
SELECT
    band_name,
    CASE
        WHEN split = 0 THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
