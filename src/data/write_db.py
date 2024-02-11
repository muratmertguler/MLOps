import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine
import etl # Extract, Transform, Load
import pandas as pd

df = pd.read_csv("/home/mert/Desktop/MLOPS/bitcoin-forecast/data/raw/btc_usd.csv")

# PostgreSQL connection
engine = create_engine('postgresql://postgres:5052@localhost/finance')

# DataFrame is written in PostgreSQL database
df.to_sql('btc_usd', con=engine, if_exists='replace', index=False)

# close to connetion
engine.dispose()

