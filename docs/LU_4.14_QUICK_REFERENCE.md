# Python Data Types - Quick Reference Guide

**Learning Unit 4.14 - Quick Cheat Sheet**  
**Trivin Insight Engine - Sprint 3**

---

## 📌 Numeric Types

### Integer (`int`)
```python
count = 42
employees = 100
year = 2026

# Whole numbers (no decimals)
# Can be positive, negative, or zero
```

### Float (`float`)
```python
average = 4.2
price = 99.99
temperature = -5.5

# Decimal numbers
# Floating-point precision
```

---

## 🔢 Arithmetic Operations

| Operation | Symbol | Example | Result |
|-----------|--------|---------|--------|
| Addition | `+` | `10 + 5` | `15` |
| Subtraction | `-` | `10 - 5` | `5` |
| Multiplication | `*` | `10 * 5` | `50` |
| Division | `/` | `10 / 3` | `3.333...` (float) |
| Floor Division | `//` | `10 // 3` | `3` (int) |
| Modulo | `%` | `10 % 3` | `1` (remainder) |
| Exponentiation | `**` | `10 ** 2` | `100` (10²) |

---

## 📝 String Types

### Creating Strings
```python
# Single quotes
name = 'Alice'

# Double quotes
department = "Engineering"

# Triple quotes (multi-line)
message = """
Hello,
World!
"""
```

### String Operations
```python
# Concatenation
full_name = first + " " + last

# Repetition
divider = "-" * 40

# Length
length = len(text)  # Number of characters

# Indexing
first_char = text[0]    # First character
last_char = text[-1]    # Last character

# Slicing
substring = text[0:5]   # Characters 0-4
substring = text[:5]    # First 5 characters
substring = text[5:]    # From position 5 onwards
```

---

## 🛠️ String Methods

| Method | Example | Result |
|--------|---------|--------|
| `.upper()` | `"hello".upper()` | `"HELLO"` |
| `.lower()` | `"HELLO".lower()` | `"hello"` |
| `.title()` | `"hello world".title()` | `"Hello World"` |
| `.strip()` | `"  hi  ".strip()` | `"hi"` |
| `.replace(old, new)` | `"cat".replace("c", "b")` | `"bat"` |
| `.split()` | `"a b c".split()` | `["a", "b", "c"]` |
| `.startswith(s)` | `"hello".startswith("he")` | `True` |
| `.endswith(s)` | `"hello".endswith("lo")` | `True` |

---

## 🔄 Type Conversion

### Number → String
```python
age = 30
age_str = str(age)           # "30"
message = f"Age: {age}"      # "Age: 30" (f-string)
message = "Age: " + str(age) # "Age: 30"
```

### String → Number
```python
# String to integer
score_str = "85"
score = int(score_str)       # 85

# String to float
price_str = "99.99"
price = float(price_str)     # 99.99
```

### Type Conversion Table

| From | To | Function | Example |
|------|------|----------|---------|
| int | str | `str()` | `str(42)` → `"42"` |
| float | str | `str()` | `str(3.14)` → `"3.14"` |
| str | int | `int()` | `int("42")` → `42` |
| str | float | `float()` | `float("3.14")` → `3.14` |
| float | int | `int()` | `int(3.14)` → `3` (truncates) |
| int | float | `float()` | `float(42)` → `42.0` |

---

## 🎯 String Formatting

### F-Strings (Recommended)
```python
name = "Alice"
age = 30
score = 87.5

# Basic
message = f"Hello, {name}!"
# Result: "Hello, Alice!"

# With expressions
message = f"{name} is {age} years old"
# Result: "Alice is 30 years old"

# With formatting
message = f"Score: {score:.1f}%"
# Result: "Score: 87.5%"

# With alignment
message = f"{name:<10}|"  # Left-align (10 chars)
message = f"{name:>10}|"  # Right-align (10 chars)
message = f"{name:^10}|"  # Center (10 chars)
```

### Format Specifiers
```python
value = 1234.5678

f"{value:.2f}"    # "1234.57" (2 decimals)
f"{value:,.2f}"   # "1,234.57" (with comma)
f"{value:>10}"    # "  1234.5678" (right-align, 10 wide)
f"{value:010.2f}" # "0001234.57" (zero-padded)
```

---

## 🔍 Type Inspection

### Check Type
```python
# Get type
x = 42
print(type(x))        # <class 'int'>
print(type(x).__name__)  # "int"

# Check if specific type
value = "hello"
if isinstance(value, str):
    print("It's a string!")

# Check multiple types
if isinstance(value, (int, float)):
    print("It's a number!")
```

### Type Checking Table

| Check | Code | Result |
|-------|------|--------|
| Is integer? | `isinstance(x, int)` | `True/False` |
| Is float? | `isinstance(x, float)` | `True/False` |
| Is string? | `isinstance(x, str)` | `True/False` |
| Is number? | `isinstance(x, (int, float))` | `True/False` |
| Get type | `type(x).__name__` | `"int"`, `"float"`, `"str"`, etc. |

