import matplotlib.pyplot as plt

ACCENT = "#FAB387"          # warm peach — primary color for the subject of a plot
NEUTRAL = "#6C7086"         # muted slate — gray for comparison / context
BACKGROUND = "#1E1E2E"      # dark slate background
SURFACE = "#313244"         # slightly lighter than background — gridlines, spines
TEXT_LIGHT = "#CDD6F4"      # soft off-white — text, labels, ticks
TEXT_ON_ACCENT = "#1E1E2E"  # dark text for labels placed on top of the light accent color


def apply_style():
    """Update plt.rcParams with the package's dark, warm-accented visual style."""
    plt.rcParams.update({
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.spines.bottom": False,
        "axes.grid": False,
        "grid.color": SURFACE,
        "grid.linewidth": 0.6,
        "grid.alpha": 0.7,
        "axes.axisbelow": True,
        "axes.titlelocation": "left",
        "axes.titleweight": "bold",
        "axes.titlesize": 14,
        "axes.titlepad": 14,
        "axes.titlecolor": TEXT_LIGHT,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size": 11,
        "axes.labelsize": 10,
        "text.color": TEXT_LIGHT,
        "axes.labelcolor": TEXT_LIGHT,
        "xtick.color": TEXT_LIGHT,
        "ytick.color": TEXT_LIGHT,
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": BACKGROUND,
        "savefig.facecolor": BACKGROUND,
        "figure.dpi": 100,
    })
