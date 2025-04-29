import os, sqlalchemy as sa, pandas as pd
engine = sa.create_engine(os.getenv("POSTGRES_URL"))
pd.DataFrame({'team':[], 'delta':[]}).to_sql('standin_delta', engine, if_exists='replace', index=False)
print("✅ standin_delta – empty stand‑in table")
