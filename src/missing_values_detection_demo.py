"""
Missing Value Detection - Video Demonstration Script
=====================================================

This script demonstrates the core concepts of detecting missing values
in Pandas DataFrames, designed for a 2-minute video walkthrough.

Author: Data Analysis Fundamentals Course
Date: March 2026
"""

import pandas as pd
import numpy as np


def print_section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def demonstrate_missing_value_detection():
    """
    Comprehensive demonstration of missing value detection in Pandas.
    
    This function covers:
    1. Loading data
    2. Detecting missing values
    3. Counting missing values per column
    4. Identifying rows with missing data
    5. Explaining why detection matters
    """
    
    # ========================================================================
    # PART 1: LOAD THE DATASET
    # ========================================================================
    print_section_header("PART 1: Loading Dataset with Missing Values")
    
    # Load the employee survey data with missing values
    df = pd.read_csv('data/raw/employee_survey_with_missing_2026_Q1.csv')
    
    print(f"\n✓ Dataset loaded successfully!")
    print(f"  - Shape: {df.shape} ({df.shape[0]} rows × {df.shape[1]} columns)")
    print(f"  - Total cells: {df.shape[0] * df.shape[1]:,}")
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    # ========================================================================
    # PART 2: DETECT MISSING VALUES
    # ========================================================================
    print_section_header("PART 2: Detecting Missing Values")
    
    print("\nUsing isna() to create a boolean mask:")
    print("(True = missing, False = present)\n")
    
    missing_mask = df.isna()
    print("First 5 rows of missing value mask:")
    print(missing_mask.head())
    
    print("\nKey insight:")
    print("  - isna() returns a DataFrame of True/False values")
    print("  - True indicates a missing value")
    print("  - Same shape as original DataFrame")
    
    # ========================================================================
    # PART 3: COUNT MISSING VALUES PER COLUMN
    # ========================================================================
    print_section_header("PART 3: Counting Missing Values Per Column")
    
    print("\nMissing value counts by column:")
    missing_counts = df.isna().sum()
    print(missing_counts)
    
    print(f"\nTotal missing cells in entire dataset: {df.isna().sum().sum()}")
    
    # Calculate percentages
    print("\n" + "-" * 80)
    print("Missing value percentages (more informative than raw counts):")
    print("-" * 80)
    
    missing_percentage = (df.isna().sum() / len(df) * 100).round(2)
    
    # Create summary DataFrame
    summary = pd.DataFrame({
        'Column': df.columns,
        'Missing_Count': missing_counts.values,
        'Missing_Percent': missing_percentage.values
    })
    
    # Show only columns with missing values
    summary_with_missing = summary[summary['Missing_Count'] > 0].sort_values(
        'Missing_Count', 
        ascending=False
    )
    
    print(f"\n{len(summary_with_missing)} columns have missing values:\n")
    print(summary_with_missing.to_string(index=False))
    
    # ========================================================================
    # PART 4: IDENTIFY ROWS WITH MISSING DATA
    # ========================================================================
    print_section_header("PART 4: Identifying Rows with Missing Data")
    
    # Find rows with any missing value
    rows_with_missing = df[df.isna().any(axis=1)]
    complete_rows = df[df.notna().all(axis=1)]
    
    print(f"\nRows with at least one missing value: {len(rows_with_missing)}")
    print(f"Complete rows (no missing values): {len(complete_rows)}")
    print(f"Percentage affected: {(len(rows_with_missing) / len(df) * 100):.1f}%")
    
    print("\nFirst 3 rows with missing data:")
    print(rows_with_missing.head(3))
    
    # Show missing value distribution per row
    print("\n" + "-" * 80)
    print("Distribution of missing values per row:")
    print("-" * 80)
    
    missing_per_row = df.isna().sum(axis=1)
    distribution = missing_per_row.value_counts().sort_index()
    
    for num_missing, count in distribution.items():
        print(f"  {num_missing} missing value(s): {count} rows")
    
    # Highlight a specific example
    print("\n" + "-" * 80)
    print("Example: Rows missing critical 'satisfaction_score' column:")
    print("-" * 80)
    
    missing_satisfaction = df[df['satisfaction_score'].isna()]
    print(f"\nFound {len(missing_satisfaction)} rows")
    print("\nSample:")
    print(missing_satisfaction[['employee_id', 'department', 'satisfaction_score', 'response_text']].head(3))
    
    # ========================================================================
    # PART 5: WHY DETECTION MATTERS
    # ========================================================================
    print_section_header("PART 5: Why Missing Value Detection Matters")
    
    print("\n🎯 Detection is CRITICAL because missing values:")
    print()
    print("  1. DISTORT STATISTICS")
    print("     - Mean, median, and counts will be incorrect")
    print("     - Example: Average satisfaction without handling missing values")
    
    # Demonstrate the impact
    mean_with_na = df['satisfaction_score'].mean()
    mean_described = df['satisfaction_score'].describe()['mean']
    
    print(f"\n     Average satisfaction score: {mean_with_na:.2f}")
    print(f"     Based on {df['satisfaction_score'].notna().sum()} out of {len(df)} responses")
    print(f"     Missing: {df['satisfaction_score'].isna().sum()} ({df['satisfaction_score'].isna().sum()/len(df)*100:.1f}%)")
    
    print("\n  2. CREATE SILENT ERRORS")
    print("     - Analysis may complete without warnings")
    print("     - Results appear correct but are misleading")
    
    print("\n  3. INTRODUCE BIAS")
    print("     - If missing data is not random (e.g., only unhappy employees skip)")
    print("     - Results won't represent the full population")
    
    print("\n  4. BREAK DOWNSTREAM PROCESSES")
    print("     - Machine learning models may fail or produce poor results")
    print("     - Visualizations may be incorrect")
    print("     - Reports will have incomplete information")
    
    print("\n" + "=" * 80)
    print(" BEST PRACTICE WORKFLOW")
    print("=" * 80)
    print("""
    Step 1: Load data
    Step 2: IMMEDIATELY check for missing values ← YOU ARE HERE
    Step 3: Understand WHY data is missing
    Step 4: Decide handling strategy (drop, fill, or keep with special handling)
    Step 5: Document your decisions
    Step 6: Proceed with analysis
    
    ⚠️  NEVER skip Step 2! Detection comes BEFORE action.
    """)
    
    # ========================================================================
    # FINAL SUMMARY
    # ========================================================================
    print_section_header("SUMMARY: Quick Missing Value Check")
    
    total_cells = df.shape[0] * df.shape[1]
    total_missing = df.isna().sum().sum()
    
    print(f"""
    Dataset: employee_survey_with_missing_2026_Q1.csv
    
    Overall Statistics:
      • Total cells: {total_cells:,}
      • Missing cells: {total_missing:,}
      • Missing percentage: {(total_missing/total_cells*100):.2f}%
      
    Column Impact:
      • Columns with missing data: {len(summary_with_missing)} out of {len(df.columns)}
      • Worst column: {summary_with_missing.iloc[0]['Column']} ({summary_with_missing.iloc[0]['Missing_Percent']:.1f}% missing)
      
    Row Impact:
      • Rows affected: {len(rows_with_missing)} out of {len(df)} ({len(rows_with_missing)/len(df)*100:.1f}%)
      • Complete rows: {len(complete_rows)} ({len(complete_rows)/len(df)*100:.1f}%)
    
    ✅ Detection complete! Ready to decide on handling strategy.
    """)
    print("=" * 80)


