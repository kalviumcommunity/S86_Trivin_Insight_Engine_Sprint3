"""
Data Types Fundamentals - Learning Unit 4.14
Understanding Python Numeric and String Data Types

This module demonstrates:
1. Working with Numeric Data Types
2. Understanding String Data Types
3. Mixing Numbers and Strings Safely
4. Inspecting Data Types

Author: Trivin Insight Engine
Date: February 27, 2026
"""


def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


# ============================================================================
# 1. WORKING WITH NUMERIC DATA TYPES
# ============================================================================

def demonstrate_numeric_types():
    """Demonstrate integers and floating-point numbers"""
    section_header("1. Working with Numeric Data Types")
    
    # Integer examples
    print("\n--- INTEGER EXAMPLES ---")
    employees_count = 50
    survey_responses = 42
    departments = 5
    
    print(f"Number of employees: {employees_count}")
    print(f"Survey responses received: {survey_responses}")
    print(f"Number of departments: {departments}")
    print(f"Type of 'employees_count': {type(employees_count)}")
    
    # Float examples
    print("\n--- FLOATING-POINT EXAMPLES ---")
    average_satisfaction = 4.2
    response_rate = 84.5
    average_tenure = 3.75
    
    print(f"Average satisfaction score: {average_satisfaction}")
    print(f"Response rate: {response_rate}%")
    print(f"Average tenure (years): {average_tenure}")
    print(f"Type of 'average_satisfaction': {type(average_satisfaction)}")
    
    # Basic arithmetic operations
    print("\n--- ARITHMETIC OPERATIONS ---")
    total_employees = 100
    present_employees = 87
    
    absent_employees = total_employees - present_employees
    attendance_percentage = (present_employees / total_employees) * 100
    
    print(f"Total employees: {total_employees}")
    print(f"Present employees: {present_employees}")
    print(f"Absent employees: {absent_employees}")
    print(f"Attendance percentage: {attendance_percentage}%")
    
    # Division behavior
    print("\n--- DIVISION BEHAVIOR ---")
    total_hours = 40
    work_days = 5
    
    hours_per_day = total_hours / work_days  # Regular division (float result)
    hours_per_day_int = total_hours // work_days  # Floor division (integer result)
    remainder = total_hours % 7  # Modulo (remainder)
    
    print(f"Hours per day (regular division): {hours_per_day}")
    print(f"Hours per day (floor division): {hours_per_day_int}")
    print(f"Remainder when 40 divided by 7: {remainder}")
    
    # Power and complex operations
    print("\n--- POWER AND COMPLEX OPERATIONS ---")
    base_salary = 50000
    annual_raise = 1.05  # 5% raise
    years = 3
    
    future_salary = base_salary * (annual_raise ** years)
    print(f"Starting salary: ${base_salary:,.2f}")
    print(f"Salary after {years} years with 5% annual raise: ${future_salary:,.2f}")


# ============================================================================
# 2. UNDERSTANDING STRING DATA TYPES
# ============================================================================

def demonstrate_string_types():
    """Demonstrate string creation and manipulation"""
    section_header("2. Understanding String Data Types")
    
    # Creating strings
    print("\n--- CREATING STRINGS ---")
    employee_name = "Sarah Johnson"
    department = 'Engineering'
    job_title = """Senior Data Analyst"""
    
    print(f"Employee name: {employee_name}")
    print(f"Department: {department}")
    print(f"Job title: {job_title}")
    print(f"Type of 'employee_name': {type(employee_name)}")
    
    # String concatenation
    print("\n--- STRING CONCATENATION ---")
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    
    greeting = "Hello, " + full_name + "!"
    print(greeting)
    
    # String repetition
    divider = "-" * 40
    print(divider)
    
    # Accessing string characters
    print("\n--- ACCESSING STRING CHARACTERS ---")
    company = "Trivin Insights"
    print(f"First character: {company[0]}")
    print(f"Last character: {company[-1]}")
    print(f"First 6 characters: {company[0:6]}")
    print(f"Characters from index 7 onwards: {company[7:]}")
    
    # String length
    print(f"Length of company name: {len(company)} characters")
    
    # String methods
    print("\n--- STRING METHODS ---")
    message = "  Python Data Types  "
    print(f"Original: '{message}'")
    print(f"Uppercase: '{message.upper()}'")
    print(f"Lowercase: '{message.lower()}'")
    print(f"Stripped: '{message.strip()}'")
    print(f"Replaced: '{message.replace('Python', 'Advanced')}'")
    
    # Multi-line strings
    print("\n--- MULTI-LINE STRINGS ---")
    report = """
    Employee Survey Summary:
    - Total Responses: 42
    - Average Rating: 4.2
    - Completion Rate: 84%
    """
    print(report)
    
    # String formatting
    print("\n--- STRING FORMATTING ---")
    name = "Alice"
    score = 87.5
    rank = 3
    
    # f-string formatting
    result1 = f"{name} scored {score}% and ranked #{rank}"
    print(f"F-string: {result1}")
    
    # Format method
    result2 = "{} scored {}% and ranked #{}".format(name, score, rank)
    print(f"Format method: {result2}")
    
    # Old-style formatting
    result3 = "%s scored %.1f%% and ranked #%d" % (name, score, rank)
    print(f"Old-style: {result3}")


