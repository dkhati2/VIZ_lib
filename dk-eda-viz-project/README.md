# dk-eda-viz

Boring, aesthetic EDA helpers for pandas — check missing data, get a quick summary, and plot without matplotlib's default look.

[![PyPI](https://img.shields.io/pypi/v/dk-eda-viz)](https://pypi.org/project/dk-eda-viz/)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://pypi.org/project/dk-eda-viz/)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

## Install

```bash
pip install dk-eda-viz
```

## Quick start

```python
import pandas as pd
import dk_eda_viz as eda

df = pd.read_csv("data.csv")

eda.summarize(df)
eda.check_na(df)
eda.plot_missing(df)
eda.plot_dist(df, "salary")
```

## Functions

| Function | What it does |
|---|---|
| `check_na(df)` | Count of missing values per column, sorted worst-first |
| `convert_types(df, mapping=None)` | Convert column dtypes — auto-detect numeric/date strings, or pass an explicit mapping |
| `summarize(df)` | Shape, dtypes, missing %, and numeric/categorical columns in one dict |
| `plot_missing(df)` | Horizontal bar chart of missing % per column, labeled directly on the bars |
| `plot_dist(df, column)` | Histogram of one numeric column with the median marked |

## Why this exists

Most quick-EDA tooling either pulls in a pile of dependencies or defaults to matplotlib's out-of-the-box look. `dk-eda-viz` uses only `pandas` and `matplotlib`, with a small built-in style layer so every plot shares a consistent, dark, readable theme — no extra setup required.

## License

MIT — see [LICENSE](LICENSE).
