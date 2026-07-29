"""One-shot structural summary of a pandas DataFrame."""

import pandas as pd


def summarize(df):
    """Return a plain dict describing the shape and columns of ``df``.

    The dict has: ``rows``, ``columns``, ``column_names``, ``dtypes``
    (name -> dtype string), ``missing_pct`` (name -> percent missing,
    rounded to 1 decimal, only for columns that have missing values),
    ``numeric_columns``, and ``categorical_columns``. The input is not
    modified and nothing is printed.

    Example
    -------
    >>> df = pd.DataFrame({"a": [1, 2, None], "b": ["x", "y", "z"]})
    >>> summarize(df)
    {'rows': 3, 'columns': 2, 'column_names': ['a', 'b'],
     'dtypes': {'a': 'float64', 'b': 'object'},
     'missing_pct': {'a': 33.3},
     'numeric_columns': ['a'], 'categorical_columns': ['b']}
    """
    missing = df.isna().mean() * 100
    return {
        "rows": len(df),
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing_pct": {col: round(pct, 1) for col, pct in missing.items() if pct > 0},
        "numeric_columns": list(df.select_dtypes(include="number").columns),
        "categorical_columns": list(df.select_dtypes(include=["object", "category"]).columns),
    }
