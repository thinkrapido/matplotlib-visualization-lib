import numpy as np
import pandas as pd
from dataclasses import dataclass


def _poi(df, periods, gain_threshold):

    close = df['close'].to_numpy()[:-periods]
    close = close * np.ones((periods, len(close)))
    close = close.T

    high = (pd.DataFrame([window.to_list() for window in df['high'].rolling(periods)], index=df.index).dropna()[1:] - close) / close

    return (high > gain_threshold).any(axis=1)

def _goi(df, indicator):
    predictions = [ indicator(df, index ) for index in df.index ]
    return pd.Series([ p.value() for p in predictions ], index=df.index)

@dataclass
class Prediction:
    date: np.datetime64
    state: str
    hit: bool

    def value(self):
        return self.hit if self.state == 'valid' else False
    
    def is_incomplete(self):
        return self.state != 'incomplete'

def confusion_matrix(df, *, gain_threshold, periods, indicator):
    poi = _poi(df, periods=periods, gain_threshold=.02).to_numpy()
    goi = _goi(df, indicator=indicator).iloc[periods:].to_numpy()
    out = pd.DataFrame([(poi & goi), (poi & np.invert(goi)), (np.invert(poi) & goi), (np.invert(poi) & np.invert(goi))]).T
    out.columns=['TP', 'FP', 'FN', 'TN']
    out = out.sum()
    return out
