"""
Code Structure Fundamentals - Learning Unit 4.21
Structuring Python Code for Readability and Reuse

This module demonstrates:
1. Organizing Code into Logical Sections
2. Using Functions for Reuse (DRY Principle)
3. Separating Logic from Execution
4. Writing Readable, Maintainable Code
5. Before/After Restructuring Examples

Author: Trivin Insight Engine
Date: March 3, 2026
"""

# ============================================================================
# IMPORTS SECTION
# Always place imports at the top of the file
# ============================================================================
import math
from datetime import datetime


# ============================================================================
# CONSTANTS AND CONFIGURATION
# Group related constants together
# ============================================================================
MAX_EMPLOYEE_COUNT = 1000
DEFAULT_DEPARTMENT = "General"
SURVEY_SCALE_MIN = 1
SURVEY_SCALE_MAX = 5
COMPANY_NAME = "Trivin Insight Engine"


# ============================================================================
# HELPER FUNCTIONS
# Define reusable functions before main execution logic
# ============================================================================

def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def calculate_percentage(value, total):
    """
    Calculate percentage from value and total.
    
    Args:
        value: The partial value
        total: The total value
        
    Returns:
        Percentage as a float (0-100)
    """
    if total == 0:
        return 0.0
    return (value / total) * 100


def format_currency(amount):
    """
    Format a number as currency.
    
    Args:
        amount: The amount to format
        
    Returns:
        Formatted string with $ and comma separators
    """
    return f"${amount:,.2f}"


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        Average as a float, or 0 if list is empty
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


# ============================================================================
# DEMONSTRATION FUNCTIONS
# Each function demonstrates a specific concept
# ============================================================================

def demonstrate_section_organization():
    """Demonstrate organizing code into logical sections"""
    section_header("1. Organizing Code into Logical Sections")
    
    print("\n--- Well-Organized Script Structure ---")
    print("""
    1. Module docstring (explains purpose)
    2. Imports (standard library, third-party, local)
    3. Constants and configuration
    4. Helper functions (utilities)
    5. Main logic functions
    6. Execution code (if __name__ == "__main__")
    """)
    
    print("\n✓ This structure makes code predictable and easy to navigate")
    print("✓ Anyone reading your code knows where to find things")


def demonstrate_function_reuse():
    """Demonstrate using functions to avoid code repetition"""
    section_header("2. Using Functions for Reuse (DRY Principle)")
    
    print("\n--- WITHOUT Functions (Repetitive) ---")
    print("Code:")
    print("  total_employees = 450")
    print("  surveyed = 360")
    print("  response_rate = (surveyed / total_employees) * 100")
    print("  print(f'Response rate: {response_rate:.1f}%')")
    print()
    print("  total_tasks = 200")
    print("  completed = 175")
    print("  completion_rate = (completed / total_tasks) * 100")
    print("  print(f'Completion rate: {completion_rate:.1f}%')")
    
    print("\n--- WITH Functions (Reusable) ---")
    
    # Using our reusable function
    total_employees = 450
    surveyed = 360
    response_rate = calculate_percentage(surveyed, total_employees)
    print(f"Response rate: {response_rate:.1f}%")
    
    total_tasks = 200
    completed = 175
    completion_rate = calculate_percentage(completed, total_tasks)
    print(f"Completion rate: {completion_rate:.1f}%")
    
    print("\n✓ Function is defined once, used multiple times")
    print("✓ Changes need to be made in only one place")
    print("✓ Code is shorter and more maintainable")


def demonstrate_logic_separation():
    """Demonstrate separating setup, logic, and execution"""
    section_header("3. Separating Logic from Execution")
    
    print("\n--- Poor Structure (Everything Mixed) ---")
    print("""
    # Calculation mixed with data
    salary = 75000
    bonus_percent = 0.15
    bonus = salary * bonus_percent
    print(bonus)
    
    department = "Sales"
    another_salary = 82000
    another_bonus = another_salary * 0.15
    print(another_bonus)
    """)
    
    print("--- Good Structure (Separated and Clear) ---")
    
    # Define the function first
    def calculate_bonus(salary, bonus_percent=0.15):
        """Calculate employee bonus based on salary"""
        return salary * bonus_percent
    
    # Then use it in execution
    print("\nExecution:")
    employee_salary = 75000
    employee_bonus = calculate_bonus(employee_salary)
    print(f"  Employee 1 bonus: {format_currency(employee_bonus)}")
    
    manager_salary = 82000
    manager_bonus = calculate_bonus(manager_salary, 0.20)
    print(f"  Manager bonus: {format_currency(manager_bonus)}")
    
    print("\n✓ Functions defined at the top")
    print("✓ Execution code is clean and readable")
    print("✓ Logic is separated from data")


