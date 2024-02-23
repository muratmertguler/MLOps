import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("/home/mert/Desktop/MLOPS/bitcoin-forecast/data/raw/btc_usd.csv")

# standartScaler 
data_scalering = data.drop(['btc_timestamp'], axis=1).copy()
data_scalering = data_scalering.astype(np.float64)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_scalering)
scaled_data = pd.DataFrame(scaled_data, columns=data_scalering.columns)
scaled_data['btc_timestamp'] = data['btc_timestamp'].copy()
scaled_data['btc_vwap_org']  = data['btc_vwap'].copy() 
data = scaled_data.copy()

data['Datetime']   = pd.to_datetime(data['btc_timestamp']) #Replace 'time' with your actual datetime column name
data['year']       = data['Datetime'].dt.year
data['month']      = data['Datetime'].dt.month
data['dayofmonth'] = data['Datetime'].dt.day
data['dayofyear']  = data['Datetime'].dt.dayofyear
data['weekday']    = data['Datetime'].dt.weekday
data['date']       = data['Datetime'].dt.date
data['wntr_month'] = data['month'].apply(lambda x:1 if x in [11, 12, 1, 2] else 0)
data['month_label']= data['month'].map(lambda x:1 if x in [11, 12, 1, 2, 3] else (2 if x in [6, 7, 8, 9] else 3))
data['quarter']    = data['month'].map(lambda x:1 if x in [1, 2, 3] else (2 if x in [4, 5, 6] else (3 if x in [7, 8, 9] else 4)))
data['season']     = data['month'].map(lambda x:1 if x in [12, 1, 2] else (2 if x in [3, 4, 5] else (3 if x in [6, 7, 8] else 4)))
data['days']       = data['dayofmonth'].map(lambda x:1 if x < 5 else 0)
data["rolling_30"] = data['btc_vwap'].rolling(window=30).mean()

lag_periods = [1, 3, 5, 15,45, 60, 90]

for lag in lag_periods:
    data[f'btc_vwap_lag_{lag}'] = data['btc_vwap'].shift(lag)

        
# Drop rows with NaN values (resulting from shifting)
data.dropna(inplace=True)
data = data.drop("btc_timestamp", axis=1)
data.set_index('Datetime', inplace=True)
data = data.sort_index()
data = data.iloc[:-1]


# Encode cyclical features
def encode(data, col, max_val):
    data[col + '_sin'] = np.sin(2 * np.pi * data[col] / max_val)
    data[col + '_cos'] = np.cos(2 * np.pi * data[col] / max_val)
    return data

data = encode(data, 'dayofyear', 365)
data = encode(data, 'weekday', 52)
data = encode(data, 'month', 12)

data.to_csv("/home/mert/Desktop/MLOPS/bitcoin-forecast/data/external/btc_usd_features.csv", index=False)
