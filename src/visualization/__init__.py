"""
This is a python package for for simplifying visualizations utilizing matplotlib.
"""

from .dflt import *


def prepare_plt_data(
        raw             : pd.DataFrame, 
        transformer     : DataFrameTransformer          = id_transformer,
        index_filter    : DataFrameTransformer          = id_transformer,
        range_filter    : DataFrameToAxisTupleDictTransformer    = dflt_axis_transformer,
    ) -> tuple[pd.DataFrame, AxisTupleDict]:
    """
    Prepares the raw data into a format for usage with matplotlib.

    It also provides a dictionary of axis information.

    Keyword arguments:
        raw: 
            Provides the raw pd.DataFrame for the selection.
        transformer: 
            Transformation functino of raw the pd.DataFrame. (optional)
        index_filter: 
            Filter function for the transformed pd.DataFrame index. (optional)
        range_filter: 
            Filter function for the extraction of the range of the given axes. (optional)

    Returns:
        A tuple containing the transformed and filtered dataframe plus plot hints for the axis.
    """
    out = index_filter(transformer(raw))
    return out, range_filter(out)