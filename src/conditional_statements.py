"""
Conditional Statements for Data Logic
======================================

This module demonstrates:
- Basic if statements
- if-else decision branching
- elif for multiple conditions
- Logical operators (and, or, not)
- Practical data-driven conditional logic

Author: Data Engineering Team
Date: March 2, 2026
"""

# ============================================================================
# 1. BASIC IF STATEMENTS
# ============================================================================

print("=" * 70)
print("1. BASIC IF STATEMENTS")
print("=" * 70)

# Simple numeric condition
age = 25
if age >= 18:
    print(f"Age {age}: You are an adult")

# Condition that is false (nothing prints)
salary = 35000
if salary > 100000:
    print(f"Salary {salary}: You have a high income")
print("(No output above because condition is false)\n")

# String comparison
department = "Engineering"
if department == "Engineering":
    print(f"Department: {department} - Welcome to the tech team!")

# String comparison with inequality
role = "Intern"
if role != "Manager":
    print(f"Role: {role} - You are not a manager\n")


# ============================================================================
# 2. IF–ELSE FOR DECISION BRANCHING
# ============================================================================

print("=" * 70)
print("2. IF–ELSE FOR DECISION BRANCHING")
print("=" * 70)

# Numeric branch
score = 72
if score >= 80:
    print(f"Score {score}: PASS with distinction")
else:
    print(f"Score {score}: PASS (needs improvement)")

# String branch
employee_status = "Part-Time"
if employee_status == "Full-Time":
    print(f"Status: {employee_status} - Eligible for full benefits")
else:
    print(f"Status: {employee_status} - Limited benefits package\n")

# Boolean-like conditions
is_manager = False
if is_manager:
    print("You have manager privileges")
else:
    print("You have standard user privileges\n")


# ============================================================================
# 3. HANDLING MULTIPLE CONDITIONS WITH ELIF
# ============================================================================

print("=" * 70)
print("3. HANDLING MULTIPLE CONDITIONS WITH ELIF")
print("=" * 70)

# Performance rating system
performance_score = 78

if performance_score >= 90:
    rating = "Excellent"
    action = "Recommend for promotion"
elif performance_score >= 80:
    rating = "Good"
    action = "Consider for advancement"
elif performance_score >= 70:
    rating = "Satisfactory"
    action = "Standard annual review"
else:
    rating = "Below Standard"
    action = "Performance improvement plan"

print(f"Performance Score: {performance_score}")
print(f"Rating: {rating}")
print(f"Action: {action}\n")

# Employee satisfaction survey response
satisfaction_level = "Neutral"

if satisfaction_level == "Very Satisfied":
    print("Thank you! We're glad you're happy!")
elif satisfaction_level == "Satisfied":
    print("Thank you for your feedback. We appreciate your support.")
elif satisfaction_level == "Neutral":
    print("We'd like to understand your concerns better.")
elif satisfaction_level == "Dissatisfied":
    print("We apologize. Please share feedback with HR.")
else:
    print("Unknown satisfaction level")

print()

# Grade conversion
grade_points = 3.7

if grade_points >= 3.8:
    grade_letter = "A"
elif grade_points >= 3.5:
    grade_letter = "A-"
elif grade_points >= 3.2:
    grade_letter = "B+"
elif grade_points >= 3.0:
    grade_letter = "B"
else:
    grade_letter = "Below B"

print(f"GPA {grade_points}: Grade {grade_letter}\n")


# ============================================================================
# 4. LOGICAL OPERATORS: AND, OR, NOT
# ============================================================================

print("=" * 70)
print("4. LOGICAL OPERATORS: AND, OR, NOT")
print("=" * 70)

# AND operator: ALL conditions must be true
age = 28
salary = 75000
has_experience = True

if age >= 25 and salary >= 50000 and has_experience:
    print("AND operator: All conditions true")
    print("✓ Eligible for senior position\n")

# Example where AND fails
age = 22
if age >= 25 and salary >= 50000:
    print("Eligible for senior position")
else:
    print(f"AND operator: Condition fails (age {age} < 25)")
    print("✗ Not eligible for senior position\n")

# OR operator: AT LEAST ONE condition must be true
experience_years = 3
has_certification = True

if experience_years >= 5 or has_certification:
    print("OR operator: At least one condition true")
    print("✓ Qualified for position (has certification)\n")

# Example where OR fails
experience_years = 1
has_certification = False

if experience_years >= 5 or has_certification:
    print("Qualified for position")
else:
    print(f"OR operator: Both conditions false")
    print("✗ Does not meet qualification requirements\n")

# NOT operator: INVERTS the condition
is_on_vacation = False

if not is_on_vacation:
    print("NOT operator: Condition inverted")
    print("✓ Employee is available for work\n")

is_approved = False
if not is_approved:
    print("NOT operator: Inverted false to true")
    print("✓ Request requires approval\n")


# ============================================================================
# 5. COMBINING OPERATORS FOR COMPLEX LOGIC
# ============================================================================

print("=" * 70)
print("5. COMBINING OPERATORS FOR COMPLEX LOGIC")
print("=" * 70)

# Complex business rule: Project assignment eligibility
skill_level = "Intermediate"
years_experience = 4
project_complexity = "High"
available = True

if (skill_level == "Advanced" or years_experience >= 5) and available:
    if project_complexity == "High":
        print("Complex condition 1: APPROVED")
        print("✓ Assigned to challenging project\n")

# Data validation: Check if a survey response is valid
response_value = 8
response_type = "numeric"

if isinstance(response_value, int) and not isinstance(response_value, bool):
    if 1 <= response_value <= 10:
        print("Complex condition 2: VALID")
        print(f"✓ Survey response {response_value} is valid (1-10 scale)\n")

