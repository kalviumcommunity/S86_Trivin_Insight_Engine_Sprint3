"""
Pandas Fundamentals - CSV Loading into DataFrames
Loading CSV Data into Pandas DataFrames

This module demonstrates:
1. Understanding CSV files in context
2. Loading CSV files into Pandas DataFrames
3. Inspecting loaded data for correctness
4. Recognizing common CSV loading issues

Author: Trivin Insight Engine
Date: March 6, 2026
"""

from pathlib import Path
from io import StringIO

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "employee_survey_2026_Q1.csv"

EXPECTED_COLUMNS = [
    "employee_id",
    "department",
    "survey_date",
    "satisfaction_score",
    "work_life_balance",
    "management_support",
    "career_growth",
    "team_collaboration",
    "response_text",
]


def section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def explain_csv_structure():
    """Explain what CSV files represent before loading."""
    section_header("1. Understanding CSV Files")

    print("CSV stands for Comma-Separated Values.")
    print("A CSV file stores tabular data as plain text:")
    print("  - One line per row")
    print("  - Commas separate columns")
    print("  - First row usually contains headers")

    print("\nCSV and spreadsheet relationship:")
    print("  - CSV row    -> spreadsheet row")
    print("  - CSV column -> spreadsheet column")

    print("\nDelimiter concept:")
    print("  - Common delimiter is ','")
    print("  - Some files use ';' or tabs")
    print("  - Wrong delimiter can shift data into wrong columns")


def load_csv_to_dataframe(csv_path):
    """Load CSV to DataFrame using standard Pandas behavior."""
    section_header("2. Loading CSV Files into Pandas")

    print(f"Attempting to load file:\n  {csv_path}")

    if not csv_path.exists():
        print("\nError: CSV file path does not exist.")
        print("Check the path before continuing.")
        return None

    df = pd.read_csv(csv_path)

    print("\nCSV loaded successfully.")
    print(f"DataFrame type: {type(df)}")
    print(f"Rows loaded: {len(df)}")
    print(f"Columns loaded: {len(df.columns)}")

    return df


def inspect_loaded_dataframe(df):
    """Inspect first rows, columns, shape, and basic structure."""
    section_header("3. Inspecting Loaded Data")

    print("First 5 rows:")
    print(df.head())

    print("\nColumn names:")
    print(list(df.columns))

    print("\nStructure summary:")
    print(f"Shape (rows, columns): {df.shape}")
    print(f"Total rows: {df.shape[0]}")
    print(f"Total columns: {df.shape[1]}")

    print("\nData types:")
    print(df.dtypes)


def verify_expected_structure(df):
    """Validate that loaded data has expected columns and row count."""
    section_header("Structure Verification")

    actual_columns = list(df.columns)

    missing_columns = [col for col in EXPECTED_COLUMNS if col not in actual_columns]
    extra_columns = [col for col in actual_columns if col not in EXPECTED_COLUMNS]

    print(f"Expected column count: {len(EXPECTED_COLUMNS)}")
    print(f"Actual column count: {len(actual_columns)}")

    if missing_columns:
        print(f"Missing columns: {missing_columns}")
    else:
        print("Missing columns: None")

    if extra_columns:
        print(f"Unexpected columns: {extra_columns}")
    else:
        print("Unexpected columns: None")

    print(f"Row count loaded: {len(df)}")

    if not missing_columns and not extra_columns:
        print("\nResult: Column structure matches expectation.")
    else:
        print("\nResult: Column structure mismatch detected. Inspect load settings.")


def demonstrate_common_loading_issues():
    """Show common mistakes that cause incorrect DataFrame structure."""
    section_header("4. Recognizing Common Loading Issues")

    sample_csv = (
        "employee_id,department,satisfaction_score\n"
        "1001,Engineering,7\n"
        "1002,Marketing,9\n"
    )

    print("Issue A: Wrong delimiter used during loading")
    wrong_delimiter_df = pd.read_csv(StringIO(sample_csv), sep=";")
    print(f"  Shape when using sep=';': {wrong_delimiter_df.shape}")
    print(f"  Columns: {list(wrong_delimiter_df.columns)}")
    print("  Observation: Entire row can collapse into one column.")

    print("\nIssue B: Header row treated as data (header=None)")
    header_misread_df = pd.read_csv(StringIO(sample_csv), header=None)
    print(f"  Shape when using header=None: {header_misread_df.shape}")
    print(f"  Columns: {list(header_misread_df.columns)}")
    print("  First row now contains what should have been column names.")

    print("\nLesson:")
    print("  Always inspect head(), columns, and shape right after read_csv().")


def main():
    """Run all CSV loading milestone sections in sequence."""
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*  PANDAS FUNDAMENTALS: CSV LOADING INTO DATAFRAMES            *")
    print("*  Load, Inspect, and Validate CSV Data Safely                 *")
    print("*" + " " * 68 + "*")
    print("*" * 70)

    explain_csv_structure()

    dataframe = load_csv_to_dataframe(RAW_CSV_PATH)
    if dataframe is None:
        print("\nStopping execution because the CSV file could not be loaded.")
        return

    inspect_loaded_dataframe(dataframe)
    verify_expected_structure(dataframe)
    demonstrate_common_loading_issues()

    section_header("Summary and Key Takeaways")
    print(
        """
    ✓ CSV files represent rows and columns as plain text
    ✓ pd.read_csv() loads CSV data into DataFrames
    ✓ Always inspect head(), columns, and shape after loading
    ✓ Verify column names and row counts before further analysis
    ✓ Catch delimiter/header mistakes early to avoid downstream errors

    This milestone focuses on loading and inspection only.
    """
    )

    print("\n" + "=" * 70)
    print("  Demonstration Complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
