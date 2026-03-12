# Line Plot Trends - Quick Start Guide

Get started quickly with the new time-trend milestone.

---

## Option 1: Run the Demo Script

From the project root:

```bash
python src/line_plot_trends_demo.py
```

This will:

- load the survey dataset with `survey_date`
- sort the data by time
- generate line plots in `outputs/figures/`
- print short interpretation notes in the terminal

---

## Option 2: Work Through the Notebook

Open the interactive lesson:

```bash
jupyter notebook notebooks/17_identifying_trends_over_time_line_plots.ipynb
```

Then run the cells in order.

The notebook covers:

- understanding time-based data
- sorting dates correctly
- creating line plots
- smoothing trends with a rolling average
- spotting spikes and drops
- comparing a few department trends without clutter

---

## Files You Need

| Resource | Purpose |
|----------|---------|
| `notebooks/17_identifying_trends_over_time_line_plots.ipynb` | Interactive learning notebook |
| `src/line_plot_trends_demo.py` | Standalone runnable demo |
| `docs/LINE_PLOT_QUICK_REFERENCE.md` | Fast concept lookup |
| `docs/LINE_PLOT_TRENDS_GUIDE.md` | Detailed explanation |
| `data/raw/employee_survey_2026_Q1.csv` | Dataset with `survey_date` |

---

## Core Idea

A line plot shows how a numeric value changes across time.

To do this correctly:

1. Parse the time column as dates
2. Sort the data by time
3. Plot a numeric metric on the y-axis
4. Look for direction, stability, and anomalies

---

## Typical Workflow

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and sort
_df = pd.read_csv('data/raw/employee_survey_2026_Q1.csv', parse_dates=['survey_date'])
_df = _df.sort_values('survey_date')

# Aggregate daily trend
daily = _df.groupby('survey_date', as_index=False)['satisfaction_score'].mean()

# Plot
plt.plot(daily['survey_date'], daily['satisfaction_score'], marker='o')
plt.xlabel('Survey Date')
plt.ylabel('Average Satisfaction Score')
plt.title('Satisfaction Trend Over Time')
plt.show()
```

---

## Common Problems

### Problem: Dates look unordered
Sort by the date column before plotting.

### Problem: The line is too noisy
Add a rolling average or resample weekly.

### Problem: The chart is cluttered
Plot fewer lines or focus on one metric at a time.

### Problem: You want to explain one spike
Use the chart to raise a question, not to assume a cause.

---

## Expected Outputs

The demo script saves these figures in `outputs/figures/`:

- `line_plot_daily_satisfaction.png`
- `line_plot_rolling_average_satisfaction.png`
- `line_plot_weekly_satisfaction.png`
- `line_plot_department_comparison.png`

---

## Next Step

Start with the notebook if you want the teaching version.
Start with the script if you want the fastest runnable example.