# Multi-condition with negation
is_inactive = False
account_age_days = 15
is_flagged = False

if not is_inactive and account_age_days < 30 and not is_flagged:
    print("Complex condition 3: PASSED")
    print("✓ New account, active, no issues\n")


# ============================================================================
# 6. PRACTICAL DATA-DRIVEN SCENARIOS
# ============================================================================

print("=" * 70)
print("6. PRACTICAL DATA-DRIVEN SCENARIOS")
print("=" * 70)

# Scenario 1: Employee eligibility for bonus
base_salary = 55000
performance_rating = 4.2
years_with_company = 2

bonus_percentage = 0

if performance_rating >= 4.0:
    bonus_percentage = 15
elif performance_rating >= 3.5:
    bonus_percentage = 10
elif performance_rating >= 3.0:
    bonus_percentage = 5
else:
    bonus_percentage = 0

if years_with_company >= 2 and bonus_percentage > 0:
    bonus_amount = (base_salary * bonus_percentage) / 100
    print(f"Scenario 1: Bonus Calculation")
    print(f"✓ Performance Rating {performance_rating}: {bonus_percentage}% bonus")
    print(f"✓ Bonus Amount: ${bonus_amount:.2f}\n")
else:
    print(f"Scenario 1: No bonus (years: {years_with_company}, rating: {performance_rating})\n")

# Scenario 2: Data validation for survey response
survey_answers = [7, 8, "invalid", 9, 6]

print(f"Scenario 2: Survey Data Validation")
print(f"Survey Answers: {survey_answers}")

valid_count = 0
for answer in survey_answers:
    if isinstance(answer, int) and not isinstance(answer, bool) and 1 <= answer <= 10:
        print(f"  ✓ {answer} is valid")
        valid_count += 1
    else:
        print(f"  ✗ {answer} is invalid")

print(f"Valid Responses: {valid_count}/{len(survey_answers)}\n")

# Scenario 3: Risk assessment
age = 35
credit_score = 720
debt_to_income = 0.35

if credit_score >= 750:
    risk_level = "Low"
elif credit_score >= 700:
    if debt_to_income <= 0.4:
        risk_level = "Low"
    else:
        risk_level = "Medium"
elif credit_score >= 650:
    risk_level = "Medium"
else:
    risk_level = "High"

print(f"Scenario 3: Risk Assessment")
print(f"Credit Score: {credit_score}, Debt/Income: {debt_to_income}")
print(f"✓ Risk Level: {risk_level}\n")

# Scenario 4: Category assignment based on multiple factors
hours_worked = 38
is_salaried = True
department = "Engineering"

if is_salaried:
    employment_type = "Salaried"
elif hours_worked >= 35:
    employment_type = "Full-Time Hourly"
elif hours_worked >= 20:
    employment_type = "Part-Time"
else:
    employment_type = "Casual"

if department in ["Engineering", "Research", "Data Science"]:
    department_tier = "Technical"
elif department in ["Sales", "Marketing"]:
    department_tier = "Revenue"
else:
    department_tier = "Support"

print(f"Scenario 4: Employee Classification")
print(f"Employment Type: {employment_type}")
print(f"Department Tier: {department_tier}\n")


# ============================================================================
# 7. COMMON PITFALLS AND BEST PRACTICES
# ============================================================================

print("=" * 70)
print("7. COMMON PITFALLS AND BEST PRACTICES")
print("=" * 70)

# Pitfall 1: Using = instead of ==
print("Pitfall 1: Assignment vs Comparison")
value = 10
if value == 10:  # Correct: == for comparison
    print("✓ Correct: Using == for comparison")

# Pitfall 2: Indentation errors (shown in comments, not executed)
print("\nPitfall 2: Indentation")
if True:
    print("✓ Correct indentation: Code block indented")

# Pitfall 3: Unreachable code
print("\nPitfall 3: Unreachable Conditions")
x = 5
if x > 0:
    print("✓ x is positive")
elif x > 0:  # This branch never executes
    print("✗ This never runs (unreachable)")

# Pitfall 4: Forgetting to handle edge cases
print("\nPitfall 4: Edge Cases")
score = None
if score is None:
    print("✓ Handling None value correctly")

score = 0
if score > 0 and score <= 100:
    print("Valid score range")
else:
    print(f"✓ Edge case handled: score = {score}")

# Best Practice: Clear variable names and comments
print("\nBest Practice: Readability")
min_experience_required = 5
candidate_experience = 7

if candidate_experience >= min_experience_required:
    print("✓ Clear condition: candidate meets experience requirement")

# Best Practice: Simplify nested conditions when possible
print("\nBest Practice: Avoiding Deep Nesting")
status = "Active"
if status == "Active":
    print("✓ Simple, readable condition\n")


# ============================================================================
# SUMMARY
# ============================================================================

print("=" * 70)
print("SUMMARY: CONDITIONAL STATEMENTS MASTERY CHECKLIST")
print("=" * 70)

summary_items = [
    "✓ Basic if statements with single conditions",
    "✓ if-else for two-way decisions",
    "✓ elif for multiple conditions",
    "✓ Logical AND operator (all conditions required)",
    "✓ Logical OR operator (any condition allowed)",
    "✓ Logical NOT operator (condition inversion)",
    "✓ Combined conditions with multiple operators",
    "✓ Practical data validation scenarios",
    "✓ Risk assessment logic",
    "✓ Employee classification based on multiple factors",
    "✓ Handling edge cases (None, 0, empty values)",
    "✓ Avoiding common pitfalls (indentation, unreachable code)"
]

for item in summary_items:
    print(item)

print("\n" + "=" * 70)
print("All conditional statement concepts demonstrated successfully!")
print("=" * 70)
