# Outlier Detection Quick Reference

## What Is an Outlier

An outlier is a value that stands far from the majority of observations.
Outliers can be:

- valid rare observations
- measurement or data-entry errors
- signals of a different subgroup

Outliers are context-dependent.

---

## Why Outliers Matter

Outliers can strongly affect:

- mean values
- spread and variance
- trend interpretation
- downstream modeling decisions

Early detection improves analysis quality.

---

## Visual Detection Checklist

1. Boxplot:
- points beyond whiskers are potential outliers

2. Scatter plot:
- isolated points away from main cloud are potential outliers

3. Histogram:
- unusually sparse extreme tails may indicate outliers

Visuals are early warning tools.

---

## Rule-Based Detection Checklist

### IQR Rule

1. Compute quartiles and IQR:
- Q1 = 25th percentile
- Q3 = 75th percentile
- IQR = Q3 - Q1

2. Compute bounds:
- Lower bound = Q1 - 1.5 * IQR
- Upper bound = Q3 + 1.5 * IQR

3. Flag values outside bounds.

### Simple Threshold Rule

Use domain-aware limits (example for 1-10 score):
- low threshold: < 3
- high threshold: > 9

Rules indicate unusual values. They are not automatic deletion commands.

---

## Quick Code Template

```python
import pandas as pd

col = 'satisfaction_score'
df = pd.read_csv('data/raw/employee_survey_2026_Q1.csv')

q1 = df[col].quantile(0.25)
q3 = df[col].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

iqr_flagged = df[(df[col] < lower) | (df[col] > upper)]
threshold_flagged = df[(df[col] < 3) | (df[col] > 9)]
```

---

## Interpretation Questions

- Does this value make sense in context?
- Is the value plausible or likely an error?
- Is the point influential for summary statistics?
- Should it be investigated further before cleaning?

---

## Good Practice Rules

- combine visuals and simple rules
- document why points were flagged
- investigate before taking action
- keep raw data unchanged

---

## What Not To Do

- do not remove all outliers by default
- do not rely on one method only
- do not treat rarity as error automatically
- do not skip explanation in reports
