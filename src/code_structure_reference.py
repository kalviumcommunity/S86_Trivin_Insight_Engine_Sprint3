"""
QUICK REFERENCE: Code Structure Best Practices
===============================================
Keep this file open as a reference when writing Python code.

Author: Trivin Insight Engine
Date: March 3, 2026
"""

# ============================================================================
# TEMPLATE: WELL-STRUCTURED PYTHON SCRIPT
# ============================================================================

# 1. MODULE DOCSTRING (always at the very top)
"""
Brief description of what this module does.

This module contains functions for [purpose].
Used in [project/context].
"""

# 2. IMPORTS (grouped and organized)
# Standard library imports
import os
import sys
from datetime import datetime

# Third-party imports
# import pandas as pd
# import numpy as np

# Local application imports
# from .config import settings
# from .utils import helper_function


# 3. CONSTANTS AND CONFIGURATION (all caps with underscores)
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"
SUPPORTED_FILE_TYPES = ['.csv', '.json', '.xlsx']


# 4. HELPER FUNCTIONS (defined before use)
def format_timestamp(dt):
    """
    Format a datetime object as ISO string.
    
    Args:
        dt: datetime object
        
    Returns:
        ISO formatted string
    """
    return dt.isoformat()


def validate_input(value, min_val, max_val):
    """
    Validate that a value is within acceptable range.
    
    Args:
        value: The value to validate
        min_val: Minimum acceptable value
        max_val: Maximum acceptable value
        
    Returns:
        True if valid, False otherwise
    """
    return min_val <= value <= max_val


# 5. MAIN LOGIC FUNCTIONS (core functionality)
def process_data(data_list):
    """
    Process a list of data items.
    
    Args:
        data_list: List of items to process
        
    Returns:
        Processed results
    """
    results = []
    for item in data_list:
        # Processing logic here
        processed_item = item * 2  # Example
        results.append(processed_item)
    return results


# 6. MAIN EXECUTION FUNCTION
def main():
    """
    Main execution function.
    Coordinates the overall program flow.
    """
    print("Starting program...")
    
    # Example execution
    sample_data = [1, 2, 3, 4, 5]
    results = process_data(sample_data)
    
    print(f"Processed {len(results)} items")
    print(f"Results: {results}")


# 7. ENTRY POINT (always at the bottom)
if __name__ == "__main__":
    main()


# ============================================================================
# BEFORE vs AFTER EXAMPLES
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# EXAMPLE 1: CALCULATING PERCENTAGES
# ────────────────────────────────────────────────────────────────────────────

# ❌ BEFORE (repetitive, hard to maintain)
"""
surveyed = 360
total_employees = 450
response_rate = (surveyed / total_employees) * 100
print(f"Response rate: {response_rate}%")

completed = 175
total_tasks = 200
completion_rate = (completed / total_tasks) * 100
print(f"Completion rate: {completion_rate}%")

present = 42
total_staff = 50
attendance_rate = (present / total_staff) * 100
print(f"Attendance rate: {attendance_rate}%")
"""

# ✅ AFTER (reusable function)
"""
def calculate_percentage(part, whole):
    '''Calculate percentage from part and whole'''
    return (part / whole) * 100

response_rate = calculate_percentage(360, 450)
completion_rate = calculate_percentage(175, 200)
attendance_rate = calculate_percentage(42, 50)

print(f"Response rate: {response_rate:.1f}%")
print(f"Completion rate: {completion_rate:.1f}%")
print(f"Attendance rate: {attendance_rate:.1f}%")
"""


# ────────────────────────────────────────────────────────────────────────────
# EXAMPLE 2: PROCESSING DATA
# ────────────────────────────────────────────────────────────────────────────

# ❌ BEFORE (everything in one block, no structure)
"""
data = [85000, 92000, 78000, 95000, 88000]
total = 0
for num in data:
    total = total + num
avg = total / len(data)
print("Average:", avg)

scores = [4, 5, 3, 4, 5]
total2 = 0
for s in scores:
    total2 = total2 + s
avg2 = total2 / len(scores)
print("Score avg:", avg2)
"""

# ✅ AFTER (structured with reusable functions)
"""
def calculate_average(numbers):
    '''Calculate the average of a list of numbers'''
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

# Clear data definitions
employee_salaries = [85000, 92000, 78000, 95000, 88000]
survey_scores = [4, 5, 3, 4, 5]

# Clean execution
average_salary = calculate_average(employee_salaries)
average_score = calculate_average(survey_scores)

print(f"Average salary: ${average_salary:,.2f}")
print(f"Average score: {average_score:.2f}")
"""