**Note:** `isinstance(True, int)` returns `True` because bool is a subclass of int!

---

## ❌ Common Errors

### TypeError: Cannot Concatenate
```python
# ❌ WRONG
age = 30
message = "Age: " + age  # TypeError!

# ✅ CORRECT
message = "Age: " + str(age)
message = f"Age: {age}"
```

### String Concatenation vs Addition
```python
# ❌ String concatenation (not addition)
result = "5" + "3"  # "53" (string)

# ✅ Numeric addition
result = int("5") + int("3")  # 8 (integer)
```

### ValueError: Invalid Conversion
```python
# ❌ Cannot convert
num = int("abc")  # ValueError!

# ✅ Validate first
text = "abc"
if text.isdigit():
    num = int(text)
else:
    print("Not a valid number")
```

### Division Type Confusion
```python
# Regular division (returns float)
result = 10 / 3      # 3.3333...

# Floor division (returns int)
result = 10 // 3     # 3
```

---

## ✅ Best Practices

### 1. Use F-Strings for Formatting
```python
# ✅ Preferred
name = "Alice"
age = 30
message = f"{name} is {age} years old"

# ❌ Avoid (harder to read)
message = name + " is " + str(age) + " years old"
```

### 2. Validate Before Converting
```python
# ✅ Good practice
user_input = "42"
if user_input.isdigit():
    number = int(user_input)
else:
    print("Invalid input")

# OR use try/except
try:
    number = int(user_input)
except ValueError:
    print("Invalid input")
```

### 3. Use isinstance() for Type Checking
```python
# ✅ Recommended
def calculate(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be numeric")
    return value * 2

# ❌ Less robust
def calculate(value):
    if type(value) not in [int, float]:  # Doesn't handle subclasses
        raise TypeError("Value must be numeric")
    return value * 2
```

### 4. Choose Appropriate Type
```python
# ✅ Use int for counts
employee_count = 50  # int (not 50.0)

# ✅ Use float for measurements
average_score = 4.2  # float

# ✅ Use str for text
employee_name = "Alice"  # str
```

---

## 🚨 Quick Troubleshooting

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| TypeError: unsupported operand | Mixing string + number | Convert: `str(num)` or `int(str)` |
| ValueError: invalid literal | Converting non-numeric string | Validate or use try/except |
| "53" instead of 8 | String concat instead of add | Convert to int first |
| 3.333 instead of 3 | Used `/` instead of `//` | Use `//` for integer division |
| AttributeError: 'int' has no attribute... | Called string method on number | Check type with `type()` |

---

## 📋 Quick Reference Code

### Complete Example
```python
# Numeric types
employee_count = 50              # int
average_rating = 4.2             # float

# String types
employee_name = "Alice Johnson"  # str
department = "Engineering"       # str

# Type inspection
print(type(employee_count))      # <class 'int'>
print(type(average_rating))      # <class 'float'>

# Type conversion
count_str = str(employee_count)  # "50"
rating_int = int(average_rating) # 4 (truncated)

# String formatting
report = f"{employee_name} from {department} has rating {average_rating}"
print(report)
# Output: "Alice Johnson from Engineering has rating 4.2"

# Type validation
if isinstance(average_rating, (int, float)):
    percentage = average_rating / 5 * 100
    print(f"Percentage: {percentage:.1f}%")
    # Output: "Percentage: 84.0%"
```

---

## 🎯 Video Recording Cheat Sheet

### Section 1: Numeric Types (30s)
```python
employees = 50                    # int
score = 4.2                       # float
print(10 / 3)                     # 3.333... (float)
print(10 // 3)                    # 3 (int)
```

### Section 2: String Types (30s)
```python
name = "Sarah"                    # str
full = name + " Johnson"          # concatenation
print(name.upper())               # "SARAH"
print(f"{name} scored {score}")   # f-string
```

### Section 3: Type Mixing (30s)
```python
age = 30
# "Age: " + age                   # ERROR!
message = f"Age: {age}"           # Correct
score1 = int("85")                # Convert
score2 = int("92")                # Convert
total = score1 + score2           # 177
```

### Section 4: Type Inspection (30s)
```python
print(type(42))                   # <class 'int'>
print(isinstance(age, int))       # True

def calc(x):
    if not isinstance(x, (int, float)):
        return "Error"
    return x * 2
```

---

## 💡 Memory Aids

### Division Types
- `/` = **D**ivision returns **D**ecimal (float)
- `//` = **F**loor division returns **F**lat number (int)

### String Methods
- **UPPER** for `.upper()`
- **lower** for `.lower()`
- Clean spaces with `.strip()`

### Type Conversion
- **str**ing = `str()`
- **int**eger = `int()`
- **float**ing-point = `float()`

### F-String = Format String
- **F** = Fast, Flexible, Formatted
- Always put `f` before the quotes: `f"..."`

---

**Print this for quick reference during coding!**

*Learning Unit 4.14 - Trivin Insight Engine - February 27, 2026*
