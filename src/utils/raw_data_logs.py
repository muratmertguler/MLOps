
import json
import numpy as np
import pandas as pd
from datetime import datetime
from src.utils import relative_paths

def save_raw_data_logs():

    df = pd.read_csv(relative_paths.raw_data)
    df_timestamp = df["btc_timestamp"].copy()
    df = df.drop("btc_timestamp", axis=1)

    numerical_columns = df.select_dtypes(include=[np.number])
    mean_raw = round(numerical_columns.mean(), 3)
    std_raw  = round(numerical_columns.std(), 3)
    length_raw  = len(numerical_columns)

    stats_dict = {
        "data save date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "mean": mean_raw.to_dict(),
        "std":  std_raw.to_dict(),
        "lenght": length_raw,
        "start date": datetime.strptime(str(df_timestamp.iloc[0]), '%Y-%m-%d').strftime('%Y-%m-%d'),
        "end date"  : datetime.strptime(str(df_timestamp.iloc[-1]), '%Y-%m-%d').strftime('%Y-%m-%d')
    }


    with open(relative_paths.raw_data_logs, 'r') as existing_file:
        existing_data = json.load(existing_file)
        
    existing_data.update(stats_dict)

    with open(relative_paths.raw_data_logs, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

