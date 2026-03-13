"""
Exploring Relationships Between Variables Using Scatter Plots
==============================================================

This script demonstrates how to create and interpret scatter plots for
exploratory data analysis (EDA). It focuses on visual pattern reading,
including direction, strength, clusters, and outliers.

Author: Trivin Insight Engine
Date: March 13, 2026
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
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
    """Configure matplotlib defaults for clear scatter plots."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["font.size"] = 11
    plt.rcParams["axes.titleweight"] = "bold"
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_dataset(csv_path):
    """Load survey dataset from CSV."""
    section_header("1. Loading the Dataset")

    print(f"Reading: {csv_path}")
    if not csv_path.exists():
        print("CSV file not found. Check the project path and try again.")
        return None

    df = pd.read_csv(csv_path, parse_dates=["survey_date"])
    print(f"Loaded shape: {df.shape}")
    print("Columns:")
    print(df.columns.tolist())

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    print("\nNumeric columns available for scatter plots:")
    print(numeric_cols)
    return df


def relationship_direction_label(x, y):
    """Return a simple direction label using covariance sign."""
    covariance = np.cov(x, y, ddof=0)[0, 1]
    if covariance > 0:
        return "positive"
    if covariance < 0:
        return "negative"
    return "no clear"


def relationship_strength_label(x, y):
    """Return a rough strength label without statistical testing."""
    q1 = pd.Series(x).quantile(0.25)
    q3 = pd.Series(x).quantile(0.75)

    low_x_avg = y[x <= q1].mean()
    high_x_avg = y[x >= q3].mean()
    gap = abs(high_x_avg - low_x_avg)

    if gap >= 2:
        return "strong visual relationship"
    if gap >= 1:
        return "moderate visual relationship"
    return "weak or unclear visual relationship"


def create_basic_scatter(df, x_col, y_col, output_name, title):
    """Create and save a basic scatter plot for two numeric columns."""
    section_header(f"2. Scatter Plot: {x_col} vs {y_col}")

    fig, ax = plt.subplots()
    ax.scatter(
        df[x_col],
        df[y_col],
        color="steelblue",
        alpha=0.8,
        s=65,
        edgecolor="black",
        linewidth=0.5,
    )
    ax.set_xlabel(x_col.replace("_", " ").title())
    ax.set_ylabel(y_col.replace("_", " ").title())
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / output_name, dpi=300, bbox_inches="tight")
    plt.show()

    direction = relationship_direction_label(df[x_col].to_numpy(), df[y_col].to_numpy())
    strength = relationship_strength_label(df[x_col].to_numpy(), df[y_col].to_numpy())

    print(f"Saved: outputs/figures/{output_name}")
    print(f"Observed direction: {direction} relationship")
    print(f"Observed strength: {strength}")


def create_department_colored_scatter(df, x_col, y_col):
    """Create a scatter plot with colors by department to reveal clusters."""
    section_header("3. Looking for Clusters by Department")

    departments = sorted(df["department"].dropna().unique())
    cmap = plt.cm.get_cmap("tab10", len(departments))

    fig, ax = plt.subplots(figsize=(11, 6))
    for idx, department in enumerate(departments):
        subset = df[df["department"] == department]
        ax.scatter(
            subset[x_col],
            subset[y_col],
            s=70,
            alpha=0.8,
            color=cmap(idx),
            edgecolor="black",
            linewidth=0.4,
            label=department,
        )

    ax.set_xlabel(x_col.replace("_", " ").title())
    ax.set_ylabel(y_col.replace("_", " ").title())
    ax.set_title("Scatter Plot Colored by Department")
    ax.legend(title="Department", ncol=2, fontsize=9)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "scatter_department_clusters.png", dpi=300, bbox_inches="tight")
    plt.show()

    print("Saved: outputs/figures/scatter_department_clusters.png")
    print("Use color grouping to inspect whether departments occupy different regions.")


def detect_outliers_iqr(df, x_col, y_col):
    """Detect potential outliers using IQR limits for x and y dimensions."""
    x_q1, x_q3 = df[x_col].quantile(0.25), df[x_col].quantile(0.75)
    y_q1, y_q3 = df[y_col].quantile(0.25), df[y_col].quantile(0.75)

    x_iqr = x_q3 - x_q1
    y_iqr = y_q3 - y_q1

    x_low, x_high = x_q1 - 1.5 * x_iqr, x_q3 + 1.5 * x_iqr
    y_low, y_high = y_q1 - 1.5 * y_iqr, y_q3 + 1.5 * y_iqr

    outliers = df[
        (df[x_col] < x_low)
        | (df[x_col] > x_high)
        | (df[y_col] < y_low)
        | (df[y_col] > y_high)
    ]
    return outliers


