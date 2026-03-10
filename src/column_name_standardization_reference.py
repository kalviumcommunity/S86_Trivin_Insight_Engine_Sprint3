"""
Column Name Standardization - Quick Reference Guide
====================================================

This is a quick reference for standardizing column names and data formats.
Keep this file open while working on data cleaning tasks.

Author: Data Analysis Fundamentals Course
Date: March 2026
"""

import pandas as pd
import re


# ==============================================================================
# QUICK STANDARDIZATION FUNCTIONS
# ==============================================================================

def standardize_column_names(df):
    """
    Standardize column names to snake_case.
    
    Rules: lowercase, underscores, no special characters
    
    Example:
    --------
    >>> df_clean = standardize_column_names(df_messy)
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


def standardize_text_data(df, column, case='title'):
    """
    Standardize text data in a column.
    
    Parameters:
    -----------
    df : pd.DataFrame
    column : str
        Column name to standardize
    case : str
        'lower', 'upper', or 'title'
    
    Example:
    --------
    >>> df['department'] = standardize_text_data(df, 'department', 'title')
    """
    df = df.copy()
    df[column] = df[column].astype(str).str.strip()
    df[column] = df[column].str.replace(r'\s+', ' ', regex=True)
    
    if case == 'lower':
        df[column] = df[column].str.lower()
    elif case == 'upper':
        df[column] = df[column].str.upper()
    elif case == 'title':
        df[column] = df[column].str.title()
    
    return df


# ==============================================================================
# NAMING CONVENTION EXAMPLES
# ==============================================================================

"""
✅ GOOD COLUMN NAMES (snake_case):
------------------------------------
employee_id
department_name
satisfaction_score
work_life_balance
survey_date
response_text
avg_score
total_responses
created_at
updated_at


❌ BAD COLUMN NAMES (avoid these):
------------------------------------
'Employee ID'           # spaces, capitals
'Department Name'       # spaces, capitals
'Satisfaction Score'    # spaces, capitals
'Work/Life Balance'     # spaces, capitals, special chars
'Survey Date (Q1)'      # spaces, capitals, parentheses
'AvgScore'              # camelCase (use for programming, not data)
'TOTAL_RESPONSES'       # all caps (use for constants, not columns)
'createdAt'             # camelCase
'response-text'         # hyphens (use underscores instead)
'avg score %'           # spaces, special chars


🎯 NAMING RULES:
----------------
1. Use lowercase letters only
2. Replace spaces with underscores
3. Remove special characters (!@#$%^&*()-+=[]{}|;:',.<>?/")
4. Use descriptive names (not abbreviations)
5. Be consistent across datasets
6. Keep names concise but clear


🎯 TEXT DATA STANDARDIZATION:
------------------------------
Before:  ['  Engineering', 'marketing  ', 'Sales', 'hr', 'FINANCE']
After:   ['Engineering', 'Marketing', 'Sales', 'Hr', 'Finance']

Rules:
1. Strip leading/trailing whitespace
2. Remove extra internal spaces
3. Apply consistent casing (title, lower, or upper)
4. Handle null/missing values appropriately


🎯 WHEN TO STANDARDIZE:
-----------------------
✓ Immediately after loading data
✓ Before merging/joining datasets
✓ Before any analysis
✓ At the start of your data pipeline
✗ Not as an afterthought or "nice to have"


🎯 COMMON WORKFLOWS:
--------------------

# Workflow 1: Load and standardize
df = pd.read_csv('data.csv')
df = standardize_column_names(df)
df = standardize_text_data(df, 'department', 'title')

# Workflow 2: Check before standardizing
print("Before:", df.columns.tolist())
df = standardize_column_names(df)
print("After:", df.columns.tolist())

# Workflow 3: Standardize multiple text columns
text_cols = ['department', 'city', 'state']
for col in text_cols:
    df = standardize_text_data(df, col, 'title')
"""


# ==============================================================================
# QUICK CHECKS
# ==============================================================================

def check_column_names(df):
    """Check if column names need standardization."""
    issues = []
    for col in df.columns:
        if ' ' in col:
            issues.append(f"'{col}' has spaces")
        if col != col.lower():
            issues.append(f"'{col}' has uppercase")
        if re.search(r'[^a-z0-9_]', col.lower()):
            issues.append(f"'{col}' has special characters")
    
    if issues:
        print("❌ Issues found:")
        for issue in issues:
            print(f"  • {issue}")
        return False
    else:
        print("✅ Column names are clean!")
        return True


def preview_standardization(df):
    """Preview what standardized column names will look like."""
    print("Column name transformation preview:\n")
    for orig in df.columns:
        clean = orig.lower().replace(' ', '_')
        clean = re.sub(r'[^a-z0-9_]', '', clean)
        clean = re.sub(r'_+', '_', clean).strip('_')
        print(f"  '{orig}' → '{clean}'")


# ==============================================================================
# USAGE EXAMPLES
# ==============================================================================

if __name__ == "__main__":
    # Example 1: Create messy data
    data = {
        'Employee ID': [1, 2, 3],
        'Department Name': ['  Eng', 'sales  ', 'HR'],
        'Salary ($)': [50000, 60000, 70000]
    }
    df = pd.DataFrame(data)
    
    print("=" * 70)
    print("EXAMPLE: Column Name Standardization")
    print("=" * 70)
    
    # Check current state
    print("\n1. Check current column names:")
    check_column_names(df)
    
    # Preview standardization
    print("\n2. Preview standardization:")
    preview_standardization(df)
    
    # Apply standardization
    print("\n3. Apply standardization:")
    df_clean = standardize_column_names(df)
    print("✅ Columns standardized!")
    
    # Verify
    print("\n4. Verify result:")
    check_column_names(df_clean)
    
    print("\n" + "=" * 70)
    print("✅ Quick reference demonstration complete!")
    print("=" * 70)
