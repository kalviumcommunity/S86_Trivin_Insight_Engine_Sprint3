"""
Complete Data Standardization Workflow
========================================

This script demonstrates a complete data cleaning and standardization workflow:
1. Load raw data
2. Standardize column names
3. Standardize data formats (text, dates, numbers)
4. Identify and remove duplicates
5. Compute summary statistics
6. Save cleaned data

Author: Data Analysis Fundamentals Course
Date: March 2026
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime


def print_section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def standardize_column_names(df):
    """
    Standardize column names to snake_case format.
    
    Rules:
    - Convert to lowercase
    - Replace spaces with underscores
    - Remove special characters
    - Ensure consistency
    """
    df_clean = df.copy()
    new_columns = []
    
    for col in df_clean.columns:
        col_clean = col.lower()
        col_clean = col_clean.replace(' ', '_')
        col_clean = re.sub(r'[^a-z0-9_]', '', col_clean)
        col_clean = re.sub(r'_+', '_', col_clean)
        col_clean = col_clean.strip('_')
        new_columns.append(col_clean)
    
    df_clean.columns = new_columns
    return df_clean


def standardize_text_columns(df, text_columns):
    """Standardize text data in specified columns."""
    df_clean = df.copy()
    
    for col in text_columns:
        if col in df_clean.columns:
            # Strip whitespace
            df_clean[col] = df_clean[col].astype(str).str.strip()
            # Remove extra spaces
            df_clean[col] = df_clean[col].str.replace(r'\s+', ' ', regex=True)
            # Apply title case for categorical columns
            df_clean[col] = df_clean[col].str.title()
    
    return df_clean


def standardize_numeric_columns(df, numeric_columns):
    """Ensure numeric columns have correct data types."""
    df_clean = df.copy()
    
    for col in numeric_columns:
        if col in df_clean.columns:
            # Convert to numeric, coercing errors to NaN
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    return df_clean


def standardize_date_columns(df, date_columns):
    """Standardize date columns to datetime format."""
    df_clean = df.copy()
    
    for col in date_columns:
        if col in df_clean.columns:
            # Convert to datetime
            df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
    
    return df_clean


def identify_duplicates(df):
    """Identify duplicate records in the DataFrame."""
    duplicates = df.duplicated()
    duplicate_count = duplicates.sum()
    
    if duplicate_count > 0:
        print(f"\n⚠️  Found {duplicate_count} duplicate record(s)")
        print("\nDuplicate rows:")
        print(df[duplicates])
    else:
        print("\n✓ No duplicate records found")
    
    return duplicates


def remove_duplicates(df, keep='first'):
    """
    Remove duplicate records from DataFrame.
    
    Parameters:
    -----------
    df : pd.DataFrame
    keep : str
        'first': Keep first occurrence
        'last': Keep last occurrence
        False: Remove all duplicates
    """
    df_clean = df.drop_duplicates(keep=keep)
    removed_count = len(df) - len(df_clean)
    
    if removed_count > 0:
        print(f"\n✓ Removed {removed_count} duplicate record(s)")
        print(f"  Original rows: {len(df)}")
        print(f"  After removal: {len(df_clean)}")
    
    return df_clean


def compute_summary_statistics(df, numeric_columns):
    """Compute and display summary statistics for numeric columns."""
    print("\n📊 Summary Statistics for Numeric Columns:")
    print("-" * 80)
    
    for col in numeric_columns:
        if col in df.columns:
            print(f"\n{col.upper()}:")
            print(f"  Count:   {df[col].count()}")
            print(f"  Mean:    {df[col].mean():.2f}")
            print(f"  Median:  {df[col].median():.2f}")
            print(f"  Std Dev: {df[col].std():.2f}")
            print(f"  Min:     {df[col].min():.2f}")
            print(f"  Max:     {df[col].max():.2f}")
    
    return df.describe()


def main():
    """Main workflow demonstrating complete data standardization."""
    
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "  COMPLETE DATA STANDARDIZATION WORKFLOW".center(78) + "║")
    print("║" + "  Data Cleaning and Preparation".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    
    # ========================================================================
    # STEP 1: LOAD RAW DATA
    # ========================================================================
    print_section_header("STEP 1: Load Raw Data")
    
    # Try to load messy CSV first, fallback to clean CSV
    try:
        df_raw = pd.read_csv('data/raw/employee_survey_messy_columns.csv')
        print("\n✓ Loaded dataset: employee_survey_messy_columns.csv")
    except FileNotFoundError:
        df_raw = pd.read_csv('data/raw/employee_survey_2026_Q1.csv')
        print("\n✓ Loaded dataset: employee_survey_2026_Q1.csv")
    
    print(f"  Shape: {df_raw.shape} ({df_raw.shape[0]} rows × {df_raw.shape[1]} columns)")
    
    print("\n📋 Original Column Names:")
    for i, col in enumerate(df_raw.columns, 1):
        print(f"  {i}. '{col}'")
    
    print("\nFirst 3 rows:")
    print(df_raw.head(3))
    
    # ========================================================================
    # STEP 2: STANDARDIZE COLUMN NAMES
    # ========================================================================
    print_section_header("STEP 2: Standardize Column Names")
    
    print("\n🔧 Applying snake_case naming convention...")
    df_clean = standardize_column_names(df_raw)
    
    print("\n✅ Column name transformation:")
    for orig, new in zip(df_raw.columns, df_clean.columns):
        if orig != new:
            print(f"  '{orig}' → '{new}'")
    
    print("\n📋 Standardized Column Names:")
    for i, col in enumerate(df_clean.columns, 1):
        print(f"  {i}. {col}")
    
    # ========================================================================
    # STEP 3: STANDARDIZE DATA FORMATS
    # ========================================================================
    print_section_header("STEP 3: Standardize Data Formats")
    
    # Identify column types
    text_cols = [col for col in df_clean.columns if 'department' in col or 'name' in col]
    date_cols = [col for col in df_clean.columns if 'date' in col]
    numeric_cols = [col for col in df_clean.columns if any(x in col for x in 
                   ['score', 'balance', 'support', 'growth', 'collaboration', 'satisfaction'])]
    
    # Standardize text columns
    if text_cols:
        print("\n📝 Standardizing text columns:", text_cols)
        df_clean = standardize_text_columns(df_clean, text_cols)
        print("✓ Text columns standardized (whitespace removed, title case applied)")
    
    # Standardize numeric columns
    if numeric_cols:
        print("\n🔢 Standardizing numeric columns:", numeric_cols)
        df_clean = standardize_numeric_columns(df_clean, numeric_cols)
        print("✓ Numeric columns verified and converted")
    
    # Standardize date columns
    if date_cols:
        print("\n📅 Standardizing date columns:", date_cols)
        df_clean = standardize_date_columns(df_clean, date_cols)
        print("✓ Date columns converted to datetime format")
    
    print("\n📊 Data after standardization:")
    print(df_clean.head(3))
    
    # ========================================================================
    # STEP 4: IDENTIFY AND REMOVE DUPLICATES
    # ========================================================================
    print_section_header("STEP 4: Identify and Remove Duplicates")
    
    # Check for duplicates
    print("\n🔍 Checking for duplicate records...")
    duplicates = identify_duplicates(df_clean)
    
    # Remove duplicates if found
    if duplicates.sum() > 0:
        df_clean = remove_duplicates(df_clean, keep='first')
    
    # ========================================================================
    # STEP 5: COMPUTE SUMMARY STATISTICS
    # ========================================================================
    print_section_header("STEP 5: Compute Summary Statistics")
    
    if numeric_cols:
        summary_stats = compute_summary_statistics(df_clean, numeric_cols)
        
        print("\n\n📈 Complete Statistical Summary:")
        print(summary_stats)
    
    # ========================================================================
    # STEP 6: DATA QUALITY REPORT
    # ========================================================================
    print_section_header("STEP 6: Data Quality Report")
    
    print("\n📊 DataFrame Information:")
    print(f"  Total Rows:    {len(df_clean)}")
    print(f"  Total Columns: {len(df_clean.columns)}")
    print(f"  Memory Usage:  {df_clean.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
    print("\n🔍 Missing Values:")
    missing = df_clean.isnull().sum()
    if missing.sum() > 0:
        for col, count in missing[missing > 0].items():
            print(f"  {col}: {count} missing ({count/len(df_clean)*100:.1f}%)")
    else:
        print("  ✓ No missing values detected")
    
    print("\n📋 Data Types:")
    for col, dtype in df_clean.dtypes.items():
        print(f"  {col}: {dtype}")
    
    # ========================================================================
    # STEP 7: SAVE CLEANED DATA
    # ========================================================================
    print_section_header("STEP 7: Save Cleaned Data")
    
    output_path = 'data/processed/employee_survey_standardized.csv'
    df_clean.to_csv(output_path, index=False)
    print(f"\n✓ Cleaned data saved to: {output_path}")
    print(f"  Rows: {len(df_clean)}")
    print(f"  Columns: {len(df_clean.columns)}")
    
    # ========================================================================
    # FINAL SUMMARY
    # ========================================================================
    print_section_header("WORKFLOW COMPLETE!")
    
    print("\n✅ Standardization Summary:")
    print(f"  ✓ Column names standardized to snake_case")
    print(f"  ✓ Text data cleaned and normalized")
    print(f"  ✓ Numeric columns verified")
    print(f"  ✓ Date columns converted to datetime")
    print(f"  ✓ Duplicates removed (if any)")
    print(f"  ✓ Summary statistics computed")
    print(f"  ✓ Clean data saved to {output_path}")
    
    print("\n💡 Best Practices Applied:")
    print("  1. Standardized early in the workflow")
    print("  2. Applied consistent naming conventions")
    print("  3. Cleaned and normalized all data formats")
    print("  4. Removed duplicate records")
    print("  5. Validated data quality")
    print("  6. Documented the process")
    
    print("\n🎯 Next Steps:")
    print("  • Use the cleaned data for analysis")
    print("  • Apply the same workflow to other datasets")
    print("  • Build reusable cleaning functions")
    print("  • Share standardization practices with your team")
    
    print("\n" + "=" * 80)
    print(" 🎉 Your data is clean, standardized, and analysis-ready!")
    print("=" * 80 + "\n")
    
    return df_clean


if __name__ == "__main__":
    # Run the complete workflow
    cleaned_df = main()
