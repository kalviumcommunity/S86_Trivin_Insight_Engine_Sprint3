# Scatter Plot Relationships Guide

## Overview

This guide explains how to explore relationships between numeric variables using scatter plots.
In exploratory data analysis (EDA), scatter plots are often the first tool used to evaluate whether two variables appear related.

This milestone is descriptive, not predictive.
The goal is to observe and interpret patterns, not to run modeling or infer causation.

---

## 1. Why Scatter Plots Matter

Beginners often analyze variables one by one and miss how variables move together.
Scatter plots help you avoid that by making relationships visible.

Scatter plots can reveal:

- positive or negative direction
- strong or weak visual relationships
- linear and non-linear patterns
- clusters of similar observations
- outliers that may influence conclusions

Most relationship-based insight in EDA starts here.

---

## 2. What a Scatter Plot Represents

A scatter plot has:

- x-axis: first numeric variable
- y-axis: second numeric variable
- point: one observation with both values

If a row has values $(x_i, y_i)$, the chart places one point at that coordinate.

For $n$ rows, you get $n$ points.

---

## 3. Choosing Variables

Use scatter plots only for numeric variables.

Good examples in this project:

- `satisfaction_score`
- `work_life_balance`
- `management_support`
- `career_growth`
- `team_collaboration`

Avoid plotting text or category labels directly as numeric values unless they truly represent numeric scale.

---

## 4. Creating a Basic Scatter Plot

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/raw/employee_survey_2026_Q1.csv')

plt.figure(figsize=(9, 6))
plt.scatter(
    df['work_life_balance'],
    df['satisfaction_score'],
    alpha=0.8,
    s=60,
    edgecolor='black',
    linewidth=0.4
)
plt.xlabel('Work-Life Balance')
plt.ylabel('Satisfaction Score')
plt.title('Satisfaction vs Work-Life Balance')
plt.show()
```

Minimal requirements:

1. clear x-axis label
2. clear y-axis label
3. meaningful title
4. readable point style

---

## 5. Interpreting Relationship Direction

### Positive Direction
As x increases, y tends to increase.
Points trend upward from left to right.

### Negative Direction
As x increases, y tends to decrease.
Points trend downward from left to right.

### No Clear Direction
Points form a diffuse cloud with no obvious slope.

Direction is visual evidence of association, not proof of cause.

---

## 6. Interpreting Strength

Strength describes how tightly points follow a visual path.

- Tight grouping around a path: stronger visual relationship
- Wide, diffuse spread: weaker visual relationship

You can treat this as a visual estimate before any formal statistic.

---

## 7. Linear vs Non-Linear Pattern

### Linear Pattern
Points roughly align around a straight line.

### Non-Linear Pattern
Points follow a curve, bend, or segmented shape.

Scatter plots are useful because they reveal non-linearity that summary statistics may hide.

---

## 8. Identifying Clusters

Clusters are groups of points concentrated in separate regions.
They may indicate subgroups (for example, departments) behaving differently.

A practical approach is to color points by a category:

```python
for department in sorted(df['department'].unique()):
    subset = df[df['department'] == department]
    plt.scatter(subset['career_growth'], subset['satisfaction_score'], label=department)
plt.legend()
```

If multiple clusters appear, ask what variable might explain subgroup behavior.

---

## 9. Identifying Outliers

Outliers are points isolated far from the main cloud.
They may represent:

- data entry errors
- unusual but valid cases
- rare subgroup behavior

Never remove outliers automatically.
Use the plot to flag them, then investigate context.

A common initial rule is IQR-based screening per axis:

$$
\text{Lower Bound} = Q_1 - 1.5 \times IQR
$$

$$
\text{Upper Bound} = Q_3 + 1.5 \times IQR
$$

Points beyond either bound on x or y can be flagged for review.

---

## 10. Common Mistakes

1. Assuming correlation means causation
2. Ignoring outliers that change the visual story
3. Drawing strong conclusions from very sparse points
4. Using unlabeled axes
5. Confusing scatter plots with line plots
6. Plotting non-numeric variables as if they were continuous

---

## 11. Suggested Workflow for This Milestone

1. Load dataset into a DataFrame
2. List numeric columns
3. Create 2 to 4 scatter plots for different variable pairs
4. Write short interpretation notes for each plot:
- direction
- strength
- pattern shape
- clusters
- outliers
5. Save at least one figure to `outputs/figures/`
6. Use these observations to guide future analysis decisions

---

## 12. Video Walkthrough Checklist (~2 Minutes)

Your video should show:

1. opening dataset and selecting two numeric columns
2. creating at least one scatter plot
3. explaining direction of relationship
4. describing trend shape, clusters, and any outliers
5. stating why scatter plots are useful in early EDA

Keep the explanation visual and concise.
No modeling or regression is required.

---

## Final Reminder

Scatter plots are a conversation between two variables.
They help you ask better questions before applying deeper statistical tools.
Use them early, interpret them carefully, and avoid causal claims without stronger evidence.
