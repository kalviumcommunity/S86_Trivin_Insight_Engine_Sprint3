"""
Code Readability Fundamentals - Learning Unit 4.20
Writing Readable Variable Names and Comments (PEP 8 Basics)

This module demonstrates:
1. Writing Readable Variable Names
2. Following PEP 8 Naming Conventions
3. Writing Useful Comments
4. Avoiding Common Readability Mistakes
5. Refactoring an Unreadable Example

Author: Trivin Insight Engine
Date: March 3, 2026
"""


def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# ============================================================================
# 1. WRITING READABLE VARIABLE NAMES
# ============================================================================

def demonstrate_readable_variable_names():
    """Demonstrate clear, descriptive variable names"""
    section_header("1. Writing Readable Variable Names")

    print("--- Poor vs Good Variable Names ---")

    # Poor naming
    x = 42
    tmp = 0.84
    val = "Engineering"

    print("Poor names example:")
    print(f"  x = {x}")
    print(f"  tmp = {tmp}")
    print(f"  val = {val}")

    # Improved naming
    total_employee_count = 42
    survey_response_rate = 0.84
    employee_department_name = "Engineering"

    print("\nReadable names example:")
    print(f"  total_employee_count = {total_employee_count}")
    print(f"  survey_response_rate = {survey_response_rate}")
    print(f"  employee_department_name = {employee_department_name}")

    print("\n✓ Good names describe meaning without extra comments")


# ============================================================================
# 2. FOLLOWING PEP 8 NAMING CONVENTIONS
# ============================================================================

def demonstrate_pep8_naming():
    """Demonstrate basic PEP 8 naming conventions"""
    section_header("2. Following PEP 8 Naming Conventions")

    # Variables use snake_case
    average_satisfaction_score = 4.3
    monthly_turnover_rate = 0.06

    # Constants use UPPER_CASE_WITH_UNDERSCORES
    MAX_ALLOWED_LOGIN_ATTEMPTS = 5
    DEFAULT_SURVEY_SCALE_MAX = 5

    # Consistent naming in the same context
    first_quarter_responses = 120
    second_quarter_responses = 138
    third_quarter_responses = 126

    print("Variables (snake_case):")
    print(f"  average_satisfaction_score = {average_satisfaction_score}")
    print(f"  monthly_turnover_rate = {monthly_turnover_rate}")

    print("\nConstants (UPPER_CASE):")
    print(f"  MAX_ALLOWED_LOGIN_ATTEMPTS = {MAX_ALLOWED_LOGIN_ATTEMPTS}")
    print(f"  DEFAULT_SURVEY_SCALE_MAX = {DEFAULT_SURVEY_SCALE_MAX}")

    print("\nConsistent naming across related variables:")
    print(f"  first_quarter_responses = {first_quarter_responses}")
    print(f"  second_quarter_responses = {second_quarter_responses}")
    print(f"  third_quarter_responses = {third_quarter_responses}")

    print("\n✓ Consistency improves readability instantly")


# ============================================================================
# 3. WRITING USEFUL COMMENTS
# ============================================================================

def demonstrate_useful_comments():
    """Demonstrate useful comments that explain intent"""
    section_header("3. Writing Useful Comments")

    print("--- Comment Quality Examples ---")

    print("\nPoor comment (explains obvious operation):")
    print("  total_score = score_a + score_b  # add two scores")

    print("\nUseful comment (explains intent/why):")
    print("  # Normalize to 0-1 range so dashboards can compare metrics")
    print("  normalized_score = raw_score / max_possible_score")

    raw_score = 42
    max_possible_score = 50

    # Normalize score to a common scale so different surveys are comparable.
    normalized_score = raw_score / max_possible_score

    print("\nApplied useful comment example:")
    print(f"  raw_score = {raw_score}")
    print(f"  max_possible_score = {max_possible_score}")
    print(f"  normalized_score = {normalized_score:.2f}")

    print("\n✓ Good comments explain non-obvious intent")


# ============================================================================
# 4. AVOIDING COMMON READABILITY MISTAKES
# ============================================================================

def demonstrate_readability_mistakes_to_avoid():
    """Show common readability mistakes and better alternatives"""
    section_header("4. Avoiding Common Readability Mistakes")

    print("--- Mistake 1: Commented-out code ---")
    print("Avoid leaving disabled code in final files.")
    print("Better: delete unused code and rely on version control history.")

    print("\n--- Mistake 2: Misleading comments ---")
    print("Comment says one thing, code does another -> causes review confusion.")
    print("Better: keep comments aligned whenever code changes.")

    print("\n--- Mistake 3: Inconsistent naming styles ---")
    print("Bad mix: totalEmployees, total_employees, TotalEmployees")
    print("Better: choose snake_case and stay consistent.")

    print("\n--- Mistake 4: Over-commenting simple lines ---")
    print("Bad: value = 10  # set value to 10")
    print("Better: remove obvious comments, keep only valuable ones.")

    print("\n✓ Readable code builds reviewer trust")


# ============================================================================
# 5. REFACTORING AN UNREADABLE EXAMPLE
# ============================================================================

def demonstrate_refactoring_example():
    """Refactor poor naming/comments into readable code"""
    section_header("5. Refactoring an Unreadable Example")

    print("--- Before (hard to read) ---")
    print("a = 5")
    print("b = 3")
    print("c = a / (a + b)")
    print("# divide")

    dissatisfied_employee_count = 5
    satisfied_employee_count = 3

    # Compute dissatisfaction ratio for quick trend comparison across teams.
    dissatisfaction_ratio = dissatisfied_employee_count / (
        dissatisfied_employee_count + satisfied_employee_count
    )

    print("\n--- After (readable and review-ready) ---")
    print(f"dissatisfied_employee_count = {dissatisfied_employee_count}")
    print(f"satisfied_employee_count = {satisfied_employee_count}")
    print(f"dissatisfaction_ratio = {dissatisfaction_ratio:.3f}")

    print("\n✓ Same logic, much clearer intent")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all demonstrations"""
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*  LEARNING UNIT 4.20: READABLE NAMES & COMMENTS (PEP 8)      *")
    print("*  Write Clean, Review-Ready Python for Team Collaboration     *")
    print("*" + " " * 68 + "*")
    print("*" * 70)

    demonstrate_readable_variable_names()
    demonstrate_pep8_naming()
    demonstrate_useful_comments()
    demonstrate_readability_mistakes_to_avoid()
    demonstrate_refactoring_example()

    section_header("Summary and Key Takeaways")
    print("""
    VARIABLE NAMING:
    ✓ Use descriptive names that communicate intent
    ✓ Avoid vague names like x, tmp, val
    ✓ Prefer snake_case for variables in Python

    PEP 8 BASICS:
    ✓ Use lowercase_with_underscores for variables
    ✓ Use UPPER_CASE for constants
    ✓ Keep naming consistent across the file

    COMMENT QUALITY:
    ✓ Explain WHY, not obvious WHAT
    ✓ Add comments only where they provide value
    ✓ Keep comments short, clear, and accurate

    READABILITY HABITS:
    ✓ Remove commented-out code
    ✓ Avoid misleading or outdated comments
    ✓ Write code for humans first, machines second

    Readable code is a professional skill that improves collaboration,
    debugging speed, and long-term maintainability.
    """)

    print("\n" + "=" * 70)
    print("  Demonstration Complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