def quick_missing_check(dataframe, dataset_name="Dataset"):
    """
    Quick utility function for checking missing values in any DataFrame.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The DataFrame to check
    dataset_name : str
        Name of the dataset for display purposes
    """
    print_section_header(f"Quick Missing Value Check: {dataset_name}")
    
    total_missing = dataframe.isna().sum().sum()
    
    if total_missing == 0:
        print("\n✅ No missing values detected! Dataset is complete.")
    else:
        print(f"\n⚠️  Found {total_missing} missing values")
        print("\nBreakdown by column:")
        
        missing_summary = pd.DataFrame({
            'Column': dataframe.columns,
            'Missing': dataframe.isna().sum().values,
            'Percent': ((dataframe.isna().sum() / len(dataframe)) * 100).round(2).values
        })
        
        missing_summary = missing_summary[missing_summary['Missing'] > 0].sort_values(
            'Missing', 
            ascending=False
        )
        
        print(missing_summary.to_string(index=False))
        
        rows_affected = len(dataframe[dataframe.isna().any(axis=1)])
        print(f"\n{rows_affected} rows affected ({rows_affected/len(dataframe)*100:.1f}%)")
    
    print("=" * 80)
    

if __name__ == "__main__":
    """
    Main execution block for video demonstration.
    
    Run this script to see a complete demonstration of missing value detection.
    Recommended for recording the 2-minute video walkthrough.
    """
    
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "DETECTING MISSING VALUES IN PANDAS DATAFRAMES" + " " * 18 + "║")
    print("║" + " " * 25 + "Video Demonstration Script" + " " * 26 + "║")
    print("╚" + "=" * 78 + "╝")
    
    print("\nThis demonstration covers:")
    print("  1. Loading data with missing values")
    print("  2. Detecting missing values using isna()")
    print("  3. Counting missing values per column")
    print("  4. Identifying rows with missing data")
    print("  5. Understanding why detection is critical")
    print("\n" + "=" * 80)
    
    # Run the main demonstration
    demonstrate_missing_value_detection()
    
    print("\n✅ Demonstration complete!")
    print("\nUse this script as a guide for your video recording.")
    print("Remember to explain each step clearly and show outputs.")
    print("\n" + "=" * 80)
