"""Data-cleaning helpers for pandas DataFrames.

Each function takes a pandas DataFrame, never mutates it in place, and
returns plain objects (Series, DataFrame, dict, ...).
"""

import pandas as pd


def check_na(df):
    """Return a Series of missing-value counts per column.

    Sorted highest-first; columns with zero missing values are dropped.

    Example
    -------
    >>> df = pd.DataFrame({"a": [1, None, 3], "b": [1, 2, 3]})
    >>> check_na(df)
    a    1
    dtype: int64
    """
    counts = df.isna().sum()
    return counts[counts > 0].sort_values(ascending=False)


def convert_types(df, mapping=None):
    """Return a copy of ``df`` with column dtypes converted.

    If ``mapping`` (e.g. ``{"age": "int"}``) is given, apply it with
    ``astype``. Otherwise auto-detect: object columns whose non-null values
    are all numeric become numeric, and object columns that are >90%
    date-parseable become datetime. Prints a line per converted column.

    Example
    -------
    >>> df = pd.DataFrame({"n": ["1", "2", "3"]})
    >>> convert_types(df)["n"].dtype
    n: object -> int64
    dtype('int64')
    """
    df = df.copy()
    if mapping is not None:
        return df.astype(mapping)
    for col in df.select_dtypes(include="object").columns:
        old = str(df[col].dtype)
        values = df[col].dropna()
        if values.empty:
            continue
        if pd.to_numeric(values, errors="coerce").notna().all():
            df[col] = pd.to_numeric(df[col], errors="coerce")
        elif pd.to_datetime(values, errors="coerce").notna().mean() > 0.9:
            df[col] = pd.to_datetime(df[col], errors="coerce")
        else:
            continue
        print(f"{col}: {old} -> {df[col].dtype}")
    return df
