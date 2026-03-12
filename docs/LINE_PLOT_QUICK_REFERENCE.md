# Line Plots for Time Trends - Quick Reference Guide

**Project: Trivin Insight Engine**  
**Topic: Identifying Trends Over Time Using Line Plots**  
**Date: March 12, 2026**

---

## What Is a Line Plot?

A **line plot** shows how a numeric value changes across an ordered timeline.

- **Purpose**: Reveal movement, direction, and pattern over time
- **Use Case**: Time-based data with a date, time, or ordered sequence column
- **Key Insight**: Order matters, so the x-axis must be sorted correctly

---

## When to Use a Line Plot

Use a line plot when:

- You have a **date or time column**
- You want to track a **numeric value over time**
- You need to see **upward, downward, or stable patterns**
- You want to spot **spikes, drops, and volatility**

Do **not** use a line plot when:

- The x-axis is unordered categories
- The order of points does not matter
- Too many separate lines will create clutter

---

## Key Components

### 1. X-Axis: Time
- Examples: dates, months, weeks, timestamps
- Must be sorted in correct chronological order
- Can be regular or irregular intervals

### 2. Y-Axis: Numeric Measure
- Examples: sales, satisfaction score, temperature, revenue
- Should represent one continuous measure

### 3. Connected Points
- Each point is an observed value
- Connecting the points shows how values change over time

### 4. Optional Smoother
- Rolling average or weekly aggregation
- Helps separate long-term direction from short-term noise

---

## What Line Plots Help You See

### Direction
- **Upward trend**: values generally increase over time
- **Downward trend**: values generally decrease over time
- **Stable trend**: values stay in a similar range

### Variability
- **Low volatility**: line changes gradually
- **High volatility**: line jumps up and down often

### Anomalies
- **Spike**: sudden jump upward
- **Drop**: sudden fall downward
- **Gap**: missing period or irregular observation interval

---

## Interpretation Checklist

When reading a line plot, ask:

1. Is the data sorted by time?
2. What is the overall direction?
3. Is the pattern smooth or noisy?
4. Are there sudden spikes or drops?
5. Are there missing periods or irregular intervals?
6. Is the pattern consistent across the whole timeline?

---

## Common Mistakes

| Mistake | Why It Causes Problems | Better Approach |
|---------|------------------------|-----------------|
| Plotting unsorted dates | Creates a misleading line path | Sort by time first |
| Overreacting to one point | One point may be noise | Look for sustained patterns |
| Plotting too many lines | Chart becomes unreadable | Limit comparison lines |
| Ignoring missing intervals | Gaps can affect interpretation | Check date spacing |
| Treating line plots like forecasts | Plot only shows observed data | Keep interpretation descriptive |

---

## Basic Python Pattern

```python
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

csv_path = Path('data/raw/employee_survey_2026_Q1.csv')
df = pd.read_csv(csv_path, parse_dates=['survey_date'])
df = df.sort_values('survey_date')

daily = df.groupby('survey_date', as_index=False)['satisfaction_score'].mean()

plt.figure(figsize=(10, 6))
plt.plot(daily['survey_date'], daily['satisfaction_score'], marker='o')
plt.xlabel('Survey Date')
plt.ylabel('Average Satisfaction Score')
plt.title('Satisfaction Trend Over Time')
plt.tight_layout()
plt.show()
```

---

## Smoothing the Trend

```python
daily['rolling_5_day_avg'] = daily['satisfaction_score'].rolling(window=5, min_periods=1).mean()

plt.figure(figsize=(10, 6))
plt.plot(daily['survey_date'], daily['satisfaction_score'], label='Daily score', alpha=0.5)
plt.plot(daily['survey_date'], daily['rolling_5_day_avg'], label='5-day rolling average', linewidth=2.5)
plt.legend()
plt.show()
```

---

## Best Practices

- Always parse the time column as actual dates
- Always sort by time before plotting
- Label axes clearly
- Use markers when the dataset is small
- Use aggregation or rolling averages to reduce noise
- Limit the number of comparison lines
- Treat spikes and drops as questions to investigate

---

## Quick Summary

A line plot tells the story of how data changes across time.

- **Sort first**
- **Plot one clear metric**
- **Look for direction, noise, and anomalies**
- **Interpret patterns across the whole series, not one point**

---

## Related Project Files

| Resource | Purpose |
|----------|---------|
| `notebooks/17_identifying_trends_over_time_line_plots.ipynb` | Full interactive lesson |
| `src/line_plot_trends_demo.py` | Standalone runnable demo |
| `docs/LINE_PLOT_TRENDS_GUIDE.md` | Detailed explanation |
| `QUICK_START_LINE_PLOTS.md` | Fast start instructions |
