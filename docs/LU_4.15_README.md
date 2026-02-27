# Learning Unit 4.15: Python Lists, Tuples, and Dictionaries

**Trivin Insight Engine - Sprint 3**  
**Last Updated:** February 27, 2026

---

## 📚 Overview

This learning unit covers Python's three fundamental collection types: lists, tuples, and dictionaries. Understanding when and how to use each collection is essential for organizing data effectively in data science projects.

### Learning Objectives

By completing this unit, you will be able to:

- ✅ Create and use lists, tuples, and dictionaries
- ✅ Access elements using indexing (lists/tuples) and keys (dictionaries)
- ✅ Modify mutable collections (lists and dictionaries)
- ✅ Understand and apply tuple immutability
- ✅ Choose the appropriate collection type for different scenarios
- ✅ Combine collections to build complex data structures

---

## 🎯 What You'll Learn

### 1. Lists
- Ordered, mutable collections
- Creating lists: `[1, 2, 3]`
- Accessing elements: indexing and slicing
- Modifying: append, insert, remove, pop
- Common operations: sort, reverse, concatenate
- Use cases: dynamic collections that change

### 2. Tuples
- Ordered, immutable collections
- Creating tuples: `(1, 2, 3)`
- Accessing elements: same as lists
- Unpacking: `a, b, c = my_tuple`
- Immutability: data protection
- Use cases: fixed data, function returns, dictionary keys

### 3. Dictionaries
- Key-value pair collections
- Creating dictionaries: `{"key": "value"}`
- Accessing by key: `my_dict["key"]`
- Safe access: `.get()` method
- Modifying: add, update, remove
- Iteration: keys(), values(), items()
- Use cases: labeled data, configuration, modeling entities

---

## 🚀 Quick Start

### Option 1: Run the Demo Script

```powershell
# Navigate to project root
cd e:\SPRINT3\S86_Trivin_Insight_Engine_Sprint3

# Run the comprehensive demo
python src/collections_fundamentals.py
```

**Expected Output:**
- Section 1: List demonstrations (creation, access, modification)
- Section 2: Tuple demonstrations (immutability, unpacking)
- Section 3: Dictionary demonstrations (key-value operations)
- Section 4: Comparison and use cases
- Section 5: Practical survey system example

### Option 2: Interactive Jupyter Notebook

```powershell
# Start Jupyter
jupyter notebook

# Open: notebooks/03_python_collections.ipynb
```

**The notebook includes:**
- Code examples with explanations
- 4 practice exercises
- 1 final challenge project
- Completion checklist

### Option 3: Python Interactive Shell

```python
# Lists
scores = [4, 5, 3, 4, 5]
scores.append(3)
print(scores)

# Tuples
employee = ("Alice", 1001, "Engineering")
name, emp_id, dept = employee

# Dictionaries
survey = {"score": 4.5, "recommend": True}
survey["date"] = "2026-02-27"
print(survey)
```

---

## 📖 Detailed Guide

### Lists: Mutable, Ordered Collections

**When to Use Lists:**
- You need to add/remove items
- Order matters
- You have similar items (homogeneous data)
- You need to sort or filter

**Common Operations:**
```python
# Create
my_list = [1, 2, 3, 4, 5]

# Access
first = my_list[0]           # 1
last = my_list[-1]           # 5
slice = my_list[1:3]         # [2, 3]

# Modify
my_list.append(6)            # Add to end
my_list.insert(0, 0)         # Insert at position
my_list.remove(3)            # Remove first occurrence
popped = my_list.pop()       # Remove and return last
my_list[0] = 10              # Change by index

# Operations
my_list.sort()               # Sort in place
my_list.reverse()            # Reverse in place
length = len(my_list)        # Get length
```

**Real-World Example:**
```python
# Daily survey scores (can add more each day)
daily_scores = [4.5, 4.2, 4.8, 4.1]
daily_scores.append(4.6)  # New day's score
average = sum(daily_scores) / len(daily_scores)
```

### Tuples: Immutable, Ordered Collections

**When to Use Tuples:**
- Data should NOT change
- Protecting from accidental modification
- Returning multiple values from functions
- Using as dictionary keys (must be immutable)
- Performance matters (tuples are faster)

**Common Operations:**
```python
# Create
my_tuple = (1, 2, 3)
single = (42,)               # Note comma for single item!

# Access (same as lists)
first = my_tuple[0]          # 1
last = my_tuple[-1]          # 3

# Unpack
a, b, c = my_tuple           # a=1, b=2, c=3

# CANNOT modify
# my_tuple[0] = 10           # ❌ TypeError!

# To "change", create new tuple
new_tuple = (10,) + my_tuple[1:]
```

**Real-World Example:**
```python
# Employee record (ID and hire date shouldn't change)
employee = (1001, "Alice Johnson", "Engineering", "2020-01-15")
emp_id, name, dept, hire_date = employee

# Geographic coordinates (immutable)
location = (40.7128, -74.0060)
latitude, longitude = location
```

### Dictionaries: Key-Value Collections

**When to Use Dictionaries:**
- You need labeled data
- Fast key-based lookup
- Modeling entities with attributes
- Configuration settings
- Counting/grouping

