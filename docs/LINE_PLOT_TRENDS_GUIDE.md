# Line Plot Trends Guide

## Overview

This guide explains how to identify trends over time using line plots. In exploratory data analysis, time adds context that summary statistics alone cannot provide. A line plot helps you see how a numeric value changes across an ordered timeline, making it easier to detect direction, consistency, volatility, and unusual events.

This milestone is descriptive, not predictive. The goal is to understand what happened in the observed data, not to build a forecasting model.

---

## Table of Contents

1. Understanding Time-Based Data
2. Why Sorting Matters
3. Creating Line Plots
4. Interpreting Trends
5. Spotting Spikes, Drops, and Volatility
6. Using Smoothers and Aggregation
7. Comparing a Few Time Series Safely
8. Common Mistakes
9. Best Practices
10. Suggested Workflow

---

## 1. Understanding Time-Based Data

Time-based data contains a column that represents when each observation happened.

Common examples include:

- Daily sales records
- Weekly support tickets
- Monthly revenue
- Survey responses with submission dates
- Sensor readings by timestamp

In this project, the employee survey dataset includes a `survey_date` column. That makes it possible to examine how employee satisfaction changes across the observed period.

### Time Is Not Just Another Column

A time column has structure.

- Earlier observations should appear before later observations
- The order changes the meaning of the chart
- Gaps between observations may matter
- Repeated observations can be aggregated by day, week, or month

If time is treated like an unordered category, the visual can become misleading.

---

## 2. Why Sorting Matters

Sorting by time is the first rule of line-plot analysis.

If dates are not in chronological order, the line will connect points incorrectly. That creates a false visual story, even if the raw values are correct.

### Correct workflow

1. Parse the time column into a datetime type
2. Sort the dataset by that column
3. Group or aggregate if needed
4. Plot the ordered data

### Example

```python
df = pd.read_csv('data/raw/employee_survey_2026_Q1.csv', parse_dates=['survey_date'])
df = df.sort_values('survey_date')
```

Before you plot, it is also useful to inspect interval spacing:

```python
intervals = df['survey_date'].drop_duplicates().diff().dropna().dt.days
print(intervals.value_counts().sort_index())
```

This tells you whether the timeline is regular or if there are gaps.

---

## 3. Creating Line Plots

A line plot needs two things:

- A time column on the x-axis
- A numeric column on the y-axis

### Basic line plot

```python
daily = df.groupby('survey_date', as_index=False)['satisfaction_score'].mean()

plt.figure(figsize=(10, 6))
plt.plot(daily['survey_date'], daily['satisfaction_score'], marker='o', linewidth=2)
plt.xlabel('Survey Date')
plt.ylabel('Average Satisfaction Score')
plt.title('Daily Satisfaction Trend')
plt.tight_layout()
plt.show()
```

This type of chart is useful when you want to see how the measure changes from one point in time to the next.

### Why markers help

When the dataset is small, markers make individual observations easier to see. They also make spikes and drops easier to identify.

---

## 4. Interpreting Trends

Once the line plot is created, read the visual in layers.

### Step 1: Identify the overall direction

Ask whether the line is generally:

- Moving upward
- Moving downward
- Staying in a similar range

A trend does not need to move in one perfect direction. Most real data contains noise.

### Step 2: Separate pattern from noise

Single points can be misleading. The better question is whether multiple neighboring points support the same direction.

For example:

- One sharp drop followed by a rebound may be an isolated event
- Several consecutive lower values may indicate a real decline
- Alternating highs and lows may indicate instability or noise

### Step 3: Look at the full period

Do not summarize a trend from just the first and last point. Use the full line, because the path between those points matters.

---

## 5. Spotting Spikes, Drops, and Volatility

Line plots are especially useful for anomaly detection.

### Spike
A spike is a sudden upward jump.

Possible interpretations:

- A real improvement or one-time event
- Seasonal behavior
- Data collection artifact
- Small-sample randomness

### Drop
A drop is a sudden downward movement.

Possible interpretations:

- A real disruption or issue
- An outlier observation
- A temporary event
- Noise that needs more context

