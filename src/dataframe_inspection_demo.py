"""
DataFrame Inspection Demonstration
===================================

This script demonstrates the three essential DataFrame inspection methods:
1. head() - Preview data
2. info() - Check structure and types
3. describe() - Statistical summary

Author: Trivin Insight Engine
Date: March 2026
"""

import pandas as pd
import numpy as np


def main():
    """
    Main function demonstrating DataFrame inspection techniques.
    """
    print("\n" + "=" * 80)
    print("DATAFRAME INSPECTION DEMONSTRATION")
    print("=" * 80)
    
    # Load the dataset
    print("\n📂 Loading employee survey data...")
    df = pd.read_csv('../data/processed/employee_survey_cleaned_2026_Q1.csv')
    print(f"✓ Data loaded successfully!")
    print(f"   Dataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Section 1: head()
    print("\n" + "=" * 80)
    print("1. INSPECTING DATA WITH head()")
    print("=" * 80)
    print("\nPurpose: Quick visual preview of the data")
    print("Shows: Column names, sample values, data alignment\n")
    
    print("First 5 rows (default):")
    print(df.head())
    
    print("\n" + "-" * 80)
    print("Last 3 rows using tail(3):")
    print(df.tail(3))
    
    # Section 2: info()
    print("\n\n" + "=" * 80)
    print("2. INSPECTING STRUCTURE WITH info()")
    print("=" * 80)
    print("\nPurpose: Understand DataFrame structure and health")
    print("Shows: Data types, missing values, memory usage\n")
    
    df.info()
    
    print("\n" + "-" * 80)
    print("Missing Values Analysis:")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("✓ No missing values detected!")
    else:
        print(missing[missing > 0])
    
    # Section 3: describe()
    print("\n\n" + "=" * 80)
    print("3. SUMMARIZING DATA WITH describe()")
    print("=" * 80)
    print("\nPurpose: Statistical summary of numeric columns")
    print("Shows: count, mean, std, min, max, percentiles\n")
    
    print("Numeric columns summary:")
    print(df.describe())
    
    print("\n" + "-" * 80)
    print("Categorical columns summary:")
    print(df.describe(include='object'))
    
    # Section 4: When to use each method
    print("\n\n" + "=" * 80)
    print("4. WHEN TO USE EACH METHOD")
    print("=" * 80)
    
    print("\n┌─────────────┬────────────────────────────┬──────────────────────────┐")
    print("│   Method    │     Question It Answers    │       When to Use        │")
    print("├─────────────┼────────────────────────────┼──────────────────────────┤")
    print("│  head()     │ What does data look like?  │ Quick visual preview     │")
    print("│  info()     │ How is data structured?    │ Check types, missing vals│")
    print("│  describe() │ What are the patterns?     │ Stats, spot outliers     │")
    print("└─────────────┴────────────────────────────┴──────────────────────────┘")
    
    # Key Insights
    print("\n\n" + "=" * 80)
    print("KEY INSIGHTS FROM INSPECTION")
    print("=" * 80)
    
    print(f"\n✓ Dataset contains {df.shape[0]} employee survey responses")
    print(f"✓ {df.shape[1]} columns capturing various satisfaction metrics")
    
    # Get some specific insights
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(f"✓ {len(numeric_cols)} numeric columns for analysis")
    
    if 'satisfaction_score' in df.columns:
        avg_satisfaction = df['satisfaction_score'].mean()
        print(f"✓ Average satisfaction score: {avg_satisfaction:.2f}")
    
    if 'department' in df.columns:
        dept_count = df['department'].nunique()
        top_dept = df['department'].value_counts().index[0]
        print(f"✓ {dept_count} departments surveyed")
        print(f"✓ Most responses from: {top_dept}")
    
    print("\n" + "=" * 80)
    print("✓ INSPECTION COMPLETE - Data is ready for analysis!")
    print("=" * 80)


def inspect_any_dataframe(df, name="DataFrame"):
    """
    Reusable function to inspect any DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to inspect
    name : str
        Name to display in the report
        
    Returns:
    --------
    None (prints inspection report)
    """
    print("\n" + "=" * 80)
    print(f"INSPECTION REPORT: {name}")
    print("=" * 80)
    
    # Shape
    print(f"\n📊 SHAPE")
    print(f"   Rows: {df.shape[0]:,}")
    print(f"   Columns: {df.shape[1]}")
    
    # Preview
    print(f"\n👀 PREVIEW (First 3 rows)")
    print(df.head(3))
    
    # Structure
    print(f"\n🏗️  STRUCTURE")
    df.info()
    
    # Missing Values
    print(f"\n❓ MISSING VALUES")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("   ✓ No missing values detected!")
    else:
        missing_percent = (missing / len(df)) * 100
        missing_df = pd.DataFrame({
            'Missing Count': missing,
            'Percentage': missing_percent.round(2)
        })
        print(missing_df[missing_df['Missing Count'] > 0])
    
    # Numeric Summary
    print(f"\n📈 NUMERIC SUMMARY")
    print(df.describe())
    
    # Categorical Summary
    categorical_cols = df.select_dtypes(include='object').columns
    if len(categorical_cols) > 0:
        print(f"\n📝 CATEGORICAL SUMMARY")
        print(df.describe(include='object'))
    
    print("\n" + "=" * 80)
    print("✓ Inspection Complete")
    print("=" * 80)


if __name__ == "__main__":
    main()
    
    print("\n\n" + "=" * 80)
    print("WHY INSPECTION MATTERS")
    print("=" * 80)
    print("""
Most analysis mistakes start with poor inspection.

Common issues avoided by proper inspection:
✗ Starting analysis without understanding the data
✗ Misinterpreting column data types
✗ Missing hidden null values
✗ Drawing conclusions from incomplete information

Always inspect BEFORE cleaning, analysis, or modeling!

Inspection is a foundational Data Science habit.
    """)
