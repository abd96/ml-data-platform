import pandas as pd
from datetime import datetime
import os

# Ensure the output folder exists
os.makedirs("data/generated", exist_ok=True)

# Load raw interactions
df = pd.read_csv("data/raw/interactions.csv", parse_dates=["timestamp"])

# Feature engineering: aggregate by user_id
features = df.groupby("user_id").agg(
    click_count=("item_id", "count"),
    days_since_last_active=("timestamp", lambda x: (datetime.now() - x.max()).days)
).reset_index()

# Add required timestamp column for Feast
features["event_timestamp"] = datetime.now()

# Save to Parquet
features.to_parquet("data/generated/user_features.parquet", index=False)

print("user_features.parquet created with", len(features), "rows")
