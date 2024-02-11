import pandas as pd
from sqlalchemy import create_engine


def get_data():
    # PostgreSQL veritabanı bağlantısı oluşturun
    engine = create_engine('postgresql://postgres:5052@localhost/finance')

    # SQL sorgusu ile veriyi DataFrame'e yükleme
    query = "SELECT * FROM btc_usd"

    # Bağlantıyı kapatma
    engine.dispose()
    
    return pd.read_sql(query, con=engine)



print(get_data())

