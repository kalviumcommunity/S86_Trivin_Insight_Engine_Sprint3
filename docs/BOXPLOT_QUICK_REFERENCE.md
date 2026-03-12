# Boxplot Visualization - Quick Reference Guide

## 🎯 What is a Boxplot?

A boxplot shows how data is distributed using quartiles, making it easy to spot outliers and compare multiple distributions at a glance.

**Key Components:**
```
Outlier (●)
    │
    ●
    │
────┼────────  Upper Whisker = Q3 + 1.5×IQR
    │
┌───┼───┐
│   │   │  ─── Upper Quartile (Q3, 75th percentile)
│   │   │
│ ─ ┼ ─ │  ─── Median (50th percentile)
│   │   │
│   │   │  ─── Lower Quartile (Q1, 25th percentile)
└───┼───┘
    │
────┼────────  Lower Whisker = Q1 - 1.5×IQR
    │
    ●
    │
Outlier (●)
```

---

## 🚀 Quick Start

### Single Boxplot
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(df['column'])
ax.set_title('Distribution Title')
ax.set_ylabel('Value')
plt.show()
```

### Compare Multiple Columns
```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.boxplot([df['col1'], df['col2'], df['col3']], 
           labels=['Col1', 'Col2', 'Col3'])
plt.xticks(rotation=45)
plt.show()
```

### Compare Across Groups
```python
fig, ax = plt.subplots(figsize=(10, 6))
groups = sorted(df['group'].unique())
data = [df[df['group']==g]['value'].values for g in groups]
ax.boxplot(data, labels=groups)
ax.set_xlabel('Group')
ax.set_ylabel('Value')
plt.show()
```

---

## 📊 Key Statistics Explained

| Statistic | What It Means | Formula |
|-----------|--------------|---------|
| **Q1** | 25% of data below this | 25th percentile |
| **Median** | Center of data | 50th percentile |
| **Q3** | 75% of data below this | 75th percentile |
| **IQR** | Spread of middle 50% | Q3 - Q1 |
| **Lower Whisker** | Typical minimum | Q1 - 1.5×IQR |
| **Upper Whisker** | Typical maximum | Q3 + 1.5×IQR |
| **Outliers** | Extreme values | Beyond whiskers |

---

## 📈 Interpretation Cheat Sheet

### Read the Box Position
```
├─ Median at BOTTOM  → Right-skewed (long upper tail)
├─ Median in MIDDLE  → Symmetric
└─ Median at TOP     → Left-skewed (long lower tail)
```

### Compare Spreads
```
├─ Large box  → High variability
├─ Small box  → Low variability
└─ Long whiskers → Wide overall range
```

### Check for Outliers
```
├─ None visible → Consistent data
├─ Few outliers → Mostly normal with some extreme values
└─ Many outliers → Very variable data (investigate!)
```

---

## 🔍 Finding Outliers

```python
# Manual calculation
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['column'] < lower) | (df['column'] > upper)]

# Using reference class
from boxplot_visualization_reference import BoxplotAnalyzer
analyzer = BoxplotAnalyzer(df)
outliers, lower, upper = analyzer.find_outliers('column')
```

---

## ⚖️ Should I Keep or Remove This Outlier?

```
┌─────────────────────────┬──────────────┬────────────────────┐
│ Type of Outlier         │ Decision     │ Why                │
├─────────────────────────┼──────────────┼────────────────────┤
│ Data entry error        │ REMOVE       │ Clear mistake      │
│ (e.g., 99 instead of 9) │              │                    │
├─────────────────────────┼──────────────┼────────────────────┤
│ Legitimate extreme      │ KEEP         │ Valid data =       │
│ (e.g., CEO salary)      │              │ insights           │
├─────────────────────────┼──────────────┼────────────────────┤
│ Different subgroup      │ KEEP &       │ Normal for that    │
│ (e.g., new dept)        │ ANALYZE      │ group              │
├─────────────────────────┼──────────────┼────────────────────┤
│ You don't understand    │ INVESTIGATE  │ ALWAYS investigate │
│                         │ FIRST        │ before removing    │
└─────────────────────────┴──────────────┴────────────────────┘
```

---

## 🎨 Customization Snippets

### Style the Boxplot
```python
bp = ax.boxplot(data, patch_artist=True,
    boxprops=dict(facecolor='lightblue'),
    medianprops=dict(color='red', linewidth=2),
    whiskerprops=dict(color='darkblue'),
    flierprops=dict(marker='o', markerfacecolor='red'))
```

### Add Colors to Multiple Boxes
```python
colors = plt.cm.Set3(np.linspace(0, 1, len(columns)))
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
```

### Save High-Quality Figure
```python
plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')
```

---

## ❌ Common Mistakes & Fixes

| Mistake | Fix |
|---------|-----|
| Removing outliers without checking | Investigate first, document decisions |
| Only using mean/median | Create boxplots to see spread |
| Comparing metrics with different scales | Normalize or use separate axes |
| Not documenting changes | Keep a log of all data decisions |
| One visualization is enough | Create multiple views (single, compare, grouped) |

---

## ✅ Best Practices Checklist

- [ ] Explore all numeric columns individually
- [ ] Create comparison boxplots for related metrics
- [ ] Create grouped boxplots by important categories
- [ ] Investigate all outliers (ask "why?")
- [ ] Document outlier handling decisions
- [ ] Use meaningful titles and axis labels
- [ ] Save figures in high quality with descriptive names
- [ ] Pair boxplots with summary statistics
- [ ] Don't remove data without good reason

---

## 🔗 Related Resources

| Resource | Purpose |
|----------|---------|
| `15_visualizing_data_distributions_boxplots.ipynb` | Full interactive tutorial |
| `boxplot_visualization_reference.py` | Reusable Python functions |
| `BOXPLOT_VISUALIZATION_GUIDE.md` | Comprehensive reference |
| This file | Quick lookup |

---

## 📋 Workflow Template

```python
# 1. Setup
import pandas as pd
import matplotlib.pyplot as plt
from boxplot_visualization_reference import BoxplotAnalyzer

df = pd.read_csv('data.csv')
analyzer = BoxplotAnalyzer(df)

# 2. Explore
analyzer.create_single_boxplot('metric1')
analyzer.create_single_boxplot('metric2')

# 3. Compare
analyzer.create_comparison_boxflots(['metric1', 'metric2', 'metric3'])

# 4. Analyze by Group
analyzer.create_grouped_boxplots('category', 'metric')

# 5. Investigate Outliers
outliers, lower, upper = analyzer.find_outliers('metric')
print(f"Found {len(outliers)} outliers")
print(outliers)

# 6. Summary
analyzer.print_statistical_summary('metric')
```

---

## Quick Answers

**Q: Why is my median off-center?**
A: Your data is skewed. Look at where the median is to understand if it's right-skewed (median lower) or left-skewed (median higher).

**Q: Should I remove these outliers?**
A: Investigate first! Is it an error? Is it plausible? Does it tell you something? Only remove after understanding.

**Q: How many outliers is normal?**
A: For normally distributed data, ~0.7%. For skewed data, more is expected. Check your domain.

**Q: Can I compare boxplots on different scales?**
A: Not directly. Either normalize the data or use separate subplots with labeled axes.

**Q: Why use boxplots instead of just histograms?**
A: Boxplots show quartiles and outliers clearly. Histograms show shape. Use both!

---

**Keep this handy for quick reference while analyzing data.** 📊
