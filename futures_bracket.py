import os, sqlalchemy as sa, pandas as pd
engine = sa.create_engine(os.getenv("POSTGRES_URL"))
pd.DataFrame({'team':[], 'prob':[]}).to_sql('futures', engine, if_exists='replace', index=False)
print("✅ futures_bracket – empty futures table")
