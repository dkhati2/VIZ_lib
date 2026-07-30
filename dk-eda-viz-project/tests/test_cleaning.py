import pandas as pd

from dk_eda_viz import check_na


def test_check_na():
    df = pd.DataFrame({
        "a": [1, None, 3, None, None],  # 3 missing
        "b": [1, 2, 3, 4, 5],           # 0 missing
    })
    result = check_na(df)
    assert result["a"] == 3
    assert "b" not in result  # zero-missing columns are dropped
