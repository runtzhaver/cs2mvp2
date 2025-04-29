import os, sqlalchemy as sa, pandas as pd, numpy as np
engine = sa.create_engine(os.getenv("POSTGRES_URL"))
maps = pd.read_sql("SELECT * FROM maps", engine)
vol = maps.groupby('team_a').size().reset_index(name='games')
vol['volatility'] = np.where(vol['games']>50, 'low', 'high')
vol.to_sql('roster_vol', engine, if_exists='replace', index=False)
print("✅ roster_vol – table written")
