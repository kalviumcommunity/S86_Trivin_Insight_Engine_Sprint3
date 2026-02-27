# Learning Unit 4.14: Understanding Python Numeric and String Data Types

**Trivin Insight Engine - Data Science Sprint 3**  
**Date:** February 27, 2026  
**Status:** ✅ Complete

---

## 📋 Overview

This learning unit focuses on understanding Python's core numeric and string data types, which form the foundation of all data processing and analysis. Before working with datasets, you must be comfortable representing numbers, text, and basic operations correctly.

### Learning Objectives

By completing this milestone, you will be able to:

- ✅ Differentiate between numeric and string data types
- ✅ Perform arithmetic using Python numbers
- ✅ Manipulate and format strings correctly
- ✅ Identify data type mismatches
- ✅ Write clearer and safer Python code

---

## 📁 Files and Resources

### Main Files

1. **`src/data_types_fundamentals.py`**
   - Comprehensive Python script demonstrating all concepts
   - Can be run directly: `python src/data_types_fundamentals.py`
   - Includes 5 main sections with practical examples
   - Output shows type information and results

2. **`notebooks/02_data_types_fundamentals.ipynb`**
   - Interactive Jupyter notebook for hands-on learning
   - Contains exercises with practice problems
   - Includes detailed explanations and examples
   - Perfect for video walkthrough demonstrations

3. **`docs/LU_4.14_VIDEO_SCRIPT.md`**
   - Complete 2-minute video walkthrough script
   - Section-by-section guide with timing
   - Code snippets for each demonstration
   - Technical requirements and best practices

---

## 🚀 Quick Start

### Option 1: Run the Python Script

```powershell
# Navigate to project directory
cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3

# Run the complete demonstration
python src/data_types_fundamentals.py
```

**Output:** Comprehensive demonstration of all data type concepts with examples.

### Option 2: Use the Jupyter Notebook (Recommended)

```powershell
# Start Jupyter Notebook
jupyter notebook

# Open: notebooks/02_data_types_fundamentals.ipynb
# Run cells interactively to learn and practice
```

**Benefits:**
- Interactive code execution
- Practice exercises included
- See outputs immediately
- Perfect for learning

### Option 3: Follow the Video Script

```powershell
# Open the video script for guidance
# File: docs/LU_4.14_VIDEO_SCRIPT.md

# Use provided code snippets
# Record your 2-minute demonstration
```

---

## 📚 Content Structure

### 1. Working with Numeric Data Types

