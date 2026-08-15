import requests
import pandas as pd

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
df["home_score"] = pd.to_numeric(df["home_score"], errors="coerce")
df["away_score"] = pd.to_numeric(df["away_score"], errors="coerce")

print("\n===== FOOTBALL ANALYSIS =====")

print("Total matches:", len(df))

print(
    "Finished matches:",
    (df["status"] == "finished").sum()
)

print(
    "Live matches:",
    (df["status"] == "live").sum()
)

print(
    "Upcoming matches:",
    (df["status"] == "upcoming").sum()
)

print(
    "Total goals:",
    df["home_score"].fillna(0).sum()
    + df["away_score"].fillna(0).sum()
)

print(
    "Average goals per match:",
    round(
        (
            df["home_score"].fillna(0)
            + df["away_score"].fillna(0)
        ).mean(),
        2
    )
)

print("\nMatches by competition:")
print(df["competition"].value_counts())

print("\nData:")
print(df[[
    "home",
    "away",
    "home_score",
    "away_score",
    "status",
    "competition"
]])
