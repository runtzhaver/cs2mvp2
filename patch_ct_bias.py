import os, sqlalchemy as sa, pandas as pd
engine = sa.create_engine(os.getenv("POSTGRES_URL"))
maps = pd.read_sql("SELECT * FROM maps", engine)
maps['month'] = pd.to_datetime(maps['begin_at']).dt.to_period('M')
tbl = maps.groupby('month').apply(
    lambda g: (g['team_a_score'] > g['team_b_score']).mean()
).reset_index(name='ct_win_pct')
tbl.to_sql('ct_bias', engine, if_exists='replace', index=False)
print("✅ patch_ct_bias – table updated")
