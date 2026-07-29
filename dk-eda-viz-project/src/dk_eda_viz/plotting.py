"""Plotting functions for quick exploratory data analysis.

Every function applies the shared package style, uses only matplotlib and
pandas, and returns the matplotlib ``Figure`` (it never calls ``plt.show()``)
so the caller decides how to display or save it.
"""

import matplotlib.pyplot as plt
import pandas as pd

from ._style import apply_style, ACCENT, TEXT_DARK


def plot_missing(df):
    """Horizontal bar chart of percent missing per column, worst first.

    Only columns with missing values are shown, each bar labeled with its
    percentage. Returns None (after printing a note) if nothing is missing.
    """
    apply_style()
    missing = df.isna().mean() * 100
    missing = missing[missing > 0].sort_values(ascending=False)
    if missing.empty:
        print("No missing values found.")
        return None

    fig, ax = plt.subplots(figsize=(8, 0.5 * len(missing) + 1.5))
    ax.barh(missing.index, missing.values, color=ACCENT)
    ax.invert_yaxis()  # largest at the top
    for y, pct in enumerate(missing.values):
        ax.text(pct + 0.5, y, f"{pct:.1f}%", va="center", color=TEXT_DARK)
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
    ax.hist(values, bins=20, color=ACCENT)
    ax.axvline(median, color=TEXT_DARK, linewidth=1.5)
    ax.annotate(f"median = {median:g}", xy=(median, ax.get_ylim()[1]),
                xytext=(6, -6), textcoords="offset points",
                va="top", color=TEXT_DARK)
    ax.set_xlabel(column)
    ax.set_ylabel("count")
    ax.set_title(f"Distribution of {column}")
    fig.tight_layout()
    return fig


def plot_corr(df):
    """Correlation heatmap of numeric columns, annotated with each value."""
    apply_style()
    corr = df.select_dtypes(include="number").corr()
    labels = corr.columns

    fig, ax = plt.subplots(figsize=(1.1 * len(labels) + 2, 1.1 * len(labels) + 2))
    im = ax.imshow(corr.values, cmap="Blues", vmin=-1, vmax=1)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)
    ax.grid(False)
    for i in range(len(labels)):
        for j in range(len(labels)):
            value = corr.values[i, j]
            color = "white" if abs(value) > 0.5 else TEXT_DARK
            ax.text(j, i, f"{value:.2f}", ha="center", va="center", color=color)
    ax.set_title("Correlation between numeric columns")
    fig.tight_layout()
    return fig
