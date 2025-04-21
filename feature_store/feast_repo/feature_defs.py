from feast import Entity, FeatureView, Field, FileSource
from feast.types import Int64 
from datetime import timedelta


# 1. Define the entity: a user
user = Entity(name="user_id", join_keys=["user_id"])

# 2. Define where the data lives
user_stats_source = FileSource(
    path="data/generated/user_features.parquet",
    timestamp_field="event_timestamp"
)


# 3. Define the FeatureView
user_stats_fv = FeatureView(
    name="user_profile",  # feature group name
    entities=[user],
    ttl=timedelta(days=1),  
    schema=[
        Field(name="click_count", dtype=Int64),
        Field(name="days_since_last_active", dtype=Int64)
    ],
    source=user_stats_source
)