# dk-eda-viz

Boring, aesthetic EDA helpers for pandas — check missing data, summarize, and plot without matplotlib/seaborn defaults.

## Install

```bash
pip install dk-eda-viz
```

## Use

```python
import pandas as pd
import dk_eda_viz as eda

df = pd.read_csv("data.csv")
eda.summarize(df)
eda.check_na(df)
eda.plot_missing(df)
```

## Functions

| Function | What it does |
|----------|--------------|
| `check_na(df)` | Series of missing-value counts per column, worst first, zeros dropped. |
| `convert_types(df, mapping=None)` | Return a copy with dtypes cast — from a mapping, or auto-detected numeric/datetime. |
| `summarize(df)` | Plain dict of shape, dtypes, percent missing, and numeric vs categorical columns. |
| `plot_missing(df)` | Horizontal bar chart of percent missing per column, labeled on the bars. |
| `plot_dist(df, column)` | Histogram of one numeric column with the median marked in place. |

## Why this exists

pandas and matplotlib are the only dependencies — no seaborn, no plotly. The functions have boring, descriptive names and each does one job. The plots are styled with good visualization principles in mind — a high data-ink ratio, no chart junk, and direct labeling — rather than the loud matplotlib/seaborn defaults.
