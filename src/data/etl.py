# Extract, Transform, Load
# from API

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta
import pandas as pd

# No keys required for crypto data
client = CryptoHistoricalDataClient()

now = datetime.now()
start_date = datetime(2021, 1, 1)
# Creating request object
request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD"],
                        timeframe=TimeFrame.Day,
                        start= start_date,
                        end=datetime(now.year, now.month, now.day))

btc_bars = client.get_crypto_bars(request_params)

df = btc_bars.df 

today = datetime.now()
yesterday = today - timedelta(days=1)

end_date = yesterday.strftime("%Y-%m-%d")
df["timestamp"] = pd.date_range(start=start_date, end=end_date)

colums_name = df.columns
btc_added_name = list()

for i in colums_name:
    btc_added_name.append(str("btc_" + i))

df.columns = btc_added_name

df.to_csv("/home/mert/Desktop/MLOPS/bitcoin-forecast/data/raw/btc_usd.csv", index=False)
