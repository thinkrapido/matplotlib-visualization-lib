"""
Utility functions to load the timeseries data
"""

import numpy as np
import pandas as pd

from pathlib import Path

def load_symbols(symbol: list[str], dir: Path = Path().resolve()) -> pd.DataFrame:
    pass

def load_symbol(symbol: str, dir: Path = Path().resolve(), interval='1m') -> pd.DataFrame:
    df = pd.read_csv(f'{str(dir)}/data/{interval}/datapoints-{symbol}.csv', header=None)
    df.columns = ['timestamp_nanos', 'end_timestamp_nanos', 'open', 'high', 'low', 'close', 'volume', 'data_points']
    for col in ['timestamp_nanos', 'end_timestamp_nanos']:
        df[col] = pd.to_datetime(df[col], unit='ns')
    for col in ['open', 'high', 'low', 'close', 'volume', 'data_points']:
        df[col] = df[col] * pow(10, -9)
    df['data_points'] = df['data_points'].astype(int)
    df = df.set_index('timestamp_nanos')
    return df

def add_atr_column(df: pd.DataFrame) -> pd.DataFrame:
    prev_close = df.iloc[:-1]['close'].to_numpy()
    high = df.iloc[1:]['high']
    low = df.iloc[1:]['low']
    df['atr'] = pd.Series(np.max(np.array([np.abs(high - prev_close).dropna(), np.abs(low - prev_close).dropna()], np.abs(high - low).dropna()), axis=0), index=high.index)
    df = df.dropna()
    return df

def add_dayofweek_column(df: pd.DataFrame) -> pd.DataFrame:
    df['weekday'] = df.index.dayofweek
    return df


def set_interval(df: pd.DataFrame, freq: str) -> pd.DataFrame:
    grouper = df.groupby(pd.Grouper(level='timestamp_nanos', freq=freq))
    out = pd.DataFrame()
    out['open']         = grouper['open'].first()
    out['high']         = grouper['high'].max()
    out['low']          = grouper['low'].min()
    out['close']        = grouper['close'].last()
    out['volume']       = grouper['volume'].sum()
    out['data_points']  = grouper['data_points'].sum()
    return out
