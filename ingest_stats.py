"""Quick-and-dirty PandaScore historical ingest (stats only)."""
import os, sys, requests, json, datetime, time, sqlalchemy as sa, pandas as pd
TOKEN = os.getenv("PANDASCORE_TOKEN", "")
if not TOKEN:
    sys.exit("Set PANDASCORE_TOKEN in environment or .env")
URL = "https://api.pandascore.co/cs2/games"
headers = {"Authorization": f"Bearer {TOKEN}"}
# TODO: implement paging & DB write
print("Stub ingest_stats.py executed – replace with real logic.")