def demonstrate_readable_code():
    """Demonstrate writing readable, maintainable code"""
    section_header("4. Writing Readable, Maintainable Code")
    
    print("\n--- Characteristics of Readable Code ---")
    print("✓ Clear variable and function names")
    print("✓ Consistent formatting and spacing")
    print("✓ Logical grouping of related code")
    print("✓ Comments explain WHY, not WHAT")
    print("✓ Functions do one thing well")
    
    print("\n--- Example: Processing Survey Scores ---")
    
    # Sample data
    survey_scores = [4, 5, 3, 4, 5, 4, 3, 5, 4, 4]
    
    # Calculate metrics (readable and clear)
    average_score = calculate_average(survey_scores)
    max_score = max(survey_scores)
    min_score = min(survey_scores)
    total_responses = len(survey_scores)
    
    print(f"\nSurvey Results:")
    print(f"  Total responses: {total_responses}")
    print(f"  Average score: {average_score:.2f}")
    print(f"  Highest score: {max_score}")
    print(f"  Lowest score: {min_score}")
    
    # Calculate satisfaction percentage
    satisfaction_percentage = calculate_percentage(
        average_score, 
        SURVEY_SCALE_MAX
    )
    print(f"  Satisfaction rate: {satisfaction_percentage:.1f}%")
    
    print("\n✓ Each step is clear and purposeful")
    print("✓ Functions make the code self-documenting")


def demonstrate_before_after_refactoring():
    """Show a real example of poorly structured vs well-structured code"""
    section_header("5. Before/After Restructuring Example")
    
    print("\n--- BEFORE: Poorly Structured Code ---")
    print("""
    # Everything in one block, hard to follow
    d = [85000, 92000, 78000, 95000]
    t = 0
    for x in d:
        t = t + x
    avg = t / len(d)
    print("Avg:", avg)
    
    # More unrelated code mixed in
    s = [4, 5, 3, 4]
    total = 0
    for val in s:
        total = total + val
    score_avg = total / len(s)
    print("Score:", score_avg)
    """)
    
    print("\n--- AFTER: Well-Structured Code ---")
    print("\nCode:")
    
    # Clear data definitions
    employee_salaries = [85000, 92000, 78000, 95000]
    survey_scores = [4, 5, 3, 4]
    
    # Reusable function (defined earlier in the file)
    # def calculate_average(numbers):
    #     """Calculate average of a list of numbers"""
    #     if not numbers:
    #         return 0.0
    #     return sum(numbers) / len(numbers)
    
    # Clean execution using the function
    average_salary = calculate_average(employee_salaries)
    average_score = calculate_average(survey_scores)
    
    print("\nResults:")
    print(f"  Average salary: {format_currency(average_salary)}")
    print(f"  Average survey score: {average_score:.2f}")
    
    print("\n✓ Variable names are descriptive")
    print("✓ Logic is reusable through functions")
    print("✓ Code reads like a story from top to bottom")
    print("✓ Easy to modify, test, and extend")


# ============================================================================
# MAIN EXECUTION
# Keep this section clean and high-level
# ============================================================================

def main():
    """
    Main function that runs all demonstrations.
    This keeps the top-level execution clean and organized.
    """
    print("=" * 70)
    print(f"  {COMPANY_NAME}")
    print("  CODE STRUCTURE FUNDAMENTALS")
    print("  Learning Unit 4.21")
    print("=" * 70)
    print(f"\n  Date: {datetime.now().strftime('%B %d, %Y')}")
    print("  Topic: Structuring Python Code for Readability and Reuse")
    
    # Run all demonstrations in order
    demonstrate_section_organization()
    demonstrate_function_reuse()
    demonstrate_logic_separation()
    demonstrate_readable_code()
    demonstrate_before_after_refactoring()
    
    # Summary
    section_header("KEY TAKEAWAYS")
    print("""
    1. Organize code into clear sections (imports, constants, functions, execution)
    2. Use functions to avoid repetition (DRY: Don't Repeat Yourself)
    3. Define functions before using them
    4. Keep execution code minimal and readable
    5. Write code that others can understand without your help
    
    Well-structured code is:
    - Easier to read and understand
    - Easier to debug and test
    - Easier to modify and extend
    - Easier to collaborate on
    
    Structure turns working code into maintainable code!
    """)
    
    print("=" * 70)
    print("  End of demonstration")
    print("=" * 70)


# ============================================================================
# ENTRY POINT
# This ensures code only runs when the file is executed directly
# ============================================================================

if __name__ == "__main__":
    main()