def create_outlier_scatter(df, x_col, y_col):
    """Highlight possible outliers on a scatter plot."""
    section_header("4. Identifying Outliers")

    outliers = detect_outliers_iqr(df, x_col, y_col)
    non_outliers = df.drop(outliers.index)

    fig, ax = plt.subplots()
    ax.scatter(
        non_outliers[x_col],
        non_outliers[y_col],
        color="slategray",
        alpha=0.7,
        s=60,
        edgecolor="black",
        linewidth=0.4,
        label="Typical observations",
    )
    ax.scatter(
        outliers[x_col],
        outliers[y_col],
        color="crimson",
        alpha=0.95,
        s=95,
        edgecolor="black",
        linewidth=0.6,
        label="Potential outliers",
    )

    for _, row in outliers.iterrows():
        ax.annotate(
            str(row["employee_id"]),
            (row[x_col], row[y_col]),
            textcoords="offset points",
            xytext=(5, 5),
            fontsize=8,
        )

    ax.set_xlabel(x_col.replace("_", " ").title())
    ax.set_ylabel(y_col.replace("_", " ").title())
    ax.set_title("Scatter Plot with Potential Outliers Highlighted")
    ax.legend()
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "scatter_outlier_highlight.png", dpi=300, bbox_inches="tight")
    plt.show()

    print("Saved: outputs/figures/scatter_outlier_highlight.png")
    print(f"Potential outliers found: {len(outliers)}")
    if not outliers.empty:
        print("Outlier employee IDs:", outliers["employee_id"].tolist())


def print_interpretation_notes(df):
    """Print concise interpretation prompts for the learner."""
    section_header("5. Interpretation Notes")

    print(
        """
Use these prompts while reading each scatter plot:

1. Direction:
   - Do points move upward from left to right (positive)?
   - Do points move downward from left to right (negative)?
   - Or is there no clear direction?

2. Strength:
   - Are points tightly grouped around a visual path?
   - Or are they widely dispersed?

3. Pattern shape:
   - Does the pattern look roughly linear?
   - Does it curve or bend (non-linear)?

4. Clusters:
   - Are there groups of points concentrated in specific regions?
   - Do department colors reveal subgroup behavior?

5. Outliers:
   - Are some points isolated far from the rest?
   - Could they reflect data errors or meaningful extreme cases?

Remember: scatter plots reveal association patterns, not causation.
        """
    )

    numeric_cols = [
        "satisfaction_score",
        "work_life_balance",
        "management_support",
        "career_growth",
        "team_collaboration",
    ]
    print("Suggested additional variable pairs to explore:")
    for idx, x_col in enumerate(numeric_cols):
        for y_col in numeric_cols[idx + 1 :]:
            print(f"  - {x_col} vs {y_col}")


def main():
    """Run full scatter-plot relationship milestone demo."""
    print("\n" + "*" * 70)
    print("*  EXPLORING RELATIONSHIPS WITH SCATTER PLOTS                   *")
    print("*  Visualize Variable Interactions Before Modeling              *")
    print("*" * 70)

    configure_plotting()
    df = load_dataset(RAW_CSV_PATH)
    if df is None:
        print("\nStopping because the dataset could not be loaded.")
        return

    create_basic_scatter(
        df,
        x_col="work_life_balance",
        y_col="satisfaction_score",
        output_name="scatter_satisfaction_vs_work_life_balance.png",
        title="Satisfaction vs Work-Life Balance",
    )
    create_basic_scatter(
        df,
        x_col="management_support",
        y_col="satisfaction_score",
        output_name="scatter_satisfaction_vs_management_support.png",
        title="Satisfaction vs Management Support",
    )
    create_department_colored_scatter(
        df,
        x_col="career_growth",
        y_col="satisfaction_score",
    )
    create_outlier_scatter(
        df,
        x_col="work_life_balance",
        y_col="satisfaction_score",
    )
    print_interpretation_notes(df)


if __name__ == "__main__":
    main()
