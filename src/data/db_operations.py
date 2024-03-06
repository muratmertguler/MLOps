import pandas as pd
from sqlalchemy import create_engine
from src.utils import relative_paths

def read_to_db():
    engine = create_engine(relative_paths.sql_connection)
    query = "SELECT * FROM btc_usd"
    data = pd.read_sql(query, con=engine)
    engine.dispose()
    
    return data


def write_to_db():
    df = pd.read_csv(relative_paths.raw_data)
    engine = create_engine(relative_paths.sql_connection)
    df.to_sql('btc_usd', con=engine, if_exists='replace', index=False)
    engine.dispose()