# ============================================================================
# 3. MIXING NUMBERS AND STRINGS SAFELY
# ============================================================================

def demonstrate_type_mixing():
    """Demonstrate safe type mixing and conversion"""
    section_header("3. Mixing Numbers and Strings Safely")
    
    # Common error: trying to mix types incorrectly
    print("\n--- TYPE MIXING ERRORS ---")
    age = 30
    print(f"Age variable: {age} (type: {type(age).__name__})")
    
    # This would cause an error (commented out):
    # message = "Age is " + age  # TypeError!
    print("❌ Cannot concatenate: 'Age is ' + 30  (TypeError)")
    
    # Correct approach: convert number to string
    print("\n--- CORRECT TYPE CONVERSION ---")
    message = "Age is " + str(age)
    print(f"✓ Correct: 'Age is ' + str(30) = '{message}'")
    
    # Converting strings to numbers
    print("\n--- STRING TO NUMBER CONVERSION ---")
    text_number = "42"
    text_float = "3.14"
    
    print(f"String number: '{text_number}' (type: {type(text_number).__name__})")
    
    number_value = int(text_number)
    float_value = float(text_float)
    
    print(f"Converted to int: {number_value} (type: {type(number_value).__name__})")
    print(f"Converted to float: {float_value} (type: {type(float_value).__name__})")
    
    # Arithmetic after conversion
    print("\n--- ARITHMETIC AFTER CONVERSION ---")
    score1_str = "85"
    score2_str = "92"
    
    # Wrong: string concatenation
    wrong_result = score1_str + score2_str
    print(f"String concatenation: '{score1_str}' + '{score2_str}' = '{wrong_result}'")
    
    # Correct: convert then add
    correct_result = int(score1_str) + int(score2_str)
    print(f"After conversion: {int(score1_str)} + {int(score2_str)} = {correct_result}")
    
    # Using f-strings (automatic conversion)
    print("\n--- F-STRING AUTOMATIC FORMATTING ---")
    employee_id = 12345
    satisfaction = 4.5
    
    report = f"Employee #{employee_id} has satisfaction rating of {satisfaction}"
    print(report)
    
    # Be careful with numeric strings
    print("\n--- NUMERIC STRING PITFALLS ---")
    value1 = "100"
    value2 = "200"
    
    # String concatenation (not addition!)
    string_result = value1 + value2
    print(f"String concatenation: '{value1}' + '{value2}' = '{string_result}'")
    
    # Proper numeric addition
    numeric_result = int(value1) + int(value2)
    print(f"Numeric addition: {int(value1)} + {int(value2)} = {numeric_result}")
    
    # Handling conversion errors
    print("\n--- HANDLING CONVERSION ERRORS ---")
    invalid_number = "abc"
    print(f"Trying to convert '{invalid_number}' to int...")
    
    try:
        result = int(invalid_number)
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("✓ Solution: Validate data before conversion")


# ============================================================================
# 4. INSPECTING DATA TYPES
# ============================================================================

def demonstrate_type_inspection():
    """Demonstrate how to check and validate data types"""
    section_header("4. Inspecting Data Types")
    
    # Using type() function
    print("\n--- USING type() FUNCTION ---")
    variables = {
        "integer": 42,
        "float": 3.14,
        "string": "Hello",
        "boolean": True,
        "list": [1, 2, 3],
        "dict": {"key": "value"},
        "none": None
    }
    
    for var_name, var_value in variables.items():
        print(f"{var_name:15} = {str(var_value):20} → type: {type(var_value).__name__}")
    
    # Using isinstance() for type checking
    print("\n--- USING isinstance() FOR TYPE CHECKING ---")
    test_values = [42, 3.14, "text", True, [1, 2], None]
    
    for value in test_values:
        is_int = isinstance(value, int)
        is_float = isinstance(value, float)
        is_str = isinstance(value, str)
        is_bool = isinstance(value, bool)
        
        print(f"Value: {str(value):10} → int: {is_int}, float: {is_float}, str: {is_str}, bool: {is_bool}")
    
    # Type checking in practice
    print("\n--- TYPE CHECKING IN PRACTICE ---")
    
    def calculate_bonus(salary, bonus_rate):
        """Calculate bonus with type validation"""
        # Check if inputs are numeric
        if not isinstance(salary, (int, float)):
            return f"Error: salary must be numeric, got {type(salary).__name__}"
        
        if not isinstance(bonus_rate, (int, float)):
            return f"Error: bonus_rate must be numeric, got {type(bonus_rate).__name__}"
        
        bonus = salary * bonus_rate
        return f"Bonus: ${bonus:,.2f}"
    
    # Test with correct types
    print(calculate_bonus(50000, 0.10))
    
    # Test with incorrect types
    print(calculate_bonus("50000", 0.10))
    print(calculate_bonus(50000, "10%"))
    
    # Checking numeric vs string
    print("\n--- DISTINGUISHING NUMERIC VS STRING ---")
    values = [100, "100", 3.14, "3.14", True, "True"]
    
    for val in values:
        type_name = type(val).__name__
        is_numeric = isinstance(val, (int, float)) and not isinstance(val, bool)
        is_string = isinstance(val, str)
        
        print(f"{str(val):10} → Type: {type_name:7} | Numeric: {is_numeric} | String: {is_string}")


