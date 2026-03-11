"""
Comparing Distributions Across Multiple Columns
================================================

This script demonstrates how to compare distributions across multiple
numeric columns in a Pandas DataFrame using summary statistics only.

Author: Trivin Insight Engine
Date: March 11, 2026
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "employee_survey_2026_Q1.csv"


def section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def load_dataset(csv_path):
    """Load the employee survey dataset."""
    section_header("1. Loading the Dataset")

    print(f"Reading: {csv_path}")

    if not csv_path.exists():
        print("CSV file not found. Check the project path and try again.")
        return None

    df = pd.read_csv(csv_path)
    print(f"Loaded shape: {df.shape}")
    print("Columns:")
    print(df.columns.tolist())
    return df


def select_numeric_metric_columns(df):
    """Select numeric survey metric columns and exclude identifier fields."""
    section_header("2. Selecting Numeric Columns for Comparison")

    numeric_columns = [
        column
        for column in df.select_dtypes(include="number").columns
        if column != "employee_id"
    ]

    print("Numeric columns selected:")
    for column in numeric_columns:
        print(f"  - {column}")

    return numeric_columns


def summarize_multiple_columns(df, numeric_columns):
    """Compute summary statistics across all selected columns."""
    section_header("3. Summary Statistics Across Multiple Columns")

    summary = df[numeric_columns].describe().T.round(2)
    print(summary)
    return summary


def build_comparison_table(df, numeric_columns):
    """Create a single table for comparing central tendency and spread."""
    section_header("4. Building a Comparison Table")

    comparison_table = pd.DataFrame(
        {
            "mean": df[numeric_columns].mean(),
            "median": df[numeric_columns].median(),
            "min": df[numeric_columns].min(),
            "max": df[numeric_columns].max(),
            "range": df[numeric_columns].max() - df[numeric_columns].min(),
            "std_dev": df[numeric_columns].std(),
        }
    ).round(2)

    comparison_table["mean_minus_median"] = (
        comparison_table["mean"] - comparison_table["median"]
    ).round(2)

    comparison_table["possible_skew"] = comparison_table["mean_minus_median"].apply(
        lambda value: "possible right skew"
        if value > 0.25
        else "possible left skew"
        if value < -0.25
        else "roughly balanced"
    )

    print(comparison_table)
    return comparison_table


def compare_central_tendency(comparison_table):
    """Highlight mean and median comparisons across columns."""
    section_header("5. Comparing Means and Medians")

    central_tendency = comparison_table[["mean", "median"]].sort_values(
        "mean", ascending=False
    )
    print(central_tendency)

    highest_mean = central_tendency["mean"].idxmax()
    lowest_mean = central_tendency["mean"].idxmin()

    print(f"\nHighest average score: {highest_mean}")
    print(f"Lowest average score:  {lowest_mean}")


def compare_spread(comparison_table):
    """Highlight range and standard deviation comparisons across columns."""
    section_header("6. Comparing Spread and Variability")

    spread = comparison_table[["min", "max", "range", "std_dev"]].sort_values(
        ["std_dev", "range"], ascending=False
    )
    print(spread)

    highest_std = spread["std_dev"].idxmax()
    lowest_std = spread["std_dev"].idxmin()

    print(f"\nMost variable column: {highest_std}")
    print(f"Most stable column:   {lowest_std}")


def print_findings(comparison_table):
    """Print comparison-based EDA findings from the summary table."""
    section_header("7. Comparison-Based EDA Findings")

    highest_mean = comparison_table["mean"].idxmax()
    lowest_mean = comparison_table["mean"].idxmin()
    highest_std = comparison_table["std_dev"].idxmax()
    lowest_std = comparison_table["std_dev"].idxmin()
    most_positive_skew_signal = comparison_table["mean_minus_median"].idxmax()
    most_negative_skew_signal = comparison_table["mean_minus_median"].idxmin()

    print(
        f"1. {highest_mean} has the highest mean "
        f"({comparison_table.loc[highest_mean, 'mean']:.2f})."
    )
    print(
        f"2. {lowest_mean} has the lowest mean "
        f"({comparison_table.loc[lowest_mean, 'mean']:.2f})."
    )
    print(
        f"3. {highest_std} shows the widest spread by standard deviation "
        f"({comparison_table.loc[highest_std, 'std_dev']:.2f})."
    )
    print(
        f"4. {lowest_std} is the most stable column by standard deviation "
        f"({comparison_table.loc[lowest_std, 'std_dev']:.2f})."
    )
    print(
        f"5. {most_positive_skew_signal} has the strongest positive "
        f"mean-minus-median signal ({comparison_table.loc[most_positive_skew_signal, 'mean_minus_median']:.2f})."
    )
    print(
        f"6. {most_negative_skew_signal} has the strongest negative "
        f"mean-minus-median signal ({comparison_table.loc[most_negative_skew_signal, 'mean_minus_median']:.2f})."
    )

    print(
        "\nThese statistics help guide deeper EDA, but they should be treated "
        "as starting points rather than final conclusions."
    )


def main():
    """Run the multi-column distribution comparison demonstration."""
    print("\n" + "*" * 70)
    print("*  MULTI-COLUMN DISTRIBUTION COMPARISON IN PANDAS               *")
    print("*  Compare Central Tendency and Spread Across Survey Metrics    *")
    print("*" * 70)

    df = load_dataset(RAW_CSV_PATH)
    if df is None:
        print("\nStopping because the dataset could not be loaded.")
        return

    numeric_columns = select_numeric_metric_columns(df)
    summarize_multiple_columns(df, numeric_columns)
    comparison_table = build_comparison_table(df, numeric_columns)
    compare_central_tendency(comparison_table)
    compare_spread(comparison_table)
    print_findings(comparison_table)

    section_header("8. Key Takeaways")
    print(
        """
  - Compare columns using distributions, not raw values.
  - Mean and median help compare central tendency.
  - Range and standard deviation help compare spread.
  - Larger spread suggests more varied employee experiences.
  - Comparison tables make differences between variables easier to interpret.
        """
    )


if __name__ == "__main__":
    main()