**Topics Covered:**
- Integer (int) vs Float data types
- Basic arithmetic operations (+, -, *, /)
- Division behavior (/ vs //)
- Modulo operator (%)
- Exponentiation (**)
- Numeric precision

**Key Examples:**
```python
# Integers
employees = 50
departments = 5

# Floats
average_score = 4.2
response_rate = 84.5

# Division behavior
print(10 / 3)   # 3.333... (float)
print(10 // 3)  # 3 (integer)

# Power operations
future_salary = 50000 * (1.05 ** 3)  # 5% annual raise for 3 years
```

---

### 2. Understanding String Data Types

**Topics Covered:**
- Creating strings (quotes, triple quotes)
- String concatenation
- String indexing and slicing
- String methods (.upper(), .lower(), .strip(), etc.)
- String formatting (f-strings, .format(), %)
- Multi-line strings

**Key Examples:**
```python
# Creating strings
name = "Sarah Johnson"
department = 'Engineering'

# Concatenation
full_name = first_name + " " + last_name

# Slicing
company = "Trivin Insights"
print(company[0:6])  # "Trivin"

# Methods
message = "  python  "
print(message.strip().upper())  # "PYTHON"

# F-string formatting
score = 87.5
report = f"Score: {score:.1f}%"
```

---

### 3. Mixing Numbers and Strings Safely

**Topics Covered:**
- Why type mixing causes errors
- Converting numbers to strings (str())
- Converting strings to numbers (int(), float())
- F-strings for automatic formatting
- Common pitfalls ("85" + "92" vs 85 + 92)
- Handling conversion errors (try/except)

**Key Examples:**
```python
# ERROR: Cannot mix types
age = 30
# message = "Age is " + age  # TypeError!

# CORRECT: Convert first
message = "Age is " + str(age)
message2 = f"Age is {age}"      # F-string (recommended)

# String to number conversion
score_str = "85"
score_num = int(score_str)
result = score_num + 10  # 95

# Handling errors
try:
    num = int("abc")
except ValueError:
    print("Cannot convert to integer")
```

---

### 4. Inspecting Data Types

**Topics Covered:**
- Using type() function
- Using isinstance() for validation
- Checking numeric vs string types
- Type validation in functions
- Best practices for type checking

**Key Examples:**
```python
# Check type
age = 30
print(type(age))  # <class 'int'>

# Validate type
if isinstance(salary, (int, float)):
    bonus = salary * 0.10
else:
    print("Salary must be numeric")

# Comprehensive validation
def calculate_bonus(salary, rate):
    if not isinstance(salary, (int, float)):
        return "Error: Invalid salary type"
    if not isinstance(rate, (int, float)):
        return "Error: Invalid rate type"
    return salary * rate
```

---

### 5. Practical Examples

**Real-world scenarios:**
- Employee data processing
- Salary calculations (annual, monthly, hourly)
- Survey score aggregation
- Formatted report generation
- Mixed data type handling

---

## 🎯 Practice Exercises

The Jupyter notebook includes **4 practice exercises**:

1. **Exercise 1:** Numeric Operations
   - Calculate survey statistics
   - Response rates and percentages
   - Projections

2. **Exercise 2:** String Manipulation
   - Create formatted employee badges
   - String methods practice
   - Text formatting

3. **Exercise 3:** Type Conversion
   - Process simulated user input
   - Safe string-to-number conversion
   - Generate summary reports

4. **Exercise 4:** Type Validation
   - Build data validator function
   - Check employee data types
   - Error messages for invalid types

**Final Challenge:**
- Complete employee survey analyzer
- Combines all learned concepts
- Full validation and reporting

---

## 🎥 Video Walkthrough Requirements

### What to Include (2 minutes total):

**Section 1: Numeric Types** (30 seconds)
- Show int and float examples
- Demonstrate arithmetic operations
- Show division behavior

**Section 2: String Types** (30 seconds)
- Create strings
- Show concatenation
- Demonstrate formatting

**Section 3: Type Mixing** (30 seconds)
- Show type error
- Demonstrate conversion
- Use str(), int(), float()

**Section 4: Type Inspection** (30 seconds)
- Use type() function
- Show isinstance() checks
- Explain importance

### Video Guidelines:

✅ **Requirements:**
- Approximately 2 minutes duration
- Screen-facing and clearly visible
- Clear audio
- All code examples shown
- Outputs demonstrated
- Concepts explained verbally

📋 **Checklist:**
- [ ] Font size 14pt or larger
- [ ] Code runs without errors
- [ ] Outputs clearly shown
- [ ] All four sections covered
- [ ] Professional presentation
- [ ] Audio quality good
- [ ] Uploaded and link ready

See [`docs/LU_4.14_VIDEO_SCRIPT.md`](LU_4.14_VIDEO_SCRIPT.md) for complete script and guidelines.

---

## ⚡ Key Takeaways

### Data Types:
| Type | Description | Examples | Common Use |
|------|-------------|----------|------------|
| `int` | Whole numbers | 42, -17, 0 | Counts, IDs, whole quantities |
| `float` | Decimal numbers | 3.14, -0.5, 2.0 | Measurements, averages, rates |
| `str` | Text data | "Hello", 'Python' | Names, labels, messages |
| `bool` | True/False | True, False | Conditions, flags |

### Best Practices:

✅ **DO:**
- Use f-strings for formatting
- Validate types before operations
- Convert explicitly when needed
- Choose appropriate numeric type
- Use meaningful variable names

❌ **DON'T:**
- Mix types without conversion
- Assume input types are correct
- Ignore TypeError messages
- Use string concatenation for math
- Skip type validation

### Common Errors and Solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| `TypeError: can only concatenate str (not "int") to str` | Mixing string + number | Use `str(number)` or f-string |
| `ValueError: invalid literal for int()` | Converting non-numeric string | Validate before conversion |
| `'85' + '92' = '8592'` | String concatenation instead of addition | Convert to int/float first |
| Division returns unexpected type | Using `/` instead of `//` | Use `//` for integer division |

---

## 📊 Learning Path

### Prerequisites:
- ✅ Basic Python installation
- ✅ Text editor or Jupyter Notebook
- ✅ Understanding of variables

### Current Learning Unit:
- 📍 **LU 4.14: Numeric and String Data Types** (You are here)

### Next Steps:
1. ➡️ LU 4.15: Creating and Running First Python Script
2. ➡️ LU 4.16: Working with Lists, Tuples, and Dictionaries
3. ➡️ Continue Data Science Sprint

---

## 🔍 Testing Your Understanding

### Self-Assessment Questions:

1. **What's the difference between `/` and `//`?**
   - Answer: `/` returns float (exact), `//` returns int (floor division)

2. **How do you convert string "42" to integer?**
   - Answer: `int("42")`

3. **Why does `"5" + "3"` give `"53"` not `8`?**
   - Answer: + on strings means concatenation, not addition

4. **How do you check if a variable is an integer?**
   - Answer: `isinstance(var, int)` (but watch for bool!)

5. **What's the best way to format strings with variables?**
   - Answer: F-strings: `f"Value is {variable}"`

### Quick Test:

Run this code and predict the output:

```python
x = 10
y = "20"
result1 = x + int(y)
result2 = str(x) + y
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
```

**Expected Output:**
```
Result 1: 30
Result 2: 1020
```

---

## 🛠️ Troubleshooting

### Common Issues:

**Issue:** Script won't run  
**Solution:** Check Python installation: `python --version`

**Issue:** Jupyter notebook won't open  
**Solution:** Install Jupyter: `pip install jupyter notebook`

**Issue:** TypeError when running code  
**Solution:** Check variable types with `print(type(variable))`

**Issue:** Unexpected numeric results  
**Solution:** Check if using `/` vs `//` for division

**Issue:** String methods not working  
**Solution:** Ensure variable is a string: `isinstance(var, str)`

---

## 📖 Additional Resources

### Official Documentation:
- [Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Type Conversion](https://docs.python.org/3/library/functions.html#type)

### Bonus Content (Optional):
- Python Numeric Types - Deep dive
- Python Strings Explained - Advanced features
- Type Conversion in Python - Best practices

---

## ✅ Completion Checklist

Before marking this LU as complete:

- [ ] Reviewed all code in `src/data_types_fundamentals.py`
- [ ] Completed Jupyter notebook exercises
- [ ] Understood numeric types (int and float)
- [ ] Mastered string operations and formatting
- [ ] Can convert between types safely
- [ ] Know how to inspect types
- [ ] Completed all 4 practice exercises
- [ ] Attempted final challenge
- [ ] Prepared for video walkthrough
- [ ] Recorded 2-minute video (if required)
- [ ] Submitted video link (if required)
- [ ] Ready for next learning unit

---

## 📝 Submission

### For Assignment Submission:

1. **Code Files:**
   - Ensure all scripts run without errors
   - Complete exercise solutions in notebook
   - Show all outputs

2. **Video Recording:**
   - Duration: ~2 minutes
   - Screen clearly visible
   - Audio clear
   - Upload to required platform
   - Submit link

3. **Pull Request (if required):**
   - Create branch for LU 4.14
   - Commit all files
   - Push to repository
   - Create PR with description

### Grading Criteria:

Target: **60% or more**

Areas assessed:
- Understanding of numeric types
- String manipulation skills
- Type conversion accuracy
- Type validation practices
- Code quality and clarity
- Video demonstration quality

---

## 💡 Tips for Success

1. **Practice Regularly:** Type the code yourself, don't just read
2. **Experiment:** Try variations to see what happens
3. **Use print():** Debug by printing types and values
4. **Read Error Messages:** They tell you exactly what's wrong
5. **Ask Questions:** If confused, seek clarification
6. **Build Habits:** Always validate types in real applications

---

## 🎓 Learning Outcomes

After completing this unit, you should feel confident:

✅ Working with integers and floats  
✅ Performing arithmetic operations  
✅ Creating and manipulating strings  
✅ Converting between data types  
✅ Validating data types  
✅ Debugging type-related errors  
✅ Writing type-safe code  
✅ Applying concepts to real scenarios  

**Congratulations on completing LU 4.14!**

---

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review error messages carefully
3. Consult official Python documentation
4. Ask instructor or teaching assistant
5. Collaborate with classmates (following academic honesty policies)

---

## 🔄 Updates and Revisions

**Version:** 1.0  
**Last Updated:** February 27, 2026  
**Status:** Complete and ready for use

---

**Related Files:**
- Main Script: [`src/data_types_fundamentals.py`](../src/data_types_fundamentals.py)
- Notebook: [`notebooks/02_data_types_fundamentals.ipynb`](../notebooks/02_data_types_fundamentals.ipynb)
- Video Script: [`docs/LU_4.14_VIDEO_SCRIPT.md`](LU_4.14_VIDEO_SCRIPT.md)

**Project:** Trivin Insight Engine - Sprint 3  
**Course:** Data Science Fundamentals  
**Learning Unit:** 4.14 - Python Numeric and String Data Types
