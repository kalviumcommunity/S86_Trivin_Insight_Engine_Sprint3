"""
Identifying Trends Over Time Using Line Plots
=============================================

This script demonstrates how to analyze time-based survey data with line plots.
It focuses on correct date ordering, trend interpretation, rolling averages,
and anomaly spotting without doing any forecasting.

Author: Trivin Insight Engine
Date: March 12, 2026
"""

from pathlib import Path

import matplotlib.dates as mdates
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
    """Configure matplotlib defaults for readable line plots."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams["figure.figsize"] = (11, 6)
    plt.rcParams["font.size"] = 11
    plt.rcParams["axes.titleweight"] = "bold"
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_dataset(csv_path):
    """Load the survey dataset and parse the time column."""
    section_header("1. Loading the Time-Based Dataset")

    print(f"Reading: {csv_path}")

    if not csv_path.exists():
        print("CSV file not found. Check the project path and try again.")
        return None

    df = pd.read_csv(csv_path, parse_dates=["survey_date"])
    df = df.sort_values("survey_date").reset_index(drop=True)

    print(f"Loaded shape: {df.shape}")
    print("Columns:")
    print(df.columns.tolist())
    print("\nFirst 5 rows after date sorting:")
    print(df[["survey_date", "department", "satisfaction_score"]].head())
    return df


def inspect_time_structure(df):
    """Show why ordering and interval checks matter for time data."""
    section_header("2. Inspecting the Time Structure")

    min_date = df["survey_date"].min().date()
    max_date = df["survey_date"].max().date()
    unique_dates = df["survey_date"].nunique()

    intervals = df["survey_date"].drop_duplicates().sort_values().diff().dropna().dt.days

    print(f"Time range: {min_date} to {max_date}")
    print(f"Unique observation dates: {unique_dates}")
    print("\nDays between observations:")
    print(intervals.value_counts().sort_index())

    if intervals.nunique() == 1:
        print("\nInterpretation: The intervals are regular.")
    else:
        print(
            "\nInterpretation: The series is mostly daily, but it contains at least "
            "one gap. That means you should still sort carefully before plotting."
        )


def build_daily_metric(df, metric):
    """Create a daily average time series for the chosen metric."""
    daily = df.groupby("survey_date", as_index=False)[metric].mean()
    daily["rolling_5_day_avg"] = daily[metric].rolling(window=5, min_periods=1).mean()
    daily["daily_change"] = daily[metric].diff()
    return daily


def build_weekly_metric(df, metric):
    """Create a weekly average series for a smoother high-level trend."""
    weekly = (
        df.set_index("survey_date")
        .resample("W")[metric]
        .mean()
        .reset_index()
        .rename(columns={metric: "weekly_average"})
    )
    return weekly


def format_date_axis(ax):
    """Apply readable date labels to the x-axis."""
    locator = mdates.AutoDateLocator(minticks=5, maxticks=8)
    formatter = mdates.DateFormatter("%b %d")
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")


def create_daily_line_plot(daily, metric):
    """Plot the raw daily time series."""
    section_header("3. Creating a Basic Line Plot")

    fig, ax = plt.subplots()
    ax.plot(
        daily["survey_date"],
        daily[metric],
        color="steelblue",
        linewidth=2,
        marker="o",
        markersize=5,
    )
    ax.set_title("Daily Satisfaction Trend")
    ax.set_xlabel("Survey Date")
    ax.set_ylabel("Average Satisfaction Score")
    ax.set_ylim(0, 10.5)
    format_date_axis(ax)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "line_plot_daily_satisfaction.png", dpi=300, bbox_inches="tight")
    plt.show()

    print("Saved: outputs/figures/line_plot_daily_satisfaction.png")
    print("Notice how the connected points reveal rises, drops, and short-term noise.")


def create_rolling_average_plot(daily, metric):
    """Compare raw values with a rolling average to separate trend from noise."""
    section_header("4. Distinguishing Trend from Noise")

    fig, ax = plt.subplots()
    ax.plot(
        daily["survey_date"],
        daily[metric],
        color="lightgray",
        linewidth=1.8,
        marker="o",
        markersize=4,
        label="Daily score",
    )
    ax.plot(
        daily["survey_date"],
        daily["rolling_5_day_avg"],
        color="darkgreen",
        linewidth=2.5,
        label="5-day rolling average",
    )
    ax.set_title("Daily Scores vs. 5-Day Rolling Average")
    ax.set_xlabel("Survey Date")
    ax.set_ylabel("Satisfaction Score")
    ax.set_ylim(0, 10.5)
    format_date_axis(ax)
    ax.legend()
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "line_plot_rolling_average_satisfaction.png", dpi=300, bbox_inches="tight")
    plt.show()

    print("Saved: outputs/figures/line_plot_rolling_average_satisfaction.png")
    print("The rolling line smooths short-term fluctuations so the underlying pattern is easier to read.")


def create_weekly_line_plot(weekly):
    """Plot a weekly summary to show higher-level movement."""
    section_header("5. Looking at the Higher-Level Weekly Trend")

    fig, ax = plt.subplots()
    ax.plot(
        weekly["survey_date"],
        weekly["weekly_average"],
        color="darkorange",
        linewidth=2.5,
        marker="o",
        markersize=7,
    )
    ax.set_title("Weekly Average Satisfaction Trend")
    ax.set_xlabel("Week Ending")
    ax.set_ylabel("Average Satisfaction Score")
    ax.set_ylim(0, 10.5)
    format_date_axis(ax)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "line_plot_weekly_satisfaction.png", dpi=300, bbox_inches="tight")
    plt.show()

    print("Saved: outputs/figures/line_plot_weekly_satisfaction.png")
    print("Weekly aggregation reduces noise and makes the broader direction easier to discuss.")


def create_department_comparison_plot(df, metric, departments=None):
    """Compare a small number of departments over time without cluttering the plot."""
    section_header("6. Comparing a Few Lines Without Clutter")

    if departments is None:
        departments = ["Engineering", "Marketing", "Sales"]

    filtered = df[df["department"].isin(departments)].copy()
    filtered = filtered.sort_values(["department", "survey_date"])

    fig, ax = plt.subplots(figsize=(12, 6))
    for department in departments:
        department_slice = filtered[filtered["department"] == department]
        ax.plot(
            department_slice["survey_date"],
            department_slice[metric],
            linewidth=2,
            marker="o",
            markersize=5,
            label=department,
        )

    ax.set_title("Selected Department Trends Over Time")
    ax.set_xlabel("Survey Date")
    ax.set_ylabel("Satisfaction Score")
    ax.set_ylim(0, 10.5)
    format_date_axis(ax)
    ax.legend(title="Department")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "line_plot_department_comparison.png", dpi=300, bbox_inches="tight")
    plt.show()

    print("Saved: outputs/figures/line_plot_department_comparison.png")
    print("Only three departments are shown to keep the plot readable.")


def print_trend_findings(daily, weekly):
    """Print concrete interpretation points from the plotted time series."""
    section_header("7. Interpreting Trends and Anomalies")

    min_row = daily.loc[daily["satisfaction_score"].idxmin()]
    max_row = daily.loc[daily["satisfaction_score"].idxmax()]
    largest_drop = daily.loc[daily["daily_change"].idxmin()]
    largest_rise = daily.loc[daily["daily_change"].idxmax()]

    first_half_mean = daily.iloc[: len(daily) // 2]["satisfaction_score"].mean()
    second_half_mean = daily.iloc[len(daily) // 2 :]["satisfaction_score"].mean()

    direction = "slightly downward" if second_half_mean < first_half_mean else "slightly upward"

    print(
        f"1. The overall pattern is {direction}: the first half averages {first_half_mean:.2f} "
        f"and the second half averages {second_half_mean:.2f}."
    )
    print(
        f"2. The lowest point occurs on {min_row['survey_date'].date()} with a score of "
        f"{min_row['satisfaction_score']:.1f}."
    )
    print(
        f"3. The highest point occurs on {max_row['survey_date'].date()} with a score of "
        f"{max_row['satisfaction_score']:.1f}."
    )
    print(
        f"4. The sharpest one-day drop happens on {largest_drop['survey_date'].date()} "
        f"({largest_drop['daily_change']:.1f} points)."
    )
    print(
        f"5. The sharpest one-day rise happens on {largest_rise['survey_date'].date()} "
        f"({largest_rise['daily_change']:+.1f} points)."
    )
    print(
        f"6. Weekly averages move from {weekly['weekly_average'].iloc[0]:.2f} in the first week "
        f"to {weekly['weekly_average'].iloc[-1]:.2f} in the final week shown."
    )
    print(
        "\nThese are visual EDA findings. They describe patterns in the observed period, "
        "but they do not explain causes or predict future outcomes."
    )


def main():
    """Run the line plot trends milestone demonstration."""
    print("\n" + "*" * 70)
    print("*  IDENTIFYING TRENDS OVER TIME USING LINE PLOTS                *")
    print("*  Explore Time-Based Survey Patterns with Sorted Date Data     *")
    print("*" * 70)

    configure_plotting()
    df = load_dataset(RAW_CSV_PATH)
    if df is None:
        print("\nStopping because the dataset could not be loaded.")
        return

    inspect_time_structure(df)
    daily = build_daily_metric(df, "satisfaction_score")
    weekly = build_weekly_metric(df, "satisfaction_score")

    create_daily_line_plot(daily, "satisfaction_score")
    create_rolling_average_plot(daily, "satisfaction_score")
    create_weekly_line_plot(weekly)
    create_department_comparison_plot(df, "satisfaction_score")
    print_trend_findings(daily, weekly)

    section_header("8. Key Takeaways")
    print(
        """
  - Always sort by the time column before plotting.
  - Line plots work best when order matters across time.
  - Rolling averages help separate trend from short-term noise.
  - Sudden spikes and drops should raise questions, not assumptions.
  - Limit the number of lines so the chart stays readable.
        """
    )


if __name__ == "__main__":
    main()
