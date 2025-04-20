import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Make sure the output directory exists
os.makedirs("data/raw", exist_ok=True)

# Simulate users, items, and categories
users = [f"user_{i}" for i in range(1, 101)]
items = [f"item_{i}" for i in range(1, 21)]
categories = ["tech", "sports", "health", "finance", "gaming"]

rows = []
for _ in range(5000):  # Generate 5K rows
    rows.append({
        "user_id": random.choice(users),
        "item_id": random.choice(items),
        "timestamp": datetime.now() - timedelta(days=random.randint(0, 30), minutes=random.randint(0, 1440)),
        "category": random.choice(categories),
        "session_length": random.randint(30, 900)  # seconds
    })

# Convert to DataFrame and save
df = pd.DataFrame(rows)
df.to_csv("data/raw/interactions.csv", index=False)

print("Generated data/raw/interactions.csv with", len(df), "rows")
