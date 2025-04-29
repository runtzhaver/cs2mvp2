"""ratings.py – builds a simple Elo (placeholder for Glicko‑2)"""
import os, sqlalchemy as sa, pandas as pd
engine = sa.create_engine(os.getenv("POSTGRES_URL"))
maps = pd.read_sql("SELECT * FROM maps", engine)

teams = pd.concat([maps['team_a'], maps['team_b']]).dropna().unique()
rating = {t: 1500.0 for t in teams}
K = 32
for _, row in maps.sort_values('begin_at').iterrows():
    a, b = row['team_a'], row['team_b']
    if pd.isna(a) or pd.isna(b): continue
    sa_score = 1 if row['team_a_score'] > row['team_b_score'] else 0
    ea = 1 / (1 + 10 ** ((rating[b] - rating[a]) / 400))
    rating[a] += K * (sa_score - ea)
    rating[b] += K * ((1 - sa_score) - (1 - ea))
pd.DataFrame({'team': list(rating), 'elo': list(rating.values())}).to_sql(
    'team_ratings', engine, if_exists='replace', index=False)
print("✅ ratings.py – elo table written")