**Common Operations:**
```python
# Create
my_dict = {"name": "Alice", "age": 30}

# Access
name = my_dict["name"]              # "Alice"
age = my_dict.get("age")            # 30 (safe)
city = my_dict.get("city", "NYC")   # Default if missing

# Modify
my_dict["age"] = 31                 # Update
my_dict["city"] = "Boston"          # Add new
removed = my_dict.pop("city")       # Remove and return

# Iterate
for key in my_dict.keys():          # Keys only
    print(key)
    
for value in my_dict.values():      # Values only
    print(value)
    
for key, value in my_dict.items():  # Both
    print(f"{key}: {value}")

# Check membership
if "name" in my_dict:
    print(my_dict["name"])
```

**Real-World Example:**
```python
# Survey response with labeled fields
response = {
    "employee_id": 1001,
    "department": "Data Science",
    "score": 4.5,
    "recommend": True,
    "comments": "Great culture"
}

# Easy to understand and access
if response["recommend"] and response["score"] >= 4.0:
    print(f"Positive response from {response['department']}")
```

---

## ⚖️ Comparison: Choosing the Right Type

| Feature | List | Tuple | Dictionary |
|---------|------|-------|------------|
| **Mutable** | ✅ Yes | ❌ No | ✅ Yes |
| **Ordered** | ✅ Yes | ✅ Yes | ✅ Yes (3.7+) |
| **Indexed by** | Position (0, 1, 2...) | Position (0, 1, 2...) | Key (any hashable) |
| **Duplicates** | ✅ Yes | ✅ Yes | Keys: No, Values: Yes |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{"a": 1, "b": 2}` |
| **Performance** | Medium | Fast | Very Fast (lookup) |
| **Use When** | Dynamic collections | Fixed data | Labeled data |

### Decision Tree

```
Need to store multiple items?
│
├─ Are they labeled/named?
│  └─ YES → Use Dictionary
│
└─ NO → Will the data change?
   ├─ YES → Use List
   └─ NO → Use Tuple
```

---

## 🔧 Common Patterns

### Pattern 1: List of Dictionaries
**Use Case:** Multiple similar records

```python
employees = [
    {"id": 1001, "name": "Alice", "dept": "Engineering"},
    {"id": 1002, "name": "Bob", "dept": "Sales"},
    {"id": 1003, "name": "Charlie", "dept": "Marketing"}
]

# Easy to filter
engineers = [e for e in employees if e["dept"] == "Engineering"]
```

### Pattern 2: Dictionary with List Values
**Use Case:** Grouping items by category

```python
by_department = {
    "Engineering": ["Alice", "Bob", "Charlie"],
    "Sales": ["Diana", "Eve"],
    "Marketing": ["Frank"]
}

# Easy to access groups
eng_team = by_department["Engineering"]
```

### Pattern 3: Tuple as Dictionary Key
**Use Case:** Multi-dimensional lookup

```python
# Store data by (year, quarter)
survey_data = {
    (2026, "Q1"): {"score": 4.5, "responses": 120},
    (2026, "Q2"): {"score": 4.7, "responses": 135}
}

q1_score = survey_data[(2026, "Q1")]["score"]
```

### Pattern 4: Nested Structures
**Use Case:** Complex data models

```python
company = {
    "name": "TechCorp",
    "departments": [
        {
            "name": "Engineering",
            "employees": [
                ("Alice", 1001, "Senior"),
                ("Bob", 1002, "Junior")
            ]
        }
    ]
}
```

---

## 🎓 Practice Exercises

### Exercise 1: List Management
Create a system to track daily engagement scores:
- Store 7 days of scores
- Calculate average
- Find highest and lowest
- Identify trend (improving/declining)

### Exercise 2: Tuple Unpacking
Process employee records:
- Create tuples with (id, name, dept, salary)
- Unpack and display formatted
- Calculate average salary
- Group by department

### Exercise 3: Dictionary Operations
Build a survey response tracker:
- Store multiple responses
- Calculate average scores
- Count recommendations
- Generate summary report

### Exercise 4: Combined Collections
Create a complete employee database:
- List of employees
- Each employee is a dictionary
- Include list of skills for each
- Use tuples for contact info

**Solutions in:** `notebooks/03_python_collections.ipynb`

---

## ❗ Common Pitfalls

### 1. Forgetting Comma in Single-Item Tuple
```python
# ❌ Wrong - this is just an integer
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

# ✅ Correct - comma makes it a tuple
is_a_tuple = (42,)
print(type(is_a_tuple))   # <class 'tuple'>
```

### 2. Trying to Modify a Tuple
```python
# ❌ Wrong - will raise TypeError
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# ✅ Correct - create new tuple
my_tuple = (10,) + my_tuple[1:]
```

### 3. Dictionary KeyError
```python
# ❌ Risky - KeyError if key doesn't exist
score = my_dict["score"]

# ✅ Safe - returns None if missing
score = my_dict.get("score")

# ✅ With default
score = my_dict.get("score", 0)
```

### 4. Modifying List While Iterating
```python
# ❌ Wrong - can skip items or cause errors
scores = [1, 2, 3, 4, 5]
for score in scores:
    if score < 3:
        scores.remove(score)  # Don't do this!