### Volatility
Volatility refers to how sharply values move up and down over time.

- Smooth line: lower volatility
- Jagged line: higher volatility

Volatility matters because it changes how confident you should be in the apparent direction of the trend.

---

## 6. Using Smoothers and Aggregation

Raw daily data can be noisy. Two common ways to make the broader pattern easier to see are rolling averages and resampling.

### Rolling average

A rolling average smooths nearby observations.

```python
daily['rolling_5_day_avg'] = daily['satisfaction_score'].rolling(window=5, min_periods=1).mean()
```

Plot the raw line and the rolling average together:

```python
plt.plot(daily['survey_date'], daily['satisfaction_score'], label='Daily score', alpha=0.5)
plt.plot(daily['survey_date'], daily['rolling_5_day_avg'], label='5-day rolling average', linewidth=2.5)
plt.legend()
plt.show()
```

Use this when you want to reduce short-term fluctuation without losing the sequence.

### Weekly aggregation

Resampling groups observations into larger time buckets.

```python
weekly = df.set_index('survey_date').resample('W')['satisfaction_score'].mean().reset_index()
```

Weekly averages are often easier to describe because they emphasize the higher-level movement instead of daily noise.

---

## 7. Comparing a Few Time Series Safely

You can compare multiple lines on the same chart, but only when the chart remains readable.

### Good use

- Compare two or three departments
- Compare one metric across a few groups
- Compare actual values and a rolling average

### Risky use

- Plotting many categories at once
- Using similar colors with no clear legend
- Showing too many overlapping lines in a small figure

If you need to compare groups, limit the chart to the most relevant lines and label them clearly.

Example:

```python
selected = df[df['department'].isin(['Engineering', 'Marketing', 'Sales'])]
for department in ['Engineering', 'Marketing', 'Sales']:
    subset = selected[selected['department'] == department]
    plt.plot(subset['survey_date'], subset['satisfaction_score'], marker='o', label=department)
plt.legend()
plt.show()
```

This keeps the comparison readable and aligned with the principle of reducing clutter.

---

## 8. Common Mistakes

### Mistake 1: Plotting unsorted time values
This is the most damaging error because it changes the story the line tells.

### Mistake 2: Treating every jump as meaningful
Some changes are noise, especially in small datasets.

### Mistake 3: Ignoring gaps in the timeline
Irregular spacing can affect interpretation.

### Mistake 4: Using too many lines
A cluttered chart hides the trend instead of revealing it.

### Mistake 5: Turning description into prediction
A line plot shows observed behavior. It does not forecast future values by itself.

---

## 9. Best Practices

- Parse dates correctly with `parse_dates`
- Sort by time before plotting
- Choose one clear numeric measure for the y-axis
- Use readable axis labels and titles
- Add markers for small datasets
- Use rolling averages or aggregation when the raw line is noisy
- Limit comparison lines to avoid clutter
- Treat spikes and drops as prompts for investigation
- Describe patterns carefully without overclaiming causes

---

## 10. Suggested Workflow

Use this workflow each time you analyze trends over time:

1. Load the dataset
2. Parse the time column as datetime
3. Sort by time
4. Inspect date range and spacing
5. Create a basic line plot
6. Add a smoother or aggregated view
7. Identify the broad direction
8. Note unusual spikes, drops, or volatile periods
9. Compare a small number of groups if needed
10. Write a short interpretation based on the full pattern

---

## Summary

Line plots help you see how data evolves.

They are one of the clearest ways to answer questions like:

- Is the metric improving or declining?
- Is the pattern stable or noisy?
- When did unusual changes happen?
- Does a smoothed or aggregated view tell the same story?

For this milestone, the important habits are simple:

- respect temporal order
- plot clearly
- interpret patterns over the full timeline
- avoid turning EDA into prediction

---

## Related Project Files

- `notebooks/17_identifying_trends_over_time_line_plots.ipynb`
- `src/line_plot_trends_demo.py`
- `docs/LINE_PLOT_QUICK_REFERENCE.md`
- `QUICK_START_LINE_PLOTS.md`
