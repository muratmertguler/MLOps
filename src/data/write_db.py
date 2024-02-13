import psycopg2
from sqlalchemy import create_engine
import pandas as pd

def write_data():
    df = pd.read_csv("/home/mert/Desktop/MLOPS/bitcoin-forecast/data/raw/btc_usd.csv")
    engine = create_engine('postgresql://postgres:5052@localhost/finance')
    df.to_sql('btc_usd', con=engine, if_exists='replace', index=False)
    engine.dispose()


write_data()