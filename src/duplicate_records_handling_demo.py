"""
Pandas Data Cleaning Milestone - Identifying and Removing Duplicate Records

This module demonstrates:
1. Understanding duplicate records
2. Detecting duplicate rows
3. Removing duplicates intentionally
4. Verifying deduplication results

Author: Trivin Insight Engine
Date: March 10, 2026
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "employee_survey_2026_Q1.csv"

KEY_COLUMNS = ["employee_id", "survey_date"]


def section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def load_base_dataframe(csv_path):
    """Load the baseline dataset from CSV."""
    section_header("1. Loading Base DataFrame")

    print(f"Reading: {csv_path}")

    if not csv_path.exists():
        print("CSV file not found. Check path and try again.")
        return None

    df = pd.read_csv(csv_path)
    print(f"Loaded shape: {df.shape}")
    print(f"Initial full-row duplicates: {df.duplicated().sum()}")
    print(
        "Initial duplicates by key "
        f"{KEY_COLUMNS}: {df.duplicated(subset=KEY_COLUMNS).sum()}"
    )
    return df


def create_demo_dataframe_with_duplicates(df):
    """Create a teaching dataset containing exact and partial duplicates."""
    section_header("2. Building a DataFrame That Contains Duplicates")

    exact_duplicates = df.iloc[[1, 7]].copy()

    partial_duplicate = df.iloc[[3]].copy()
    partial_duplicate.loc[:, "response_text"] = (
        partial_duplicate["response_text"]
        .astype(str)
        .str.replace("workload", "heavy workload", regex=False)
    )

    demo_df = pd.concat([df, exact_duplicates, partial_duplicate], ignore_index=True)

    print("Added rows:")
    print("  - 2 exact duplicate rows (all columns match existing rows)")
    print("  - 1 partial duplicate row (same key, changed response_text)")
    print(f"Original shape: {df.shape}")
    print(f"Demo shape: {demo_df.shape}")

    return demo_df


def detect_duplicates(df):
    """Detect full-row and key-based duplicates and inspect examples."""
    section_header("3. Detecting Duplicate Rows")

    full_duplicate_mask = df.duplicated(keep=False)
    full_duplicate_count = df.duplicated().sum()

    key_duplicate_mask = df.duplicated(subset=KEY_COLUMNS, keep=False)
    key_duplicate_count = df.duplicated(subset=KEY_COLUMNS).sum()

    print("Duplicate indicators:")
    print("  - duplicated() checks full row matches")
    print(f"  - duplicated(subset={KEY_COLUMNS}) checks key-level matches")

    print(f"\nFull-row duplicate count: {full_duplicate_count}")
    print(f"Key-based duplicate count: {key_duplicate_count}")

    if full_duplicate_mask.any():
        print("\nRows involved in full-row duplicates:")
        print(df.loc[full_duplicate_mask].sort_values(KEY_COLUMNS))

    if key_duplicate_mask.any():
        print(f"\nRows involved in key-based duplicates ({KEY_COLUMNS}):")
        print(df.loc[key_duplicate_mask].sort_values(KEY_COLUMNS))


def remove_duplicates_intentionally(df):
    """Remove duplicates using explicit and explainable decisions."""
    section_header("4. Removing Duplicate Records Intentionally")

    print("Step A: Remove only exact full-row duplicates (keep first)")
    no_full_duplicates = df.drop_duplicates(keep="first")
    print(f"  Shape after full-row dedup: {no_full_duplicates.shape}")

    print(
        "\nStep B: Remove key-based duplicates using "
        f"{KEY_COLUMNS} (keep last)"
    )
    print(
        "  Rationale: keep='last' preserves the most recent version when "
        "same employee/date appears multiple times."
    )
    no_key_duplicates = no_full_duplicates.drop_duplicates(
        subset=KEY_COLUMNS,
        keep="last",
    )
    print(f"  Shape after key-based dedup: {no_key_duplicates.shape}")

    return no_full_duplicates, no_key_duplicates


def verify_results(original_df, final_df):
    """Verify deduplication quality and summarize what changed."""
    section_header("5. Verifying Deduplication Results")

    print("Shape comparison:")
    print(f"  Before deduplication: {original_df.shape}")
    print(f"  After deduplication:  {final_df.shape}")

    remaining_full_dups = final_df.duplicated().sum()
    remaining_key_dups = final_df.duplicated(subset=KEY_COLUMNS).sum()

    print("\nRemaining duplicates check:")
    print(f"  Full-row duplicates remaining: {remaining_full_dups}")
    print(f"  Key-based duplicates remaining: {remaining_key_dups}")

    print("\nIntegrity checks:")
    print(
        "  Unique key count before (demo data): "
        f"{original_df[KEY_COLUMNS].drop_duplicates().shape[0]}"
    )
    print(
        "  Unique key count after cleanup: "
        f"{final_df[KEY_COLUMNS].drop_duplicates().shape[0]}"
    )

    if remaining_full_dups == 0 and remaining_key_dups == 0:
        print("\nVerification result: deduplication completed successfully.")
    else:
        print("\nVerification result: duplicates still remain; review rules.")



def main():
    """Run duplicate-record detection and removal milestone demonstration."""
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*  PANDAS DATA CLEANING: DUPLICATE RECORD HANDLING             *")
    print("*  Detect, Remove, and Verify Duplicates Safely                *")
    print("*" + " " * 68 + "*")
    print("*" * 70)

    base_df = load_base_dataframe(RAW_CSV_PATH)
    if base_df is None:
        print("\nStopping because dataset could not be loaded.")
        return

    demo_df = create_demo_dataframe_with_duplicates(base_df)

    section_header("Understanding Duplicate Types")
    print("Exact duplicates: every column value matches another row.")
    print("Partial duplicates: only selected columns (business keys) match.")
    print("Duplicates can come from merge errors, repeated imports, or re-entries.")

    detect_duplicates(demo_df)

    dedup_full_df, dedup_final_df = remove_duplicates_intentionally(demo_df)

    print("\nPreview after exact full-row deduplication:")
    print(dedup_full_df.tail(5))

    print("\nPreview after full + key-based deduplication:")
    print(dedup_final_df.tail(5))

    verify_results(demo_df, dedup_final_df)

    section_header("Summary and Key Takeaways")
    print(
        """
    - Inspect duplicates before dropping anything.
    - Use duplicated() to detect repeated rows.
    - Use subset=... for business-key duplicate checks.
    - Choose keep='first' or keep='last' based on clear reasoning.
    - Verify shape and remaining duplicates after cleanup.

    Clean, deduplicated data supports trustworthy analysis.
    """
    )

    print("\n" + "=" * 70)
    print("  Demonstration Complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
