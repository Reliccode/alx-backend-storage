-- 3-glam_rock.sql

-- Set the delimiter to handle semicolons within the script
DELIMITER $$

-- Create a function to calculate the lifespan
CREATE FUNCTION calculate_lifespan(formed_year INT, split_year INT) RETURNS INT
BEGIN
    DECLARE lifespan INT;
    SET lifespan = IF(split_year = 0, 2022 - formed_year, split_year - formed_year);
    RETURN lifespan;
END$$

-- Reset the delimiter
DELIMITER ;

-- Use the database
USE holberton;

-- Select the bands with Glam rock as their main style, ranked by longevity
SELECT band_name, calculate_lifespan(formed, split) AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
