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

print("Status:", response.status_code)

response.raise_for_status()

data = response.json()

matches = data["matches"]

df = pd.DataFrame(matches)

print("\nMatches:")
print(df)

print("\nColumns:")
print(df.columns.tolist())