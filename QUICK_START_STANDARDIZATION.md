# Quick Start Guide - Column Name Standardization

## 🚀 Get Started in 3 Minutes

### Step 1: Run the Demo Script (1 minute)
```bash
cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3
python src/column_name_standardization_demo.py
```

**What you'll see:**
- Complete demonstration of column standardization
- Before/after comparisons
- All concepts explained
- Professional output

---

### Step 2: Try the Interactive Notebook (Optional)
```bash
jupyter notebook notebooks/13_column_name_standardization.ipynb
```

**What to do:**
- Execute each cell in order
- Read the explanations
- Try the practice exercises
- Experiment with the code

---

### Step 3: Record Your Video (2 minutes)

#### **What to Show:**
1. Open and run the demo script
2. Pause and explain each section:
   - Messy column names (show the problem)
   - Standardization function (show the solution)
   - Before/after comparison (show the results)
   - Benefits (explain why it matters)

#### **What to Say:**
```
"I'm demonstrating column name standardization. 
Here's messy data with spaces and special characters.
I apply snake_case convention to clean the names.
Notice how 'Employee ID' becomes 'employee_id'.
This makes code cleaner and prevents errors.
Always standardize early in your workflow!"
```

---

## 📋 Video Recording Checklist

### Before Recording:
- [ ] Close unnecessary applications
- [ ] Open terminal/VS Code
- [ ] Navigate to project directory
- [ ] Test run the script once
- [ ] Know what you'll say

### During Recording:
- [ ] Introduce the topic (15 sec)
- [ ] Run the demo script
- [ ] Explain messy column names (30 sec)
- [ ] Show standardization (45 sec)
- [ ] Compare before/after (20 sec)
- [ ] Wrap up benefits (10 sec)

### After Recording:
- [ ] Check video length (~2 minutes)
- [ ] Verify screen is visible
- [ ] Verify audio is clear
- [ ] Upload to required platform
- [ ] Submit the link

---

## 🎯 Key Points to Mention

### 1. The Problem:
"Column names with spaces and special characters make code messy and error-prone."

### 2. The Solution:
"We standardize using snake_case: lowercase letters with underscores."

### 3. The Process:
"Convert to lowercase, replace spaces, remove special characters."

### 4. The Result:
"Clean, consistent column names that are easy to use in code."

### 5. The Benefit:
"Prevents errors, improves readability, makes datasets reusable."

---

## 💻 Quick Code Reference

### Standardize Column Names:
```python
import pandas as pd
import re

def standardize_column_names(df):
    df_clean = df.copy()
    new_columns = []
    for col in df_clean.columns:
        col_clean = col.lower()
        col_clean = col_clean.replace(' ', '_')
        col_clean = re.sub(r'[^a-z0-9_]', '', col_clean)
        col_clean = re.sub(r'_+', '_', col_clean).strip('_')
        new_columns.append(col_clean)
    df_clean.columns = new_columns
    return df_clean
```

### Use It:
```python
# Load messy data
df = pd.read_csv('data/raw/employee_survey_messy_columns.csv')

# Standardize
df_clean = standardize_column_names(df)

# Compare
print("Before:", df.columns.tolist())
print("After:", df_clean.columns.tolist())
```

---

## 📁 Files You Need

### For Video Walkthrough:
- **Primary:** `src/column_name_standardization_demo.py`
- **Alternative:** `notebooks/13_column_name_standardization.ipynb`

### For Reference:
- **Functions:** `src/column_name_standardization_reference.py`
- **Guide:** `docs/COLUMN_STANDARDIZATION_GUIDE.md`

### For Practice:
- **Sample Data:** `data/raw/employee_survey_messy_columns.csv`

---

## ⚡ Pro Tips

### For Better Video:
1. **Run the script before recording** - Know what to expect
2. **Speak slowly and clearly** - Easier to understand
3. **Point to key parts** - Use your cursor
4. **Pause between sections** - Let concepts sink in
5. **End with a summary** - Reinforce key points

### For Better Code:
1. **Always make a copy** - Don't modify original data
2. **Validate after standardizing** - Check the results
3. **Document transformations** - Comment your code
4. **Test on sample data first** - Avoid surprises
5. **Standardize early** - First step after loading

---

## 🎬 Example Video Script

**INTRO (15 sec)**
```
"Hi! Today I'm demonstrating column name and data format 
standardization - a critical data cleaning step in Pandas."
```

**SHOW PROBLEM (30 sec)**
```
"Here's employee survey data with messy column names. 
Notice spaces, capitals, and special characters like 
parentheses and exclamation marks. These make code 
harder to write and more error-prone."
```

**APPLY SOLUTION (45 sec)**
```
"I'm applying standardization with four rules: convert to 
lowercase, replace spaces with underscores, remove special 
characters, and ensure consistency. Watch as 'Employee ID' 
becomes 'employee_id', 'Work/Life Balance' becomes 
'worklife_balance'. Much cleaner!"
```

**SHOW RESULTS (20 sec)**
```
"Compare before and after. The standardized version is 
professional, consistent, and easy to reference in code. 
This prevents errors when merging datasets or writing 
analysis code."
```

**WRAP UP (10 sec)**
```
"Remember: clean column names lead to clean code. 
Standardize early, standardize always. Thanks!"
```

**Total: ~2 minutes**

---

## 🔍 What Evaluators Look For

### Content:
✅ Demonstrated column name standardization  
✅ Applied snake_case convention  
✅ Standardized data format example  
✅ Showed before/after comparison  
✅ Explained why it matters  

### Technical:
✅ Code runs without errors  
✅ Results are correct  
✅ Concepts are clear  

### Presentation:
✅ Clear audio and video  
✅ Appropriate length (~2 min)  
✅ Well-organized explanation  
✅ Professional delivery  

---

## ❓ FAQ

**Q: Can I write my own code instead of using the demo script?**  
A: Yes! But the demo script covers all requirements and saves time.

**Q: Is 2 minutes a strict limit?**  
A: Approximately 2 minutes. 1:45 - 2:15 is fine.

**Q: What if I make a mistake during recording?**  
A: Re-record! Or use video editing to cut mistakes.

**Q: Can I use the Jupyter notebook for the video?**  
A: Yes! It's more interactive and shows the process well.

**Q: Do I need to show writing the code?**  
A: No. Explaining existing code is fine and faster.

---

## ✅ You're Ready!

### You have:
✅ Complete demonstration script  
✅ Interactive notebook  
✅ Sample messy data  
✅ Quick reference functions  
✅ Comprehensive guide  
✅ Video script examples  
✅ All requirements covered  

### Now:
1. Practice running the demo
2. Record your 2-minute video
3. Submit and move forward!

---

## 🎯 Remember

> **"Standardize early, standardize always!"**

Clean column names = Clean code = Better analysis

**Good luck! 🎬**
