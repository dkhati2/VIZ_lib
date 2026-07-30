import matplotlib.pyplot as plt
import pandas as pd

from ._style import apply_style, ACCENT, TEXT_LIGHT, TEXT_ON_ACCENT, BACKGROUND


def plot_missing(df):
    """Horizontal bar chart of percent missing per column, worst first.

    Value labels are drawn directly on each bar (inside it when there's room,
    just outside it in light text when the bar is too short to hold the label).
    """
    apply_style()
    missing = df.isna().mean() * 100
    missing = missing[missing > 0].sort_values(ascending=False)
    if missing.empty:
        print("No missing values found.")
        return None

    fig, ax = plt.subplots(figsize=(8, 0.5 * len(missing) + 1.5))
    bars = ax.barh(missing.index, missing.values, color=ACCENT, height=0.6)
    ax.invert_yaxis()
    ax.grid(axis="x", visible=True)
    ax.grid(axis="y", visible=False)
    max_val = missing.max()
    ax.set_xlim(0, max_val * 1.15)

    for bar, pct in zip(bars, missing.values):
        width = bar.get_width()
        y = bar.get_y() + bar.get_height() / 2
        if width > max_val * 0.15:
            ax.text(width - max_val * 0.02, y, f"{pct:.1f}%", va="center", ha="right",
                     color=TEXT_ON_ACCENT, fontweight="bold")
        else:
            ax.text(width + max_val * 0.02, y, f"{pct:.1f}%", va="center", ha="left",
                     color=TEXT_LIGHT, fontweight="bold")

    ax.set_xlabel("% missing")
    ax.set_title(f"{len(missing)} of {df.shape[1]} columns have missing values")
    fig.tight_layout()
    return fig


def plot_dist(df, column):
    """Histogram of one numeric column, with the median marked in place."""
    apply_style()
    values = df[column].dropna()
    median = values.median()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(values, bins=20, color=ACCENT, edgecolor=BACKGROUND, linewidth=0.8)
    ax.grid(axis="y", visible=True)
    ax.grid(axis="x", visible=False)
    ax.axvline(median, color=TEXT_LIGHT, linewidth=1.5, linestyle="--", alpha=0.8)
    ax.annotate(f"median = {median:g}", xy=(median, ax.get_ylim()[1]),
                xytext=(6, -6), textcoords="offset points",
                va="top", color=TEXT_LIGHT, fontweight="bold")
    ax.set_xlabel(column)
    ax.set_ylabel("count")
    ax.set_title(f"Distribution of {column}")
    fig.tight_layout()
    return fig
