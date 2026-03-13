"""
Detecting Outliers Using Visual Inspection and Simple Rules
===========================================================

This script demonstrates outlier detection as an EDA task using:
- visual inspection (boxplot and scatter plot)
- simple rules (IQR and threshold checks)

No outlier removal is performed in this milestone.

Author: Trivin Insight Engine
Date: March 13, 2026
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "employee_survey_2026_Q1.csv"
FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"


def section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def configure_plotting():
    """Set plotting defaults for readable outlier visuals."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["font.size"] = 11
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_dataset(csv_path):
    """Load survey data from the raw CSV path."""
    section_header("1. Loading Dataset")

    print(f"Reading: {csv_path}")
    if not csv_path.exists():
        print("CSV file not found. Check your project path and try again.")
        return None

    df = pd.read_csv(csv_path, parse_dates=["survey_date"])
    print(f"Loaded shape: {df.shape}")
    print("Columns:")
    print(df.columns.tolist())

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    print("\nNumeric columns available:")
    print(numeric_columns)
    return df


def create_boxplot_visual(df, column):
    """Create a boxplot to visually inspect outliers beyond whiskers."""
    section_header(f"2. Boxplot Visual Inspection: {column}")

    fig, ax = plt.subplots()
    ax.boxplot(
        df[column].dropna(),
        vert=True,
        patch_artist=True,
        boxprops={"facecolor": "lightsteelblue", "edgecolor": "navy"},
        medianprops={"color": "darkred", "linewidth": 2},
        whiskerprops={"color": "navy"},
        capprops={"color": "navy"},
        flierprops={"marker": "o", "markerfacecolor": "crimson", "markersize": 8, "alpha": 0.8},
    )
    ax.set_title(f"Boxplot: {column.replace('_', ' ').title()}")
    ax.set_ylabel(column.replace("_", " ").title())
    ax.set_xticklabels([column])
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"outlier_boxplot_{column}.png", dpi=300, bbox_inches="tight")
    plt.show()

    print(f"Saved: outputs/figures/outlier_boxplot_{column}.png")
    print("Points beyond whiskers are potential outliers and should be investigated.")


def create_scatter_visual(df, x_col, y_col):
    """Create a scatter plot to identify isolated points visually."""
    section_header(f"3. Scatter Visual Inspection: {x_col} vs {y_col}")

    fig, ax = plt.subplots()
    ax.scatter(
        df[x_col],
        df[y_col],
        s=70,
        alpha=0.8,
        color="steelblue",
        edgecolor="black",
        linewidth=0.4,
    )
    ax.set_xlabel(x_col.replace("_", " ").title())
    ax.set_ylabel(y_col.replace("_", " ").title())
    ax.set_title("Scatter Plot for Outlier Inspection")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"outlier_scatter_{x_col}_vs_{y_col}.png", dpi=300, bbox_inches="tight")
    plt.show()

    print(f"Saved: outputs/figures/outlier_scatter_{x_col}_vs_{y_col}.png")
    print("Look for points isolated far from the main cloud.")


def iqr_outlier_flags(df, column):
    """Return IQR-based outlier flags and bounds for one column."""
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    mask = (df[column] < lower_bound) | (df[column] > upper_bound)
    flagged = df.loc[mask, ["employee_id", "department", column]].copy()
    return flagged, lower_bound, upper_bound


def threshold_outlier_flags(df, column, low_threshold, high_threshold):
    """Return threshold-based outlier flags for one column."""
    mask = (df[column] < low_threshold) | (df[column] > high_threshold)
    flagged = df.loc[mask, ["employee_id", "department", column]].copy()
    return flagged


def compare_flagging_methods(df, column):
    """Compare IQR and threshold flags side-by-side."""
    section_header(f"4. Rule-Based Outlier Flags: {column}")

    iqr_flagged, lower_bound, upper_bound = iqr_outlier_flags(df, column)
    print("IQR method")
    print(f"Lower bound: {lower_bound:.2f}")
    print(f"Upper bound: {upper_bound:.2f}")
    print(f"Flagged count: {len(iqr_flagged)}")

    if not iqr_flagged.empty:
        print(iqr_flagged.to_string(index=False))

    # Simple practical threshold for 1-10 scaled survey metrics.
    threshold_flagged = threshold_outlier_flags(df, column, low_threshold=3, high_threshold=9)
    print("\nThreshold method (rule: < 3 or > 9)")
    print(f"Flagged count: {len(threshold_flagged)}")

    if not threshold_flagged.empty:
        print(threshold_flagged.to_string(index=False))

    iqr_ids = set(iqr_flagged["employee_id"].tolist())
    threshold_ids = set(threshold_flagged["employee_id"].tolist())
    overlap_ids = sorted(iqr_ids.intersection(threshold_ids))

    print("\nMethod comparison")
    print(f"IQR only: {len(iqr_ids - threshold_ids)}")
    print(f"Threshold only: {len(threshold_ids - iqr_ids)}")
    print(f"Overlap: {len(overlap_ids)}")
    if overlap_ids:
        print(f"Overlap employee IDs: {overlap_ids}")


def print_interpretation_guidance():
    """Print interpretation principles for thoughtful outlier handling."""
    section_header("5. Interpreting Outliers Carefully")

    print(
        """
Use this decision mindset:

1. Flag first, do not remove immediately.
2. Ask if flagged points are plausible real observations.
3. Check for data-entry or measurement problems.
4. Consider domain context before deciding next action.
5. Document why points were kept, reviewed, or treated later.

Important:
- Outlier rules are indicators, not verdicts.
- Outliers can be valid and informative.
- Detection comes before treatment.
        """
    )


def main():
    """Run the outlier detection milestone demo."""
    print("\n" + "*" * 70)
    print("*  DETECTING OUTLIERS: VISUAL INSPECTION + SIMPLE RULES         *")
    print("*  EDA Detection Milestone (No Outlier Removal)                 *")
    print("*" * 70)

    configure_plotting()
    df = load_dataset(RAW_CSV_PATH)
    if df is None:
        print("\nStopping because the dataset could not be loaded.")
        return

    create_boxplot_visual(df, "satisfaction_score")
    create_scatter_visual(df, "work_life_balance", "satisfaction_score")
    compare_flagging_methods(df, "satisfaction_score")
    print_interpretation_guidance()


if __name__ == "__main__":
    main()
