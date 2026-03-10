"""
Column Name and Data Format Standardization - Video Demonstration Script
==========================================================================

This script demonstrates the core concepts of standardizing column names
and data formats in Pandas DataFrames, designed for a 2-minute video walkthrough.

Learning Objectives:
- Convert column names to a consistent format
- Remove spaces and special characters from column names
- Apply predictable naming conventions (snake_case)
- Standardize simple data formats across columns
- Improve dataset usability and readability

Author: Data Analysis Fundamentals Course
Date: March 2026
"""

import pandas as pd
import numpy as np
import re


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
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with potentially messy column names
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with standardized column names
    """
    # Create a copy to avoid modifying original
    df_clean = df.copy()
    
    # Store original column names for comparison
    original_columns = df_clean.columns.tolist()
    
    # Apply standardization rules
    new_columns = []
    for col in original_columns:
        # Convert to lowercase
        col_clean = col.lower()
        
        # Replace spaces with underscores
        col_clean = col_clean.replace(' ', '_')
        
        # Remove special characters (keep only alphanumeric and underscore)
        col_clean = re.sub(r'[^a-z0-9_]', '', col_clean)
        
        # Remove multiple consecutive underscores
        col_clean = re.sub(r'_+', '_', col_clean)
        
        # Remove leading/trailing underscores
        col_clean = col_clean.strip('_')
        
        new_columns.append(col_clean)
    
    # Assign cleaned column names
    df_clean.columns = new_columns
    
    return df_clean, original_columns, new_columns


def standardize_text_columns(df, text_columns):
    """
    Standardize text data in specified columns.
    
    Rules:
    - Strip whitespace
    - Consistent casing
    - Remove extra spaces
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to clean
    text_columns : list
        List of column names to standardize
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with standardized text columns
    """
    df_clean = df.copy()
    
    for col in text_columns:
        if col in df_clean.columns:
            # Strip leading/trailing whitespace
            df_clean[col] = df_clean[col].astype(str).str.strip()
            
            # Remove extra internal spaces
            df_clean[col] = df_clean[col].str.replace(r'\s+', ' ', regex=True)
            
            # For categorical columns, ensure consistent casing (title case)
            if col in ['department']:
                df_clean[col] = df_clean[col].str.title()
    
    return df_clean


def demonstrate_column_standardization():
    """
    Comprehensive demonstration of column name and data format standardization.
    
    This function covers:
    1. Loading data with messy column names
    2. Identifying standardization issues
    3. Standardizing column names
    4. Standardizing text data formats
    5. Comparing before and after results
    6. Explaining why standardization matters
    """
    
    # ========================================================================
    # PART 1: CREATE SAMPLE DATA WITH MESSY COLUMN NAMES
    # ========================================================================
    print_section_header("PART 1: Creating Sample Dataset with Messy Column Names")
    
    # Create sample data with intentionally messy column names
    data = {
        'Employee ID': [1001, 1002, 1003, 1004, 1005],
        'Department Name': ['  Engineering', 'marketing  ', 'Sales', 'hr', 'FINANCE'],
        'Survey Date (Q1)': ['2026-01-15', '2026-01-16', '2026-01-17', '2026-01-18', '2026-01-19'],
        'Satisfaction Score (1-10)': [7, 9, 4, 8, 6],
        'Work/Life Balance': [8, 9, 3, 7, 7],
        'Manager Support %': [6, 8, 4, 8, 5],
        'Career-Growth': [5, 7, 3, 7, 4],
        'Team Collaboration!!!': [9, 8, 5, 9, 6]
    }
    
    df_messy = pd.DataFrame(data)
    
    print("\n✓ Sample dataset created with intentionally messy column names!")
    print(f"  - Shape: {df_messy.shape} ({df_messy.shape[0]} rows × {df_messy.shape[1]} columns)")
    
    print("\n📋 BEFORE STANDARDIZATION - Original Column Names:")
    for i, col in enumerate(df_messy.columns, 1):
        print(f"  {i}. '{col}'")
    
    print("\nFirst 3 rows (with messy columns):")
    print(df_messy.head(3))
    
    # ========================================================================
    # PART 2: IDENTIFY STANDARDIZATION ISSUES
    # ========================================================================
    print_section_header("PART 2: Identifying Column Name Issues")
    
    print("\n❌ Common Problems Found:")
    issues = []
    
    for col in df_messy.columns:
        col_issues = []
        
        if ' ' in col:
            col_issues.append("contains spaces")
        if col != col.lower():
            col_issues.append("mixed/upper case")
        if any(char in col for char in ['(', ')', '%', '/', '!', '-']):
            col_issues.append("special characters")
        if col.startswith(' ') or col.endswith(' '):
            col_issues.append("leading/trailing spaces")
            
        if col_issues:
            issues.append(f"  • '{col}': {', '.join(col_issues)}")
    
    for issue in issues:
        print(issue)
    
    print("\n💡 These issues make columns:")
    print("  - Harder to reference in code")
    print("  - Error-prone when merging datasets")
    print("  - Inconsistent across analysis")
    print("  - Difficult to work with programmatically")
    
    # ========================================================================
    # PART 3: STANDARDIZE COLUMN NAMES
    # ========================================================================
    print_section_header("PART 3: Standardizing Column Names")
    
    print("\n🔧 Applying standardization rules:")
    print("  1. Convert to lowercase")
    print("  2. Replace spaces with underscores")
    print("  3. Remove special characters")
    print("  4. Apply snake_case convention")
    
    df_clean, original_cols, new_cols = standardize_column_names(df_messy)
    
    print("\n✅ Column name transformation:")
    for orig, new in zip(original_cols, new_cols):
        print(f"  '{orig}' → '{new}'")
    
    print("\n📋 AFTER STANDARDIZATION - Cleaned Column Names:")
    for i, col in enumerate(df_clean.columns, 1):
        print(f"  {i}. {col}")
    
    # ========================================================================
    # PART 4: STANDARDIZE TEXT DATA FORMATS
    # ========================================================================
    print_section_header("PART 4: Standardizing Text Data Formats")
    
    print("\n🔍 Text data BEFORE standardization:")
    print(df_clean[['department_name']].head())
    print("\nIssues:")
    print("  • Leading/trailing whitespace")
    print("  • Inconsistent casing (lowercase, UPPERCASE, Title Case)")
    
    # Standardize text columns
    df_final = standardize_text_columns(df_clean, ['department_name'])
    
    print("\n✅ Text data AFTER standardization:")
    print(df_final[['department_name']].head())
    print("\nImprovements:")
    print("  • Whitespace removed")
    print("  • Consistent Title Case format")
    print("  • Ready for grouping and analysis")
    
    # ========================================================================
    # PART 5: COMPARE BEFORE AND AFTER
    # ========================================================================
    print_section_header("PART 5: Before and After Comparison")
    
    print("\n📊 BEFORE (Messy):")
    print(df_messy.head(3))
    
    print("\n" + "-" * 80)
    
    print("\n📊 AFTER (Standardized):")
    print(df_final.head(3))
    
    # ========================================================================
    # PART 6: PRACTICAL BENEFITS
    # ========================================================================
    print_section_header("PART 6: Why Standardization Matters")
    
    print("\n✅ Benefits of Standardized Column Names:")
    print("  1. Easier code: df['employee_id'] vs df['Employee ID']")
    print("  2. Predictable patterns across datasets")
    print("  3. No errors from spaces or special characters")
    print("  4. Cleaner merges and joins")
    print("  5. Better autocomplete in IDEs")
    print("  6. More professional and maintainable code")
    
    print("\n✅ Benefits of Standardized Data Formats:")
    print("  1. Consistent grouping and aggregation")
    print("  2. Reliable sorting and filtering")
    print("  3. Fewer bugs from data inconsistencies")
    print("  4. Easier data validation")
    print("  5. Better downstream processing")
    
    # ========================================================================
    # PART 7: DEMONSTRATION WITH REAL DATA
    # ========================================================================
    print_section_header("PART 7: Applying to Real Employee Survey Data")
    
    try:
        # Load real employee survey data
        df_survey = pd.read_csv('data/raw/employee_survey_2026_Q1.csv')
        
        print("\n✓ Real dataset loaded successfully!")
        print(f"  - Shape: {df_survey.shape}")
        
        print("\n📋 Current column names:")
        for i, col in enumerate(df_survey.columns, 1):
            print(f"  {i}. {col}")
        
        # Check if standardization is needed
        needs_cleaning = any(col != col.lower() or ' ' in col 
                           for col in df_survey.columns)
        
        if needs_cleaning:
            print("\n⚠️  This dataset has column naming issues!")
            df_survey_clean, orig, new = standardize_column_names(df_survey)
            
            print("\n✅ Standardized column names:")
            for i, col in enumerate(df_survey_clean.columns, 1):
                print(f"  {i}. {col}")
        else:
            print("\n✓ This dataset already follows good naming conventions!")
            print("  • All lowercase")
            print("  • Uses underscores instead of spaces")
            print("  • No special characters")
            print("\nThis is what we aim for in our own datasets!")
        
    except FileNotFoundError:
        print("\n⚠️  Real survey data file not found.")
        print("   Using demonstration data instead.")
    
    # ========================================================================
    # PART 8: BEST PRACTICES SUMMARY
    # ========================================================================
    print_section_header("PART 8: Best Practices for Data Standardization")
    
    print("\n🎯 Column Naming Convention (snake_case):")
    print("  ✅ Good: employee_id, satisfaction_score, work_life_balance")
    print("  ❌ Avoid: Employee ID, Satisfaction Score, Work/Life Balance")
    
    print("\n🎯 Text Data Standardization:")
    print("  ✅ Good: Consistent casing, no extra whitespace")
    print("  ❌ Avoid: Mixed casing, leading/trailing spaces")
    
    print("\n🎯 When to Standardize:")
    print("  • Immediately after loading data")
    print("  • Before any analysis or merging")
    print("  • At the start of your data pipeline")
    
    print("\n🎯 Why It Matters:")
    print("  • Clean data = Clean code")
    print("  • Prevents errors and bugs")
    print("  • Makes datasets reusable")
    print("  • Enables scalable analysis")
    
    print("\n" + "=" * 80)
    print(" ✅ STANDARDIZATION DEMONSTRATION COMPLETE!")
    print("=" * 80)
    print("\n💡 Remember: Standardize early, standardize always!")
    print("   Your future self (and teammates) will thank you.\n")
    
    return df_final


def main():
    """
    Main function to run the complete standardization demonstration.
    
    This serves as a complete 2-minute video walkthrough script covering:
    - Column name standardization
    - Data format standardization
    - Before/after comparisons
    - Real-world application
    - Best practices
    """
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "  COLUMN NAME AND DATA FORMAT STANDARDIZATION DEMONSTRATION".center(78) + "║")
    print("║" + "  Data Cleaning Fundamentals".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    
    # Run the complete demonstration
    df_result = demonstrate_column_standardization()
    
    print("\n📝 Next Steps:")
    print("  1. Practice with your own datasets")
    print("  2. Create a reusable standardization function")
    print("  3. Apply standardization at the start of every project")
    print("  4. Share these practices with your team")
    
    return df_result


if __name__ == "__main__":
    # Run the demonstration when script is executed
    result_df = main()
