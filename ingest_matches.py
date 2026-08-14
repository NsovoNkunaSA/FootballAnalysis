import requests
import pandas as pd
import mysql.connector

# -----------------------------
# 1. Get matches from SportScore
# -----------------------------

url = "https://sportscore.com/api/widget/matches/"

params = {
    "sport": "football",
    "limit": 10
}

response = requests.get(
    url,
    params=params,
    timeout=30
)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data["matches"])

# Convert scores to numbers
df["home_score"] = pd.to_numeric(
    df["home_score"],
    errors="coerce"
)

df["away_score"] = pd.to_numeric(
    df["away_score"],
    errors="coerce"
)

# Convert API time to MySQL-compatible datetime
df["time"] = pd.to_datetime(
    df["time"],
    errors="coerce"
).dt.tz_localize(None)

print(f"Retrieved {len(df)} matches from SportScore.")


# -----------------------------
# 2. Connect to MySQL
# -----------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="football_analysis"
)

cursor = connection.cursor()

print("Connected to MySQL.")


# -----------------------------
# 3. Create table
# -----------------------------

create_table_query = """
CREATE TABLE IF NOT EXISTS matches (
    match_url VARCHAR(500) PRIMARY KEY,
    home_team VARCHAR(255),
    away_team VARCHAR(255),
    home_score INT NULL,
    away_score INT NULL,
    status VARCHAR(50),
    status_text VARCHAR(100),
    match_time DATETIME,
    competition VARCHAR(255)
)
"""

cursor.execute(create_table_query)


# -----------------------------
# 4. Insert or update matches
# -----------------------------

insert_query = """
INSERT INTO matches (
    match_url,
    home_team,
    away_team,
    home_score,
    away_score,
    status,
    status_text,
    match_time,
    competition
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    home_score = VALUES(home_score),
    away_score = VALUES(away_score),
    status = VALUES(status),
    status_text = VALUES(status_text),
    match_time = VALUES(match_time)
"""

for _, row in df.iterrows():

    cursor.execute(
        insert_query,
        (
            row["url"],
            row["home"],
            row["away"],
            row["home_score"],
            row["away_score"],
            row["status"],
            row["status_text"],
            row["time"],
            row["competition"]
        )
    )

connection.commit()

print("Matches inserted/updated successfully.")

cursor.close()
connection.close()

print("MySQL connection closed.")