# ============================================================================
# 5. PRACTICAL EXAMPLES
# ============================================================================

def demonstrate_practical_examples():
    """Real-world examples using data types correctly"""
    section_header("5. Practical Data Type Examples")
    
    print("\n--- EMPLOYEE DATA PROCESSING ---")
    
    # Employee information (mixed types)
    employee_id = 1001
    employee_name = "Jennifer Smith"
    department = "Data Science"
    years_experience = 5
    salary = 75000.00
    is_full_time = True
    performance_score = 4.7
    
    # Display employee information
    print(f"Employee ID: {employee_id} (type: {type(employee_id).__name__})")
    print(f"Name: {employee_name} (type: {type(employee_name).__name__})")
    print(f"Department: {department} (type: {type(department).__name__})")
    print(f"Experience: {years_experience} years (type: {type(years_experience).__name__})")
    print(f"Salary: ${salary:,.2f} (type: {type(salary).__name__})")
    print(f"Full-time: {is_full_time} (type: {type(is_full_time).__name__})")
    print(f"Performance: {performance_score}/5.0 (type: {type(performance_score).__name__})")
    
    # Calculations
    print("\n--- SALARY CALCULATIONS ---")
    monthly_salary = salary / 12
    weekly_salary = salary / 52
    hourly_rate = salary / (52 * 40)
    
    print(f"Annual Salary: ${salary:,.2f}")
    print(f"Monthly Salary: ${monthly_salary:,.2f}")
    print(f"Weekly Salary: ${weekly_salary:,.2f}")
    print(f"Hourly Rate: ${hourly_rate:,.2f}")
    
    # String formatting for reports
    print("\n--- FORMATTED EMPLOYEE REPORT ---")
    report = f"""
    {'=' * 50}
    EMPLOYEE PERFORMANCE REPORT
    {'=' * 50}
    
    Employee Details:
    - ID Number: {employee_id}
    - Full Name: {employee_name}
    - Department: {department}
    - Employment Status: {'Full-Time' if is_full_time else 'Part-Time'}
    
    Compensation:
    - Annual Salary: ${salary:,.2f}
    - Monthly Salary: ${monthly_salary:,.2f}
    - Hourly Rate: ${hourly_rate:,.2f}
    
    Performance:
    - Years of Experience: {years_experience}
    - Performance Score: {performance_score}/5.0
    - Rating: {'Excellent' if performance_score >= 4.5 else 'Good' if performance_score >= 3.5 else 'Needs Improvement'}
    
    {'=' * 50}
    """
    print(report)
    
    # Survey score aggregation
    print("\n--- SURVEY SCORE AGGREGATION ---")
    score1, score2, score3, score4, score5 = 5, 4, 5, 3, 4
    
    total_score = score1 + score2 + score3 + score4 + score5
    count = 5
    average_score = total_score / count
    
    print(f"Individual scores: {score1}, {score2}, {score3}, {score4}, {score5}")
    print(f"Total score: {total_score}")
    print(f"Number of responses: {count}")
    print(f"Average score: {average_score:.2f}")
    print(f"Percentage: {(average_score / 5) * 100:.1f}%")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all demonstrations"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*  LEARNING UNIT 4.14: PYTHON NUMERIC AND STRING TYPES   *")
    print("*  Understanding Data Types Fundamentals                 *")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    
    # Run all demonstrations
    demonstrate_numeric_types()
    demonstrate_string_types()
    demonstrate_type_mixing()
    demonstrate_type_inspection()
    demonstrate_practical_examples()
    
    # Summary
    section_header("Summary and Key Takeaways")
    print("""
    ✓ Numeric Types: int and float represent numbers
    ✓ String Types: str represents text data
    ✓ Type Conversion: Use str(), int(), float() to convert between types
    ✓ Type Inspection: Use type() and isinstance() to check types
    ✓ Best Practice: Always validate data types before operations
    ✓ Common Errors: Mixing types without conversion causes TypeError
    
    Understanding data types prevents bugs and makes code more reliable!
    """)
    
    print("\n" + "=" * 60)
    print("  Demonstration Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
