# Column Name and Data Format Standardization Guide

## Overview

This guide covers the learning unit on standardizing column names and data formats in Pandas DataFrames - a critical step in data preparation.

**Duration:** ~2 minutes video walkthrough  
**Difficulty:** Beginner to Intermediate  
**Prerequisites:** Basic Pandas knowledge, CSV loading

---

## Learning Objectives

By completing this milestone, you will be able to:

- ✅ Convert column names to a consistent format
- ✅ Remove spaces and special characters from column names
- ✅ Apply predictable naming conventions (snake_case)
- ✅ Standardize simple data formats across columns
- ✅ Improve dataset usability and readability

---

## Why This Matters

### Common Problems:
- ❌ Column names with spaces (`'Employee ID'`)
- ❌ Mixed casing (`'Department Name'`, `'department_name'`)
- ❌ Special characters (`'Work/Life Balance'`, `'Salary ($)'`)
- ❌ Inconsistent naming across datasets
- ❌ Errors when merging or referencing columns

### Benefits of Standardization:
- ✅ Easier code: `df['employee_id']` vs `df['Employee ID']`
- ✅ No errors from spaces or special characters
- ✅ Cleaner merges and joins
- ✅ Better autocomplete in IDEs
- ✅ More professional and maintainable code
- ✅ Datasets are easier to reuse

---

## Files Provided

### Python Scripts:
1. **`src/column_name_standardization_demo.py`**
   - Complete demonstration script
   - Designed for 2-minute video walkthrough
   - Includes all required concepts
   - Ready to run and explain

2. **`src/column_name_standardization_reference.py`**
   - Quick reference guide
   - Reusable functions
   - Examples and best practices
   - Keep open while coding

### Jupyter Notebooks:
1. **`notebooks/13_column_name_standardization.ipynb`**
   - Interactive learning experience
   - Step-by-step explanations
   - Practice exercises
   - Cell-by-cell execution

### Sample Data:
1. **`data/raw/employee_survey_messy_columns.csv`**
   - Sample dataset with messy column names
   - Use for practice and demonstration
   - Shows real-world data issues

2. **`data/raw/employee_survey_2026_Q1.csv`**
   - Clean dataset example
   - Shows what standardized data should look like

---

## Video Walkthrough Requirements

### Duration: ~2 Minutes

### Required Content:

#### 1. **Introduction (15 seconds)**
   - Explain what standardization is
   - Why it matters for data analysis
   - Quick overview of what you'll demonstrate

#### 2. **Column Name Standardization (45 seconds)**
   - Show messy column names
   - Identify specific issues (spaces, capitals, special chars)
   - Apply standardization function
   - Show before/after comparison
   - Explain the transformation

#### 3. **Data Format Standardization (30 seconds)**
   - Show inconsistent text data
   - Demonstrate text standardization
   - Show the cleaned result
   - Explain the benefits

#### 4. **Real-World Application (20 seconds)**
   - Apply to a real dataset
   - Show how it improves code
   - Demonstrate easier column access

#### 5. **Wrap-up (10 seconds)**
   - Summarize key takeaways
   - Emphasize "standardize early, always"
   - Mention best practices

---

## Step-by-Step Video Guide

### Before Recording:
1. ✅ Close unnecessary applications
2. ✅ Clear terminal/console
3. ✅ Set up clean workspace
4. ✅ Test run the script once
5. ✅ Prepare what you'll say
6. ✅ Check microphone and screen recording settings

### During Recording:

#### **Opening (0:00 - 0:15)**
```
"Hi! Today I'm demonstrating column name and data format 
standardization - a critical data cleaning step that makes 
datasets easier to use and analyze."
```

#### **Part 1: Show the Problem (0:15 - 0:30)**
```python
# Run the script, pause at Part 1
python src/column_name_standardization_demo.py
```

Say:
```
"Here's a dataset with messy column names. Notice the 
spaces, mixed casing, and special characters. These 
make the data hard to work with."
```

#### **Part 2: Identify Issues (0:30 - 0:45)**
Point to the identified issues and say:
```
"The script identifies specific problems: spaces in names, 
uppercase letters, parentheses, and special characters. 
Each of these makes code more error-prone."
```

#### **Part 3: Apply Standardization (0:45 - 1:05)**
Show the transformation and say:
```
"Now we apply standardization: convert to lowercase, 
replace spaces with underscores, remove special characters. 
See how 'Employee ID' becomes 'employee_id' - much cleaner!"
```

#### **Part 4: Text Standardization (1:05 - 1:30)**
Show the text data standardization:
```
"We also standardize the actual data values. Notice how 
department names have inconsistent spacing and casing. 
After standardization, they're clean and uniform."
```

#### **Part 5: Benefits (1:30 - 1:50)**
Show the before/after comparison:
```
"Compare the before and after. The standardized version 
is cleaner, easier to reference in code, and ready for 
analysis. This prevents errors and saves time later."
```

#### **Closing (1:50 - 2:00)**
```
"Remember: standardize early, standardize always. Clean 
column names lead to clean code. Thanks for watching!"
```

---

## Code Demonstration Flow

