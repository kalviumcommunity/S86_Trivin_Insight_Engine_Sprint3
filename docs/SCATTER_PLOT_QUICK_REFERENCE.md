# Scatter Plot Quick Reference

## What a Scatter Plot Shows

A scatter plot places one numeric variable on the x-axis and another on the y-axis.
Each point is one observation.

Use scatter plots to:

- view relationships between two numeric variables
- detect positive or negative direction
- identify no clear relationship
- find clusters and potential outliers

---

## Interpretation Checklist

1. Direction:
- Upward pattern from left to right -> positive relationship
- Downward pattern from left to right -> negative relationship
- No direction -> no clear relationship

2. Strength:
- Tight cloud around a path -> stronger relationship
- Wide scatter -> weaker relationship

3. Shape:
- Rough straight line -> linear pattern
- Curve or bend -> non-linear pattern

4. Clusters:
- Distinct groups of points may represent subgroups

5. Outliers:
- Isolated points far from the cloud may need investigation

---

## Scatter Plot vs Line Plot

| Plot Type | Best Use | X-axis Meaning |
|-----------|----------|----------------|
| Scatter Plot | Relationship between two numeric variables | Independent numeric scale |
| Line Plot | Change over ordered sequence or time | Ordered values (often dates) |

If order is time and sequence matters, use a line plot.
If relationship between two numeric variables matters, use a scatter plot.

---

## Quick Code Template

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/raw/employee_survey_2026_Q1.csv')

# Choose two numeric columns
x_col = 'work_life_balance'
y_col = 'satisfaction_score'

# Plot
plt.figure(figsize=(9, 6))
plt.scatter(df[x_col], df[y_col], alpha=0.8, s=60, edgecolor='black', linewidth=0.4)
plt.xlabel('Work-Life Balance')
plt.ylabel('Satisfaction Score')
plt.title('Satisfaction vs Work-Life Balance')
plt.show()
```

---

## Good Practices

- Use only numeric variables
- Label axes with clear names
- Add an informative title
- Use transparency for dense points (`alpha=0.6` to `0.9`)
- Compare multiple variable pairs before concluding
- Investigate outliers before removing them

---

## Common Mistakes

- Treating categorical codes as continuous without context
- Assuming causation from a visual trend
- Ignoring outliers that may change interpretation
- Reading too much into tiny or sparse datasets
- Using scatter plots for time-sequence stories where line plots are better

---

## Useful Pair Suggestions (Current Dataset)

- `work_life_balance` vs `satisfaction_score`
- `management_support` vs `satisfaction_score`
- `career_growth` vs `satisfaction_score`
- `team_collaboration` vs `satisfaction_score`
- `work_life_balance` vs `management_support`

---

## One-Minute Summary

A scatter plot is your first relationship check in EDA.
Use it early to decide:

- Is there a pattern worth deeper analysis?
- Are there subgroup clusters?
- Are outliers likely to affect conclusions?
