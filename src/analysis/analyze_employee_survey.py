"""
Employee Survey Data Analysis Script

This is a standalone Python script that demonstrates:
1. Loading data from a CSV file
2. Performing basic data analysis
3. Printing results to console

This script is meant to be run from the terminal/command line,
not in a notebook environment.
"""

import pandas as pd
import os

# ============================================================================
# 1. LOAD THE DATA
# ============================================================================
# Get the path to the survey data relative to this script
# Navigate up from src/analysis to project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
data_path = os.path.join(project_root, 'data', 'raw', 'employee_survey_2026_Q1.csv')

print("=" * 70)
print("EMPLOYEE SURVEY DATA ANALYSIS")
print("=" * 70)
print(f"\nLoading data from: {data_path}")

# Load the CSV file
df = pd.read_csv(data_path)

# ============================================================================
# 2. EXPLORE THE DATA
# ============================================================================
print("\n" + "=" * 70)
print("DATASET OVERVIEW")
print("=" * 70)

print(f"\nTotal number of responses: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print(f"\nColumn names:")
for col in df.columns:
    print(f"  - {col}")

# ============================================================================
# 3. BASIC STATISTICS
# ============================================================================
print("\n" + "=" * 70)
print("SATISFACTION SCORE STATISTICS")
print("=" * 70)

satisfaction_stats = df['satisfaction_score'].describe()
print(f"\nMean satisfaction score: {satisfaction_stats['mean']:.2f}")
print(f"Median satisfaction score: {df['satisfaction_score'].median():.2f}")
print(f"Min satisfaction score: {satisfaction_stats['min']:.0f}")
print(f"Max satisfaction score: {satisfaction_stats['max']:.0f}")
print(f"Standard deviation: {satisfaction_stats['std']:.2f}")

# ============================================================================
# 4. ANALYSIS BY DEPARTMENT
# ============================================================================
print("\n" + "=" * 70)
print("SATISFACTION BY DEPARTMENT")
print("=" * 70)

department_analysis = df.groupby('department')['satisfaction_score'].agg(['count', 'mean', 'std'])
department_analysis.columns = ['Responses', 'Avg Score', 'Std Dev']
department_analysis = department_analysis.sort_values('Avg Score', ascending=False)

print("\n" + department_analysis.to_string())

# ============================================================================
# 5. WORK-LIFE BALANCE INSIGHTS
# ============================================================================
print("\n" + "=" * 70)
print("WORK-LIFE BALANCE ANALYSIS")
print("=" * 70)

avg_worklife = df['work_life_balance'].mean()
print(f"\nAverage work-life balance score: {avg_worklife:.2f}/10")
print(f"Employees satisfied with work-life balance (score >= 7): {len(df[df['work_life_balance'] >= 7])} / {len(df)}")
print(f"Employees struggling with work-life balance (score <= 4): {len(df[df['work_life_balance'] <= 4])} / {len(df)}")

# ============================================================================
# 6. TEAM COLLABORATION
# ============================================================================
print("\n" + "=" * 70)
print("TEAM COLLABORATION INSIGHTS")
print("=" * 70)

avg_collab = df['team_collaboration'].mean()
print(f"\nAverage team collaboration score: {avg_collab:.2f}/10")

best_depts = df.groupby('department')['team_collaboration'].mean().sort_values(ascending=False)
print(f"\nBest departments for team collaboration:")
for dept, score in best_depts.head(3).items():
    print(f"  {dept}: {score:.2f}/10")

# ============================================================================
# 7. SUMMARY AND RECOMMENDATIONS
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"\nKey Findings:")
print(f"  - Total survey responses: {len(df)}")
print(f"  - Overall satisfaction: {df['satisfaction_score'].mean():.2f}/10")
print(f"  - Best practice area: Team Collaboration ({avg_collab:.2f}/10)")
print(f"  - Area for improvement: Career Growth ({df['career_growth'].mean():.2f}/10)")
print(f"  - Departments above avg satisfaction: {len(department_analysis[department_analysis['Avg Score'] > df['satisfaction_score'].mean()])}")

print("\n" + "=" * 70)
print("Analysis complete! This script ran successfully from the command line.")
print("=" * 70 + "\n")
