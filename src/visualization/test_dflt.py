
from .dflt import *
import pandas as pd

def test_id():
    df = pd.DataFrame()
    assert id_transformer(df).equals(df)