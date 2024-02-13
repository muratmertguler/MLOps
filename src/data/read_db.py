import pandas as pd
from sqlalchemy import create_engine

def get_data():
    engine = create_engine('postgresql://postgres:5052@localhost/finance')
    query = "SELECT * FROM btc_usd"
    engine.dispose()
    
    return pd.read_sql(query, con=engine)


print(get_data())

