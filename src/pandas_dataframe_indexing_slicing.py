"""
Pandas Fundamentals - Selecting Rows and Columns Using Indexing and Slicing

This module demonstrates:
1. Selecting columns by name
2. Selecting rows by position with iloc
3. Selecting rows by label with loc
4. Selecting rows and columns together
5. Avoiding common selection mistakes

Author: Trivin Insight Engine
Date: March 9, 2026
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "employee_survey_2026_Q1.csv"


def section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 72)
    print(f"  {title}")
    print("=" * 72)


def load_dataframe(csv_path):
    """Load the source CSV for selection demonstrations."""
    section_header("0. Load DataFrame")

    print(f"Loading file:\n  {csv_path}")

    if not csv_path.exists():
        print("\nError: File not found. Check the CSV path and try again.")
        return None

    df = pd.read_csv(csv_path)

    print("\nDataFrame loaded successfully.")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    return df


def select_columns_by_name(df):
    """Demonstrate single and multiple column selection by name."""
    section_header("1. Selecting Columns by Name")

    single_column = df["department"]
    print("Single column selection: df['department']")
    print(single_column.head())
    print(f"Result type: {type(single_column)}")

    multiple_columns = df[["department", "satisfaction_score", "survey_date"]]
    print("\nMultiple column selection: df[['department', 'satisfaction_score', 'survey_date']]")
    print(multiple_columns.head())
    print(f"Result type: {type(multiple_columns)}")

    print("\nSelection check:")
    print(f"Selected columns: {list(multiple_columns.columns)}")
    print(f"Selected shape: {multiple_columns.shape}")


def select_rows_by_position(df):
    """Demonstrate row selection using integer positions with iloc."""
    section_header("2. Selecting Rows by Position (iloc)")

    print("Single row by position: df.iloc[0]")
    print(df.iloc[0])

    print("\nRow slice by position: df.iloc[0:5]")
    first_five_rows = df.iloc[0:5]
    print(first_five_rows)

    print("\nSelected rows at positions [1, 3, 5] with df.iloc[[1, 3, 5]]")
    selected_rows = df.iloc[[1, 3, 5]]
    print(selected_rows)

    print("\nZero-based indexing reminder:")
    print("- First row position is 0")
    print(f"- Last valid row position is {len(df) - 1}")

    print("\nOut-of-range access demonstration (safe with try/except):")
    try:
        print(df.iloc[len(df)])
    except IndexError as error:
        print(f"IndexError caught: {error}")


def select_rows_by_label(df):
    """Demonstrate row selection using labels with loc."""
    section_header("3. Selecting Rows by Label (loc)")

    # Use employee_id as an explicit row label for this lesson.
    df_by_employee_id = df.set_index("employee_id").sort_index()

    print("DataFrame indexed by employee_id labels (preview):")
    print(df_by_employee_id.head())

    example_label = df_by_employee_id.index[0]
    print(f"\nSingle row by label: df_by_employee_id.loc[{example_label}]")
    print(df_by_employee_id.loc[example_label])

    start_label = df_by_employee_id.index[2]
    end_label = df_by_employee_id.index[6]
    print(f"\nLabel slice: df_by_employee_id.loc[{start_label}:{end_label}]")
    label_slice = df_by_employee_id.loc[start_label:end_label]
    print(label_slice)

    print("\nInclusive behavior reminder for .loc label slicing:")
    print("- Both start and end labels are included when present")


def select_rows_and_columns_together(df):
    """Demonstrate combined row+column selection using iloc and loc."""
    section_header("4. Selecting Rows and Columns Together")

    print("Position-based row+column selection with iloc:")
    print("df.iloc[0:4, [1, 3, 4]]")
    iloc_subset = df.iloc[0:4, [1, 3, 4]]
    print(iloc_subset)

    df_by_employee_id = df.set_index("employee_id").sort_index()
    label_start = df_by_employee_id.index[1]
    label_end = df_by_employee_id.index[4]

    print("\nLabel-based row+column selection with loc:")
    print(
        "df_by_employee_id.loc[label_start:label_end, "
        "['department', 'satisfaction_score', 'management_support']]"
    )
    loc_subset = df_by_employee_id.loc[
        label_start:label_end,
        ["department", "satisfaction_score", "management_support"],
    ]
    print(loc_subset)

    print("\nResult verification:")
    print(f"iloc subset shape: {iloc_subset.shape}")
    print(f"loc subset shape: {loc_subset.shape}")


def avoid_common_selection_mistakes(df):
    """Highlight common mistakes and safer alternatives."""
    section_header("5. Avoiding Common Selection Mistakes")

    print("Mistake 1: Chained indexing can be ambiguous.")
    print("Example to avoid: df[df['department'] == 'Sales']['satisfaction_score']")

    print("\nSafer, explicit alternative with .loc:")
    explicit_selection = df.loc[
        df["department"] == "Sales",
        ["department", "satisfaction_score"],
    ]
    print(explicit_selection.head())

    print("\nMistake 2: Editing a view unintentionally.")
    print("Use .copy() when you need an independent subset to modify later.")

    safe_subset = df.loc[:, ["department", "satisfaction_score"]].copy()
    print("safe_subset = df.loc[:, ['department', 'satisfaction_score']].copy()")
    print(f"safe_subset shape: {safe_subset.shape}")

    print("\nPractice note:")
    print("- Verify subset rows and columns after each selection")
    print("- Keep selectors explicit and readable")


def main():
    """Run all DataFrame selection demonstrations in order."""
    print("\n")
    print("*" * 72)
    print("*" + " " * 70 + "*")
    print("*  PANDAS FUNDAMENTALS: INDEXING AND SLICING DATAFRAMES           *")
    print("*  Selecting Rows and Columns Safely and Intentionally            *")
    print("*" + " " * 70 + "*")
    print("*" * 72)

    df = load_dataframe(RAW_CSV_PATH)
    if df is None:
        print("\nStopping execution because data could not be loaded.")
        return

    select_columns_by_name(df)
    select_rows_by_position(df)
    select_rows_by_label(df)
    select_rows_and_columns_together(df)
    avoid_common_selection_mistakes(df)

    section_header("Summary and Key Takeaways")
    print(
        """
    ✓ Select columns by name using [] with clear column labels
    ✓ Use .iloc for position-based row/column selection
    ✓ Use .loc for label-based row/column selection
    ✓ Remember: .loc label slicing is inclusive
    ✓ Combine row and column selectors in one expression
    ✓ Prefer explicit .loc and .copy() to avoid common pitfalls

    This milestone focuses on precise, readable data selection only.
    """
    )

    print("\n" + "=" * 72)
    print("  Demonstration Complete!")
    print("=" * 72 + "\n")


if __name__ == "__main__":
    main()
