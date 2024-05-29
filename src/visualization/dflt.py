
from typing import Callable, Optional
import pandas as pd

AxisTuple                           = tuple[Optional[float], Optional[float]]
AxisTupleDict                       = dict[str, AxisTuple]
DataFrameTransformer                = Callable[[pd.DataFrame], pd.DataFrame]
DataFrameToAxisTupleDictTransformer = Callable[[pd.DataFrame], AxisTupleDict]

def id_transformer(df: pd.DataFrame) -> pd.DataFrame:
    """
    identity function

    Args:
        df DataFrame: Input gets passed through without changing.

    Returns:
        DataFrame
    """
    return df

DEFAULT_AXIS: AxisTupleDict = { 'x': (None, None), 'y': (None, None)}

def dflt_axis_transformer(_: pd.DataFrame) -> AxisTupleDict:
    return DEFAULT_AXIS