### Option 1: Run the Complete Script
```bash
cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3
python src/column_name_standardization_demo.py
```

**Pros:**
- Complete, polished demonstration
- All concepts covered
- Professional output
- Nothing to code during video

**Cons:**
- Less interactive
- Pre-built solution

### Option 2: Use the Jupyter Notebook
```bash
# Open the notebook
jupyter notebook notebooks/13_column_name_standardization.ipynb
```

**Pros:**
- Interactive demonstration
- Step-by-step execution
- Can explain each cell
- More engaging

**Cons:**
- Takes longer
- More opportunity for errors

### Option 3: Live Coding
Create a demonstration from scratch.

**Pros:**
- Shows real coding process
- Most authentic

**Cons:**
- Risk of syntax errors
- May exceed time limit
- Requires more preparation

**Recommendation:** Use Option 1 (complete script) for your first video, then try Option 2 (notebook) if you want to redo it.

---

## Key Concepts to Emphasize

### 1. **snake_case Convention**
```python
✅ Good: employee_id, department_name, satisfaction_score
❌ Bad:  Employee ID, Department Name, Satisfaction Score
```

### 2. **Standardization Rules**
1. Convert to lowercase
2. Replace spaces with underscores
3. Remove special characters
4. Keep names descriptive

### 3. **When to Standardize**
- **Immediately after loading data**
- Before merging datasets
- At the start of your pipeline
- Not as an afterthought

### 4. **Benefits**
- Cleaner code
- Fewer errors
- Easier merging
- Better collaboration
- More professional

---

## Common Mistakes to Avoid

### In the Video:
- ❌ Speaking too fast
- ❌ Not explaining what you're doing
- ❌ Skipping the "why it matters" part
- ❌ Not showing before/after comparison
- ❌ Forgetting to show real data example

### In the Code:
- ❌ Not making a copy of the DataFrame
- ❌ Overwriting original data
- ❌ Inconsistent naming conventions
- ❌ Not handling edge cases

---

## Submission Checklist

Before submitting your video:

- [ ] Video is approximately 2 minutes long
- [ ] Screen is clearly visible
- [ ] Audio is clear and audible
- [ ] Demonstrated column name standardization
- [ ] Applied naming convention (snake_case)
- [ ] Standardized at least one data format
- [ ] Showed before/after comparison
- [ ] Explained why standardization matters
- [ ] Used provided scripts or created own solution
- [ ] Video format is acceptable (MP4, MOV, etc.)
- [ ] Video is uploaded to required platform
- [ ] Link is accessible

---

## Practice Exercises

Before recording your video, practice with these datasets:

### Exercise 1: Basic Standardization
```python
import pandas as pd

data = {
    'First Name': ['Alice', 'Bob'],
    'Last Name ': ['Smith', 'Jones'],
    'Age (years)': [25, 30]
}
df = pd.DataFrame(data)

# TODO: Standardize column names
```

### Exercise 2: Text Data
```python
data = {
    'department': ['  Engineering', 'SALES  ', 'Hr'],
}
df = pd.DataFrame(data)

# TODO: Standardize text values
```

### Exercise 3: Real Data
```python
# Load the messy CSV
df = pd.read_csv('data/raw/employee_survey_messy_columns.csv')

# TODO: Standardize everything
```

---

## Additional Resources

### Best Practices:
1. Always create a copy before modifying
2. Document your transformations
3. Test on sample data first
4. Keep a mapping of old → new names
5. Validate results after standardization

### Pandas String Methods:
```python
.str.lower()      # Convert to lowercase
.str.upper()      # Convert to uppercase
.str.title()      # Convert to title case
.str.strip()      # Remove whitespace
.str.replace()    # Replace patterns
```

### Regular Expressions:
```python
re.sub(r'[^a-z0-9_]', '', text)  # Remove special chars
re.sub(r'_+', '_', text)          # Remove duplicate underscores
```

---

## Troubleshooting

### Problem: "Script not found"
**Solution:** Make sure you're in the correct directory
```bash
cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3
```

### Problem: "Module not found"
**Solution:** Install required packages
```bash
pip install pandas numpy
```

### Problem: "File not found" for CSV
**Solution:** Check the file path
```python
# Use relative path from project root
df = pd.read_csv('data/raw/employee_survey_messy_columns.csv')
```

### Problem: Video too long
**Solution:** Focus on key points only
- Skip detailed explanations
- Show results, not every step
- Practice to reduce hesitation

### Problem: Video too short
**Solution:** Add more explanation
- Explain why each step matters
- Show more examples
- Expand on benefits

---

## Next Steps

After completing this milestone:

1. ✅ Apply standardization to your own datasets
2. ✅ Create a reusable standardization function
3. ✅ Use standardization in every project
4. ✅ Share best practices with your team
5. ✅ Move on to the next learning unit

---

## Support

**Need Help?**
- Review the demonstration script
- Check the Jupyter notebook
- Review the quick reference guide
- Practice with sample data
- Re-watch example videos

**Remember:** 
> "Clean data enables clean analysis. Standardize early, standardize always!"

---

**Good luck with your video walkthrough! 🎬**
