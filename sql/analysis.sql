CREATE DATABASE football_analysis;
CREATE DATABASE IF NOT EXISTS football_analysis;

USE football_analysis;


DROP TABLE IF EXISTS matches;

CREATE TABLE matches (
    match_url VARCHAR(500) PRIMARY KEY,
    home_team VARCHAR(255),
    away_team VARCHAR(255),
    home_score INT NULL,
    away_score INT NULL,
    status VARCHAR(50),
    status_text VARCHAR(100),
    match_time DATETIME,
    competition VARCHAR(255)
);

DESCRIBE matches;

SELECT COUNT(*) AS total_matches
FROM matches;