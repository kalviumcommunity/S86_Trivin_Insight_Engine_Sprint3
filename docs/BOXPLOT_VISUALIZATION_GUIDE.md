# Boxplot Visualization Guide

## Overview

This guide provides comprehensive documentation for the Boxplot Visualization milestone. Boxplots are essential tools for exploratory data analysis (EDA), enabling quick visual assessment of data distributions, identification of outliers, and comparison across multiple columns or groups.

## Table of Contents

1. [Understanding Boxplots](#understanding-boxplots)
2. [Components of a Boxplot](#components-of-a-boxplot)
3. [Creating Boxplots](#creating-boxplots)
4. [Interpreting Boxplots](#interpreting-boxplots)
5. [Comparing Distributions](#comparing-distributions)
6. [Outlier Detection and Handling](#outlier-detection-and-handling)
7. [Common Mistakes](#common-mistakes)
8. [Best Practices](#best-practices)
9. [When to Use Boxplots](#when-to-use-boxplots)

---

## Understanding Boxplots

### What is a Boxplot?

A **boxplot** (also called a **box-and-whisker plot**) is a standardized way of displaying the distribution of a dataset based on five summary statistics:

- **Minimum** (or lower whisker)
- **Q1** (25th percentile)
- **Median** (50th percentile)
- **Q3** (75th percentile)
- **Maximum** (or upper whisker)
- **Outliers** (individual points beyond whiskers)

### Why Use Boxplots?

| Advantage | Explanation |
|-----------|-------------|
| **Compact Summary** | Summarize a distribution in a single, easy-to-read visualization |
| **Outlier Detection** | Automatically highlight potential outliers visually |
| **Comparison** | Compare distributions across multiple columns or groups side-by-side |
| **Complementary** | Work well with histograms to provide different insights |
| **Statistical Context** | Show quartiles and spread more clearly than descriptive statistics alone |
| **Stakeholder Communication** | Easy for non-technical audiences to understand |

---

## Components of a Boxplot

### Visual Structure

```
        Outlier (●)
           │
           ●
           │
    ───────┼──────────  Upper Whisker (Q3 + 1.5×IQR)
           │
       ┌───┼───┐
       │   │   │  ───  Upper Quartile (Q3)
       │   │   │
       │ ─ ┼ ─ │  ───  Median
       │   │   │
       │   │   │  ───  Lower Quartile (Q1)
       └───┼───┘
           │
    ───────┼──────────  Lower Whisker (Q1 - 1.5×IQR)
           │
           ●
           │
        Outlier (●)
```

### Key Statistics

#### **Median (Q2)**
- The 50th percentile: 50% of data is below, 50% is above
- Represents the center of the distribution
- **Shown as:** A line in the middle of the box (usually in red)

#### **Quartiles**
- **Q1 (First Quartile, 25th percentile):** 25% of data is below this value
- **Q3 (Third Quartile, 75th percentile):** 75% of data is below this value
- **Together:** Define the box, showing the middle 50% of the data

#### **Interquartile Range (IQR)**
- Calculated as: IQR = Q3 - Q1
- Represents the spread of the middle 50% of data
- Wider box = more variable data in the middle 50%

#### **Whiskers**
- Lines extending from the box to show the full range of typical data
- **Lower whisker:** Q1 - 1.5 × IQR (or minimum if higher)
- **Upper whisker:** Q3 + 1.5 × IQR (or maximum if lower)
- Any data beyond whiskers are plotted as individual **outliers** (points)

#### **Outliers**
- Individual data points beyond the whisker boundaries
- Calculated as: Q1 - 1.5×IQR < Outlier or Outlier > Q3 + 1.5×IQR
- **Shown as:** Individual dots or symbols beyond the whiskers

---

## Creating Boxplots

### Using Matplotlib (Basic)

```python
import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Create a single boxplot
fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(df['column_name'])
ax.set_ylabel('Value')
ax.set_title('Distribution of Column Name')
plt.show()
```

### Using Matplotlib (Customized)

```python
fig, ax = plt.subplots(figsize=(8, 6))

bp = ax.boxplot(df['column_name'], vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='darkblue'),
                whiskerprops=dict(color='darkblue'),
                capprops=dict(color='darkblue'),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', markerfacecolor='red', alpha=0.6))

ax.set_ylabel('Value', fontsize=11)
ax.set_title('Distribution of Satisfaction Scores', fontsize=13)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

### Multiple Boxplots for Comparison

```python
# Compare multiple columns
columns = ['satisfaction_score', 'work_life_balance', 'career_growth']
fig, ax = plt.subplots(figsize=(10, 6))

data_to_plot = [df[col] for col in columns]
bp = ax.boxplot(data_to_plot, labels=columns, patch_artist=True)

# Color the boxes
colors = ['lightblue', 'lightgreen', 'lightyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_ylabel('Score')
ax.set_title('Comparison of Metrics')
plt.xticks(rotation=45, ha='right')
plt.show()
```

### Grouped Boxplots

```python
# Compare metric across groups (departments)
fig, ax = plt.subplots(figsize=(10, 6))

departments = sorted(df['department'].unique())
data_by_dept = [df[df['department'] == dept]['satisfaction_score'].values 
                for dept in departments]

bp = ax.boxplot(data_by_dept, labels=departments, patch_artist=True)

# Customize colors
for patch in bp['boxes']:
    patch.set_facecolor('lightblue')

ax.set_xlabel('Department')
ax.set_ylabel('Satisfaction Score')
ax.set_title('Satisfaction by Department')
plt.xticks(rotation=45)
plt.show()
```

### Using the Reference Class

```python
from boxplot_visualization_reference import BoxplotAnalyzer

# Initialize analyzer
analyzer = BoxplotAnalyzer(df)

# Create a single boxplot
analyzer.create_single_boxplot('satisfaction_score', 
                               title='Employee Satisfaction')

# Create comparison boxplots
analyzer.create_comparison_boxplots(
    ['satisfaction_score', 'work_life_balance', 'career_growth'],
    title='Comparison of All Metrics'
)

# Create grouped boxplots
analyzer.create_grouped_boxplots('department', 'satisfaction_score',
                                 title='Satisfaction by Department')

# Get statistical summary
analyzer.print_statistical_summary('satisfaction_score')
```

---

## Interpreting Boxplots

### Reading the Box

1. **Locate the median line** (usually red)
   - If median is centered in the box → Distribution is fairly symmetric
   - If median is off to one side → Distribution is skewed

2. **Examine the box size**
   - Larger box = more spread in the middle 50% of data
   - Smaller box = more concentrated middle 50%

3. **Compare box to whiskers**
   - If box is small but whiskers are long → Most data is concentrated with some spread
   - If box and whiskers are balanced → Distribution is relatively uniform

### Identifying Patterns

#### **Symmetric Distribution**
- Median near center of box
- Box roughly equal above and below median
- Whiskers roughly equal length
- Few or no outliers

#### **Right-Skewed Distribution**
- Median closer to bottom of box
- Longer upper whisker
- Outliers on the right side
- Example: Income distribution (few very high earners)

#### **Left-Skewed Distribution**
- Median closer to top of box
- Longer lower whisker
- Outliers on the left side
- Example: Test scores (few very low performers)

#### **Wide Spread**
- Large box (large IQR)
- Long whiskers
- Many outliers (possibly)
- Indicates high variability

#### **Narrow Spread**
- Small box (small IQR)
- Short whiskers
- Few or no outliers
- Indicates consistency

### Comparison Insights

When comparing multiple boxplots:

- **Higher median:** Higher central value
- **Wider box:** More variability in middle 50%
- **Longer whiskers:** Wider overall range
- **More outliers:** More extreme values

---

## Comparing Distributions

### Side-by-Side Comparison

**What to Look For:**
1. Do medians differ significantly?
2. Which has the widest spread (largest box)?
3. How many outliers does each have?
4. Are the distributions similar in shape?

### Example Analysis

```
Metric                        Analysis
────────────────────────────────────────────────────────────────
Satisfaction Score            Median: 6, Box: [4,8], Some outliers
Work-Life Balance             Median: 7, Box: [6,8], Few outliers
Career Growth                 Median: 5, Box: [3,6], Many outliers

Interpretation:
- Most variables have different median values
- Work-life balance appears most consistent (smallest box)
- Career growth shows the most variability (largest box, more outliers)
```

### Questions to Ask

1. Are the distributions clustered or spread out?
2. Do they overlap significantly or are they distinct?
3. Which groups/columns are most similar?
4. Which stand out as different?
5. Are there patterns in the outliers?

---

## Outlier Detection and Handling

### What Are Outliers?

Outliers are values that fall outside the expected range based on the distribution:
- **Lower bound:** Q1 - 1.5 × IQR
- **Upper bound:** Q3 + 1.5 × IQR

Any value beyond these bounds is marked as an outlier and shown as an individual point.

### Detecting Outliers

```python
from boxplot_visualization_reference import BoxplotAnalyzer

analyzer = BoxplotAnalyzer(df)

# Find outliers in a column
outliers, lower_bound, upper_bound = analyzer.find_outliers('satisfaction_score')

print(f"Lower bound: {lower_bound:.2f}")
print(f"Upper bound: {upper_bound:.2f}")
print(f"Number of outliers: {len(outliers)}")
print(f"\nOutlier records:")
print(outliers)
```

### What Outliers ARE (Not)

| What They ARE | What They Aren't |
|---------------|-----------------|
| Statistically unusual | Automatically errors |
| Worth investigating | Always wrong |
| Potentially informative | Always to be removed |
| Extreme values | Necessarily bad data |

### Decision Framework: Keep or Remove?

| Scenario | Decision | Reason |
|----------|----------|--------|
| Data entry error (e.g., 99 vs 9) | **Correct/Remove** | Clear mistake; fix the data |
| Legitimate extreme value | **Keep & Analyze** | Valid data with insights |
| Different subgroup (different department) | **Keep & Analyze by Group** | Outlier may be normal within subgroup |
| Measurement error | **Document & Remove** | Unreliable data |
| You don't understand it | **INVESTIGATE FIRST** | Never remove blindly |

### Investigation Questions

Before removing an outlier, ask:

1. **Is it possible?** Could this value exist in reality?
2. **Is it plausible?** Does it fit the domain context?
3. **Is it consistent?** Do other variables support this value?
4. **Is it informative?** Does it reveal something important?
5. **Is it an error?** Is there evidence of data quality problems?

### Documentation

Always document your decisions:

```
Outlier Handling Log:

Column: satisfaction_score
Outlier: Employee ID 1234 with score 10

Investigation:
- Review survey response: "Excellent work culture and innovative projects"
- Check other metrics: All high scores (work_life_balance=9, team_collaboration=10)
- Check role: Senior Engineer, high performer
- Check duration: 5-year tenure

Decision: KEEP
Reason: Legitimate extreme satisfaction, not an error. Employee appears genuinely 
satisfied across all dimensions. Important for understanding high engagement drivers.
```

---

## Common Mistakes

### ❌ **Mistake 1: Removing Outliers Without Investigation**

**Problem:** Automatically deleting outliers before understanding them.

**Why It's Wrong:**
- May lose valuable insights
- Could remove the most interesting data
- Violates scientific integrity

**Fix:** Always investigate outliers first. Document your reasoning.

---

### ❌ **Mistake 2: Using Only Averages**

**Problem:** Relying on mean/median without looking at spread.

**Why It's Wrong:**
- Two datasets with same mean can have very different distributions
- Hides variability and outliers
- Ignores important patterns

**Example:**
```
Dataset A: [1, 2, 3, 4, 5]     Mean = 3, Spread is small
Dataset B: [0, 0, 3, 6, 6]     Mean = 3, Spread is large
```

**Fix:** Always create boxplots alongside summary statistics.

---

### ❌ **Mistake 3: Ignoring Scale Differences**

**Problem:** Comparing columns with different units or ranges.

**Why It's Wrong:**
- A score 0-10 looks different next to a score 0-100
- Prevents meaningful visual comparison

**Fix:** Either normalize the data or use separate axes for different metrics.

---

### ❌ **Mistake 4: Not Documenting Decisions**

**Problem:** Making changes without recording why.

**Why It's Wrong:**
- Others (or your future self) won't understand the logic
- Choices appear arbitrary
- Hard to justify or reproduce

**Fix:** Keep a documented log of all data cleaning decisions.

---

### ❌ **Mistake 5: Assuming Shape = Quality**

**Problem:** Thinking skewed or wide distributions mean bad data.

**Why It's Wrong:**
- Natural variation is normal
- Skew can reflect real patterns
- Wide spread may be appropriate

**Fix:** Understand your domain. Not all data should be normally distributed.

---

## Best Practices

### 1. **Create Multiple Views**

Don't stop at one boxplot:
- Create boxplots for each numeric column
- Create comparison boxplots across columns
- Create grouped boxplots by categories
- Create before/after boxplots for data cleaning decisions

### 2. **Pair with Other Visualizations**

Use boxplots alongside:
- **Histograms:** Show the full frequency distribution
- **Statistics tables:** Show exact values
- **Scatter plots:** Show individual data points
- **Time series plots:** Show trends over time

### 3. **Customize for Clarity**

Make your boxplots easy to understand:
- Use meaningful titles: "Satisfaction Scores by Department" (not "Boxplot #1")
- Label axes clearly: "Satisfaction Score (1-10)" not just "Score"
- Use colors strategically to group related boxes
- Make text large enough to read
- Add gridlines for easier value reading

### 4. **Investigate Before Deciding**

For anything unusual:
- Count the outliers: How many are there?
- Examine them: What values are they?
- Understand the context: Why might they be there?
- Check other variables: Do they support the pattern?

### 5. **Document Your Workflow**

Record:
- Why you created each visualization
- What you discovered
- What decisions you made and why
- How the data changed after cleaning

### 6. **Size Your Figures Appropriately**

```python
# Single boxplot: 8x6 inches
fig, ax = plt.subplots(figsize=(8, 6))

# Compare 5 columns: 12x6 inches
fig, ax = plt.subplots(figsize=(12, 6))

# Compare 10 groups: 14x8 inches
fig, ax = plt.subplots(figsize=(14, 8))
```

### 7. **Save Figures Properly**

```python
# Save with high quality
plt.savefig('boxplot_analysis.png', dpi=300, bbox_inches='tight')

# Add descriptive filenames
# Good: 02_satisfaction_by_department_boxplots.png
# Bad: boxplot1.png
```

---

## When to Use Boxplots

### ✅ **Use Boxplots For:**

1. **Early EDA (Exploratory Data Analysis)**
   - Get a quick visual overview of distributions
   - Spot potential issues or outliers

2. **Comparing Multiple Distributions**
   - Side-by-side metric comparison
   - Distribution comparison across groups

3. **Identifying Outliers**
   - Visual outlier detection
   - Understanding which values are extreme

4. **Communicating with Non-Technical Stakeholders**
   - Easy to understand visualization
   - Clear visual representation of spread

5. **Assessing Data Quality**
   - Spot data entry errors (impossible values)
   - Identify suspicious patterns

6. **Preparing for Statistical Tests**
   - Check assumptions about normality
   - Assess variance homogeneity

### ❌ **Don't Use Boxplots For:**

1. **Very Small Datasets** (< 5 values)
   - Quartiles may not be meaningful

2. **Heavily Discrete Data** (many identical values)
   - Limited utility; use bar charts instead

3. **Time Series Data** (over time)
   - Use line plots to show temporal patterns

4. **Categorical Data**
   - Use bar charts or other categorical plots

5. **Identifying Specific Patterns**
   - Use histograms for shape, scatter plots for relationships

---

## Summary

### Key Takeaways

✅ **Boxplots summarize distributions in a compact, visual format**

✅ **They excel at comparing multiple distributions side-by-side**

✅ **Outliers are highlighted and deserve investigation (not automatic removal)**

✅ **Quartiles and IQR show spread more clearly than summary statistics alone**

✅ **Use boxplots early in EDA to understand your data**

### Workflow

1. **Load your data**
2. **Create initial boxplots** for all numeric columns
3. **Identify** potential outliers and issues
4. **Investigate** anything unexpected
5. **Document** your findings and decisions
6. **Iterate** with grouped or comparison boxplots as needed

---

## Resources

- **Jupyter Notebook:** `15_visualizing_data_distributions_boxplots.ipynb`
- **Python Reference:** `src/boxplot_visualization_reference.py`
- **Data:** `data/raw/employee_survey_2026_Q1.csv`
- **Output:** Saved figures in `outputs/figures/`

---

## Questions for Self-Assessment

By the end of this module, you should be able to answer:

1. ✓ What does the median line in a boxplot represent?
2. ✓ What is IQR and why does it matter?
3. ✓ How are the whiskers calculated?
4. ✓ What makes a value an outlier?
5. ✓ How do you compare distributions using boxplots?
6. ✓ When should you keep vs. remove outliers?
7. ✓ How do you create boxplots in Python?
8. ✓ What insights can you draw from a boxplot?

---

**Last Updated:** March 12, 2026
**Author:** Data Science Team
**Version:** 1.0
