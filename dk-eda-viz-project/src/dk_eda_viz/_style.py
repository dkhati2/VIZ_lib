"""Central matplotlib styling for the package.

``apply_style()`` is called once at the top of every plotting function in
``plotting.py`` so that all charts share one consistent look — a light grid
drawn beneath the data, no top/right spines, a bold left-aligned title, and a
muted palette with a single accent color for the subject of the plot.

The style follows a few visualization principles: maximize the data-ink ratio,
avoid chart junk, and prefer direct labeling over legends where it works.

Matplotlib is the only plotting dependency (no seaborn, no plotly).
"""

import matplotlib.pyplot as plt

# Color constants
ACCENT = "#2E5EAA"      # primary color for the subject of a plot
NEUTRAL = "#B0B0B0"     # gray for comparison / context
BACKGROUND = "#FFFFFF"  # figure and axes background
TEXT_DARK = "#2B2B2B"   # text, labels, and ticks


def apply_style():
    """Update ``plt.rcParams`` with the package's shared visual style.

    Call this once at the start of a plotting function, before creating the
    figure, so every chart in the package looks the same.
    """
    plt.rcParams.update({
        # Spines: keep only left and bottom (maximize data-ink ratio)
        "axes.spines.top": False,
        "axes.spines.right": False,

        # Grid: light gray, thin, drawn below the data
        "axes.grid": True,
        "grid.color": "#EAEAEA",
        "grid.linewidth": 0.6,
        "axes.axisbelow": True,

        # Title: left-aligned, bold, size 14
        "axes.titlelocation": "left",
        "axes.titleweight": "bold",
        "axes.titlesize": 14,

        # Typography: sans-serif, base size 11, labels size 10
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.labelsize": 10,

        # Colors: dark text/labels/ticks
        "text.color": TEXT_DARK,
        "axes.labelcolor": TEXT_DARK,
        "axes.edgecolor": TEXT_DARK,
        "xtick.color": TEXT_DARK,
        "ytick.color": TEXT_DARK,

        # Backgrounds
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": BACKGROUND,

        # Resolution
        "figure.dpi": 100,
    })
