USE football_analysis;

SELECT COUNT(*) AS total_matches
FROM matches;

SELECT competition, COUNT(*) AS total_matches
FROM matches
GROUP BY competition
ORDER BY total_matches DESC;

SELECT SUM(COALESCE(home_score, 0) + COALESCE(away_score, 0)) AS total_goals
FROM matches;

SELECT AVG(COALESCE(home_score, 0) + COALESCE(away_score, 0)) AS average_goals_per_match
FROM matches;

SELECT match_url, home_team, away_team, home_score, away_score,
       home_score + away_score AS total_goals
FROM matches
ORDER BY total_goals DESC
LIMIT 10;

SELECT
    SUM(CASE WHEN home_score > away_score THEN 1 ELSE 0 END) AS home_wins,
    SUM(CASE WHEN away_score > home_score THEN 1 ELSE 0 END) AS away_wins,
    SUM(CASE WHEN home_score = away_score THEN 1 ELSE 0 END) AS draws
FROM matches;

SELECT
    100.0 * SUM(CASE WHEN home_score > away_score THEN 1 ELSE 0 END)
    / COUNT(*) AS home_win_percentage
FROM matches;

SELECT
    SUM(COALESCE(home_score, 0)) AS home_goals,
    SUM(COALESCE(away_score, 0)) AS away_goals
FROM matches;

SELECT status, COUNT(*) AS total_matches
FROM matches
GROUP BY status
ORDER BY total_matches DESC;