# ✅ Correct - create new list
scores = [s for s in scores if s >= 3]
```

### 5. Confusing [] and ()
```python
# Clear difference
my_list = [1, 2, 3]      # List
my_tuple = (1, 2, 3)     # Tuple

# But parentheses can be omitted for tuples
also_tuple = 1, 2, 3     # Still a tuple!
a, b, c = 1, 2, 3        # Tuple unpacking
```

---

## 🐛 Troubleshooting

### "TypeError: 'tuple' object does not support item assignment"
**Problem:** Trying to modify an immutable tuple  
**Solution:** Create a new tuple or use a list instead

```python
# If you need to modify, use a list
my_list = [1, 2, 3]
my_list[0] = 10  # OK
```

### "KeyError: 'key_name'"
**Problem:** Accessing non-existent dictionary key  
**Solution:** Use `.get()` or check with `in`

```python
# Safe access
value = my_dict.get("key", default_value)

# Or check first
if "key" in my_dict:
    value = my_dict["key"]
```

### "IndexError: list index out of range"
**Problem:** Accessing index that doesn't exist  
**Solution:** Check length first

```python
if len(my_list) > 5:
    item = my_list[5]
```

### "TypeError: unhashable type: 'list'"
**Problem:** Using mutable type (list) as dictionary key  
**Solution:** Use immutable type (tuple) instead

```python
# ❌ Won't work
# my_dict = {[1, 2]: "value"}

# ✅ Works
my_dict = {(1, 2): "value"}
```

---

## 📊 Performance Considerations

| Operation | List | Tuple | Dictionary |
|-----------|------|-------|------------|
| Access by index/key | O(1) | O(1) | O(1) |
| Search for value | O(n) | O(n) | O(1) for keys |
| Append/Add | O(1) | N/A | O(1) |
| Insert | O(n) | N/A | N/A |
| Delete | O(n) | N/A | O(1) |
| Memory usage | Medium | Low | High |

**Key Takeaways:**
- Tuples are fastest (immutable = optimized)
- Dictionaries excel at key lookups
- Lists are flexible but slower for large datasets

---

## 🎬 Video Recording Checklist

Your 2-minute video should cover:

- [ ] **Lists (45 sec):** Create, access, modify, show mutability
- [ ] **Tuples (45 sec):** Create, access, unpack, show immutability error
- [ ] **Dictionaries (45 sec):** Create, access by key, modify, iterate
- [ ] **Comparison (15 sec):** When to use each type

**Script:** See `docs/LU_4.15_VIDEO_SCRIPT.md`

---

## ✅ Completion Criteria

You've mastered this unit when you can:

- [ ] Create all three collection types without looking up syntax
- [ ] Explain the difference between mutable and immutable
- [ ] Choose the right collection for a given scenario
- [ ] Access elements using both indexing and keys
- [ ] Modify lists and dictionaries safely
- [ ] Unpack tuples into variables
- [ ] Iterate over all collection types
- [ ] Combine collections to model complex data
- [ ] Debug common collection errors
- [ ] Apply collections to real data science tasks

---

## 🔗 Additional Resources

### Official Documentation
- [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Related Learning Units
- **LU 4.14:** Python Numeric and String Data Types (prerequisite)
- **LU 4.16:** Python Control Flow (next topic)
- **LU 5.x:** Pandas DataFrames (builds on these concepts)

### Quick Reference
- See `docs/LU_4.15_QUICK_REFERENCE.md` for syntax cheat sheet

---

## 📝 Assignment Deliverables

For Kalvium submission:

1. **Video Recording (Required)**
   - 2-minute demonstration
   - Cover all three collection types
   - Show mutability differences
   - Upload to platform

2. **Code Files (Recommended)**
   - `src/collections_fundamentals.py` (demo script)
   - `notebooks/03_python_collections.ipynb` (exercises)

3. **Completion Tracker**
   - Update `LEARNING_UNIT_COMPLETION.md`

---

## 🎯 Next Steps

After completing this unit:

1. ✅ Mark tasks complete in Kalvium
2. 📹 Record and submit 2-minute video
3. 💾 Commit code to Git (see Git workflow below)
4. ➡️ Move to **LU 4.16: Python Control Flow**

### Git Workflow

```powershell
# Create feature branch
git checkout -b feature/lu-4.15-python-collections

# Add files
git add src/collections_fundamentals.py
git add notebooks/03_python_collections.ipynb
git add docs/LU_4.15_*

# Commit
git commit -m "feat: complete LU 4.15 - Python Collections

- Implement list operations and demonstrations
- Implement tuple immutability examples
- Implement dictionary key-value operations
- Create interactive Jupyter notebook with 4 exercises
- Add video walkthrough script
- Document common patterns and pitfalls

Addresses: Learning Unit 4.15 requirements"

# Push
git push origin feature/lu-4.15-python-collections
```

---

**Questions or issues?** Check the troubleshooting section or review the video script for guidance.

**Good luck! Collections are fundamental to everything in Python and data science! 🚀**
