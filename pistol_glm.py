import os, sqlalchemy as sa, pandas as pd
engine = sa.create_engine(os.getenv("POSTGRES_URL"))
# placeholder stub
pd.DataFrame({'stub':[]}).to_sql('pistol_model', engine, if_exists='replace', index=False)
print("✅ pistol_glm – stub model table written")