# ────────────────────────────────────────────────────────────────────────────
# EXAMPLE 3: DATA VALIDATION
# ────────────────────────────────────────────────────────────────────────────

# ❌ BEFORE (repeated validation logic)
"""
age = 25
if age >= 18 and age <= 65:
    print("Valid age")
else:
    print("Invalid age")

score = 85
if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")

temperature = 72
if temperature >= -50 and temperature <= 150:
    print("Valid temperature")
else:
    print("Invalid temperature")
"""

# ✅ AFTER (reusable validation function)
"""
def is_within_range(value, min_val, max_val, label):
    '''Check if value is within acceptable range'''
    if min_val <= value <= max_val:
        print(f"Valid {label}: {value}")
        return True
    else:
        print(f"Invalid {label}: {value}")
        return False

# Clean, readable execution
is_within_range(25, 18, 65, "age")
is_within_range(85, 0, 100, "score")
is_within_range(72, -50, 150, "temperature")
"""


# ============================================================================
# QUICK STRUCTURE CHECKLIST
# ============================================================================

"""
When writing a Python script, follow this structure:

✅ 1. Module docstring at the very top
✅ 2. Imports grouped and organized
        - Standard library
        - Third-party
        - Local
✅ 3. Constants and configuration (UPPER_CASE names)
✅ 4. Helper/utility functions
✅ 5. Main logic functions
✅ 6. Main execution function (if needed)
✅ 7. if __name__ == "__main__": block at the bottom

Benefits:
- Predictable and easy to navigate
- Clear separation of concerns
- Easy to test individual functions
- Scalable as project grows
- Collaborative-friendly
"""


# ============================================================================
# FUNCTION BEST PRACTICES
# ============================================================================

"""
GOOD FUNCTION CHARACTERISTICS:

1. SINGLE PURPOSE
   ✅ Each function does ONE thing well
   ❌ Avoid functions that do too many unrelated tasks

2. CLEAR NAMING
   ✅ Name describes what the function does (verb + noun)
   ✅ calculate_total(), validate_email(), format_date()
   ❌ do_stuff(), process(), handle()

3. GOOD DOCUMENTATION
   ✅ Docstring explains purpose, args, and return value
   ✅ Comments explain WHY, not WHAT

4. APPROPRIATE LENGTH
   ✅ Generally 5-20 lines for most functions
   ❌ 100+ line functions are hard to understand

5. MINIMAL SIDE EFFECTS
   ✅ Functions should preferably return values
   ✅ Avoid modifying global state when possible

Example of a well-structured function:

def calculate_discount_price(original_price, discount_percent):
    '''
    Calculate final price after applying discount.
    
    Args:
        original_price: Original price before discount
        discount_percent: Discount percentage (0-100)
        
    Returns:
        Final price after discount
    '''
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    
    return final_price
"""


# ============================================================================
# NAMING CONVENTIONS QUICK REFERENCE
# ============================================================================

"""
PEP 8 NAMING STANDARDS:

Variables and Functions:
✅ use_snake_case
✅ total_count, calculate_average(), user_name

Constants:
✅ USE_UPPER_CASE_WITH_UNDERSCORES
✅ MAX_ATTEMPTS, DEFAULT_TIMEOUT, API_KEY

Classes (not covered in this unit):
✅ UsePascalCase
✅ Employee, DataProcessor, SurveyAnalyzer

Private/Internal:
✅ _leading_underscore
✅ _internal_function(), _helper_variable

Avoid:
❌ Single letters (except for short loops: for i in range...)
❌ Ambiguous abbreviations (tmp, val, x, data1, data2)
❌ CamelCase for functions/variables (save it for classes)
"""


# ============================================================================
# COMMON PATTERNS
# ============================================================================

# PATTERN 1: Configuration at top
"""
# Configuration
INPUT_FILE = "data/survey.csv"
OUTPUT_FILE = "outputs/results.txt"
BATCH_SIZE = 100

# Functions use these constants
def load_data():
    return pd.read_csv(INPUT_FILE)
"""

# PATTERN 2: Guard clauses for validation
"""
def process_score(score):
    '''Process a survey score'''
    # Guard clauses (early returns for invalid input)
    if score is None:
        return 0
    if score < 1 or score > 5:
        return 0
    
    # Main logic
    return score * 20  # Convert to percentage
"""

# PATTERN 3: Main execution wrapper
"""
def main():
    '''Main execution function'''
    print("Starting...")
    
    data = load_data()
    results = process_data(data)
    save_results(results)
    
    print("Complete!")

if __name__ == "__main__":
    main()
"""

# ============================================================================
# END OF QUICK REFERENCE
# Keep this file handy when writing Python code!
# ============================================================================
