# Histogram Visualization - Quick Start Guide

**Get started in 5 minutes! 🚀**

---

## Option 1: Quick Automated Run (Fastest)

**Generate all visualizations instantly:**

```bash
cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3
python src/histogram_visualization_auto.py
```

**Result**: 6 histograms saved to `outputs/figures/` in ~2 seconds!

---

## Option 2: Interactive Notebook (Best for Learning)

**Step-by-step learning experience:**

1. **Open Jupyter:**
   ```bash
   cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3
   jupyter notebook notebooks/16_histogram_visualization.ipynb
   ```

2. **Run cells sequentially** (Shift + Enter)

3. **Complete practice exercises** in Part 8

---

## Option 3: Quick Python Script

**Run this 10-line script to see your first histogram:**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/processed/employee_survey_cleaned_2026_Q1.csv')

# Create histogram
plt.hist(df['satisfaction_score'], bins=10, color='steelblue', edgecolor='black')
plt.xlabel('Satisfaction Score')
plt.ylabel('Frequency')
plt.title('Distribution of Satisfaction Scores')
plt.show()
```

Save as `quick_histogram.py` and run:
```bash
python quick_histogram.py
```

---

## What You Need

### Prerequisites
- ✅ Python 3.7+ installed
- ✅ Pandas installed: `pip install pandas`
- ✅ Matplotlib installed: `pip install matplotlib`

### Optional (for notebook)
- Jupyter Notebook: `pip install jupyter`

### Quick Install All
```bash
pip install pandas matplotlib jupyter
```

---

## File Locations

| What You Need | Where to Find It |
|---------------|------------------|
| **Learning notebook** | `notebooks/16_histogram_visualization.ipynb` |
| **Quick reference** | `docs/HISTOGRAM_QUICK_REFERENCE.md` |
| **Video script** | `docs/HISTOGRAM_VIDEO_GUIDE.md` |
| **Auto-generate script** | `src/histogram_visualization_auto.py` |
| **Dataset** | `data/processed/employee_survey_cleaned_2026_Q1.csv` |
| **Output folder** | `outputs/figures/` |

---

## 5-Minute Learning Path

**Want to master histograms in 5 minutes?**

1. **Minute 1**: Read "What is a Histogram?" in `docs/HISTOGRAM_QUICK_REFERENCE.md`
2. **Minute 2**: Run `python src/histogram_visualization_auto.py`
3. **Minute 3**: Open `satisfaction_score_histogram.png` and interpret it
4. **Minute 4**: Open `histogram_comparison_grid.png` - compare distributions
5. **Minute 5**: Try creating one yourself (see Option 3 above)

---

## Video Recording (Required)

**When you're ready to record your 2-minute video:**

1. Review `docs/HISTOGRAM_VIDEO_GUIDE.md`
2. Prepare the code you'll demonstrate
3. Set zoom to 125-150% for visibility
4. Record using:
   - Windows: Xbox Game Bar (Win + G)
   - Mac: QuickTime
   - Cross-platform: OBS Studio

**What to show**:
- Create a histogram
- Explain bins and frequencies
- Interpret the distribution shape
- Optional: Compare two columns

---

## Common Issues & Solutions

### Issue: "Module not found: pandas"
**Solution**: `pip install pandas matplotlib`

### Issue: "File not found" error
**Solution**: Make sure you're in the project root directory:
```bash
cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3
```

### Issue: Plots not showing
**Solution**: 
- In Jupyter: Add `%matplotlib inline` at the top
- In scripts: Make sure you have `plt.show()` after plotting

### Issue: Can't open Jupyter notebook
**Solution**: Install Jupyter: `pip install jupyter`

---

## Next Steps After Quick Start

- [ ] Run automated script to see all examples
- [ ] Open and review all generated figures
- [ ] Work through the interactive notebook
- [ ] Complete the practice exercise
- [ ] Record your 2-minute video
- [ ] Submit your work

---

## Key Concepts (30-Second Summary)

**Histogram**: Shows how numeric data is distributed
- **Bins**: Group values into ranges
- **Frequency**: Height of bars = count of values
- **Shape**: Normal, skewed, uniform, bimodal
- **Skewness**: Compare mean and median
- **Outliers**: Isolated bars in extreme ranges

**Best Practice**: Always label axes and choose 10-20 bins

---

## Example Output Preview

Your histograms will look like this:

```
Frequency
   ↑
   |     ▄▄▄
   |    ▄███▄
   |   ▄█████▄
   |  ▄███████▄
   | ▄█████████▄
   └──────────────→ Satisfaction Score
```

(See actual PNG files in `outputs/figures/` after running scripts)

---

## Cheat Sheet

### Create Basic Histogram
```python
plt.hist(data, bins=10, color='steelblue', edgecolor='black')
plt.xlabel('Variable')
plt.ylabel('Frequency')
plt.title('Distribution')
plt.show()
```

### Add Mean Line
```python
mean_val = data.mean()
plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
plt.legend()
```

### Compare Columns
```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, col in zip(axes, columns):
    ax.hist(df[col], bins=10)
    ax.set_title(col)
plt.tight_layout()
plt.show()
```

### Save Figure
```python
plt.savefig('my_histogram.png', dpi=300, bbox_inches='tight')
```

---

## Resources at a Glance

| Resource | Purpose | Time |
|----------|---------|------|
| **Quick Start** (this file) | Get running in 5 min | 5 min |
| **Quick Reference** | Comprehensive guide | 15 min |
| **Interactive Notebook** | Step-by-step learning | 45 min |
| **Video Guide** | Recording instructions | 10 min |
| **Auto Script** | Generate all figures | 2 min |

---

## Checklist for Completion

**Before starting**:
- [ ] Python and packages installed
- [ ] Project folder accessible
- [ ] Dataset present in data/processed/

**Learning**:
- [ ] Understand what histograms are
- [ ] Can create basic histogram
- [ ] Can interpret distribution shapes
- [ ] Can identify skewness
- [ ] Can detect outliers

**Deliverables**:
- [ ] Generated at least 3 histograms
- [ ] Labeled all axes properly
- [ ] Can explain your visualizations
- [ ] Recorded 2-minute video
- [ ] Submitted work

---

## Help & Support

**Questions?**
1. Check `docs/HISTOGRAM_QUICK_REFERENCE.md` FAQ section
2. Review notebook markdown cells for explanations
3. Look at example code in `src/histogram_visualization_auto.py`

**Still stuck?**
- Verify all files are in correct locations
- Check Python version: `python --version` (should be 3.7+)
- Reinstall packages: `pip install --upgrade pandas matplotlib`

---

## Time Estimate

| Activity | Time |
|----------|------|
| Quick automated run | 2 min |
| Review generated figures | 10 min |
| Work through notebook | 45 min |
| Complete practice | 20 min |
| Record video | 30 min |
| **Total** | **~2 hours** |

---

## Success Criteria

You've successfully completed this milestone when you can:

✅ Create a histogram for numeric data  
✅ Interpret what the distribution shows  
✅ Identify if it's skewed or symmetric  
✅ Spot potential outliers  
✅ Compare multiple distributions  
✅ Explain your findings clearly (video)

---

**Ready to begin? Start with Option 1 (automated run) to see examples, then move to Option 2 (notebook) for hands-on learning!**

🚀 **Let's visualize some data distributions!**
