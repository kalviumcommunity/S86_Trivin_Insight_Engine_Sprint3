"""
Functions Fundamentals - Learning Unit 4.19
Passing Data into Functions and Returning Results

This module demonstrates:
1. Understanding Parameters and Arguments
2. Passing Data into Functions
3. The Return Statement
4. Using Returned Values in Further Computation
5. Avoiding Common Function Mistakes
6. Real-World Function Patterns

Author: Trivin Insight Engine
Date: March 3, 2026
"""


def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# ============================================================================
# 1. UNDERSTANDING PARAMETERS AND ARGUMENTS
# ============================================================================

def demonstrate_parameters_and_arguments():
    """Demonstrate parameters, arguments, and how data flows in"""
    section_header("1. Understanding Parameters and Arguments")

    # Simple function with one parameter
    def greet_user(name):
        """Simple function that accepts one parameter"""
        print(f"Hello, {name}! Welcome to our program.")

    print("\n--- Calling with different arguments ---")
    greet_user("Alice")
    greet_user("Bob")
    greet_user("Aarav")

    # Function with multiple parameters
    def calculate_total_cost(price, quantity, tax_rate=0.1):
        """Calculate total cost with optional tax"""
        subtotal = price * quantity
        tax = subtotal * tax_rate
        total = subtotal + tax
        return total

    print("\n--- Functions with multiple parameters ---")
    print(f"Price per item: $10, Quantity: 5, Tax: 10%")
    print(f"Total cost: ${calculate_total_cost(10, 5):.2f}")
    
    print(f"\nPrice per item: $25, Quantity: 3, Tax: 8%")
    print(f"Total cost: ${calculate_total_cost(25, 3, 0.08):.2f}")

    print("\n✓ Parameters (in function definition) vs Arguments (in function call)")
    print("✓ Order matters for positional arguments")
    print("✓ Keyword arguments allow flexibility and clarity")


# ============================================================================
# 2. PASSING DATA INTO FUNCTIONS
# ============================================================================

def demonstrate_passing_data():
    """Demonstrate various ways to pass data into functions"""
    section_header("2. Passing Data into Functions")

    # Positional arguments
    def describe_employee(name, age, salary):
        """Take employee data and use it"""
        return f"{name} is {age} years old and earns ${salary:,.2f}"

    print("--- Positional Arguments (order matters) ---")
    result1 = describe_employee("Priya", 28, 75000)
    print(result1)
    
    result2 = describe_employee("James", 35, 95000)
    print(result2)

    # Keyword arguments (order doesn't matter)
    print("\n--- Keyword Arguments (flexible order) ---")
    result3 = describe_employee(salary=85000, name="Kaito", age=32)
    print(result3)

    # Mix of positional and keyword
    print("\n--- Mixed Arguments ---")
    result4 = describe_employee("Sofia", age=29, salary=82000)
    print(result4)

    # Default parameters
    def apply_discount(price, discount_percent=10):
        """Apply a discount with a default value"""
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price

    print("\n--- Functions with Default Parameters ---")
    print(f"Item price: $100, Default 10% discount: ${apply_discount(100):.2f}")
    print(f"Item price: $100, Custom 25% discount: ${apply_discount(100, 25):.2f}")

    print("\n✓ Data flows INTO functions through parameters")


# ============================================================================
# 3. THE RETURN STATEMENT
# ============================================================================

def demonstrate_return_statement():
    """Demonstrate the return statement and how data flows out"""
    section_header("3. The Return Statement")

    # Function that returns a single value
    def calculate_average(score1, score2, score3):
        """Return average of three scores"""
        average = (score1 + score2 + score3) / 3
        return average

    print("--- Returning a Single Value ---")
    result = calculate_average(85, 90, 78)
    print(f"Function returned: {result}")
    print(f"We can store this in a variable: result = {result:.2f}")

    # Function that returns different values
    def check_score_status(score):
        """Return pass or fail status"""
        if score >= 70:
            return "PASS"
        else:
            return "FAIL"

    print("\n--- Different Return Paths ---")
    status1 = check_score_status(85)
    status2 = check_score_status(55)
    print(f"Score 85: {status1}")
    print(f"Score 55: {status2}")

    # Function that returns multiple values
    def get_budget_summary(income, expenses):
        """Return multiple values (tuple)"""
        savings = income - expenses
        savings_percent = (savings / income) * 100 if income > 0 else 0
        return savings, savings_percent

    print("\n--- Returning Multiple Values ---")
    money_saved, percent_saved = get_budget_summary(5000, 3500)
    print(f"Money saved: ${money_saved}")
    print(f"Savings percentage: {percent_saved:.1f}%")

    # Function that doesn't explicitly return anything
    def just_prints_data(message):
        """This function only prints, doesn't return"""
        print(f"Message: {message}")

    print("\n--- No Return Statement (returns None) ---")
    result_none = just_prints_data("This doesn't return anything")
    print(f"The returned value is: {result_none}")

    print("\n✓ Return sends data OUT of functions")
    print("✓ Without return, a function returns None")
    print("✓ Avoid mixing print statements with return statements")


# ============================================================================
# 4. USING RETURNED VALUES IN FURTHER COMPUTATION
# ============================================================================

def demonstrate_using_returned_values():
    """Demonstrate composing functions and reusing results"""
    section_header("4. Using Returned Values in Further Computation")

    # Helper functions
    def calculate_base_salary(hourly_rate, hours_per_week, weeks_per_year):
        """Calculate annual base salary"""
        return hourly_rate * hours_per_week * weeks_per_year

    def apply_bonus(base_salary, bonus_percent):
        """Add a bonus to base salary"""
        bonus = base_salary * (bonus_percent / 100)
        return base_salary + bonus

    def calculate_taxes(gross_salary, tax_rate):
        """Calculate tax amount"""
        return gross_salary * (tax_rate / 100)

    print("--- Chaining Function Results ---")
    hourly_rate = 35
    hours_per_week = 40
    weeks_per_year = 52

    # Step 1: Calculate base salary
    base = calculate_base_salary(hourly_rate, hours_per_week, weeks_per_year)
    print(f"Base salary: ${base:,.2f}")

    # Step 2: Add bonus using the result from step 1
    with_bonus = apply_bonus(base, 15)
    print(f"Salary with 15% bonus: ${with_bonus:,.2f}")

    # Step 3: Calculate taxes using the result from step 2
    taxes = calculate_taxes(with_bonus, 20)
    print(f"Taxes (20%): ${taxes:,.2f}")

    # Step 4: Final take-home pay
    take_home = with_bonus - taxes
    print(f"Take-home pay: ${take_home:,.2f}")

    # You can also nest function calls
    print("\n--- Nested Function Calls ---")
    final_pay = calculate_base_salary(30, 40, 52) * 1.10  # Apply 10% increase
    net_pay = final_pay - calculate_taxes(final_pay, 18)
    print(f"Final net pay: ${net_pay:,.2f}")

    print("\n✓ Store returned values in variables for reuse")
    print("✓ Pass returned values to other functions")
    print("✓ Build complex logic from simple functions")


# ============================================================================
# 5. AVOIDING COMMON FUNCTION MISTAKES
# ============================================================================

def demonstrate_common_mistakes():
    """Demonstrate common mistakes and how to avoid them"""
    section_header("5. Avoiding Common Function Mistakes")

    print("--- MISTAKE 1: Printing Instead of Returning ---")
    
    # BAD: This function only prints
    def calculate_discount_bad(price, discount):
        result = price * (1 - discount / 100)
        print(f"Discounted price: ${result:.2f}")  # Only prints, doesn't return!

    # GOOD: This function returns the value
    def calculate_discount_good(price, discount):
        result = price * (1 - discount / 100)
        return result

    print("\nBAD approach (only prints, can't reuse):")
    calculate_discount_bad(100, 20)
    # Can't do anything with the result!

    print("\nGOOD approach (returns value, can reuse):")
    discount_price = calculate_discount_good(100, 20)
    final_with_tax = discount_price * 1.08
    print(f"After 20% discount and 8% tax: ${final_with_tax:.2f}")

    print("\n--- MISTAKE 2: Hardcoded Values ---")
    
    # BAD: Values are hardcoded
    def calculate_commission_bad(sales):
        return sales * 0.05  # 5% is hardcoded!

    # GOOD: Value is a parameter
    def calculate_commission_good(sales, commission_rate):
        return sales * commission_rate

    print("\nBAD: Hard to change hardcoded values")
    print(f"Commission on $1000 sales: ${calculate_commission_bad(1000):.2f}")

    print("\nGOOD: Flexible with parameters")
    print(f"Commission at 5%: ${calculate_commission_good(1000, 0.05):.2f}")
    print(f"Commission at 10%: ${calculate_commission_good(1000, 0.10):.2f}")

    print("\n--- MISTAKE 3: Missing Return Paths ---")
    
    # BAD: Not all paths return a value
    def validate_age_bad(age):
        if age >= 18:
            return "Adult"
        else:
            print("Not adult")  # Doesn't return!

    # GOOD: All paths return a value
    def validate_age_good(age):
        if age >= 18:
            return "Adult"
        else:
            return "Minor"

    print("\nBAD result:", validate_age_bad(15))  # Returns None
    print("GOOD result:", validate_age_good(15))  # Returns "Minor"

    print("\n--- MISTAKE 4: Forgetting to Store Results ---")
    
    def get_total_price(base_price, tax_rate):
        return base_price * (1 + tax_rate)

    print("\nWrong: Just calling without storing")
    get_total_price(100, 0.1)  # Result is lost

    print("\nCorrect: Store result in a variable")
    total = get_total_price(100, 0.1)
    print(f"Total price: ${total:.2f}")

    print("\n✓ Always return values instead of just printing")
    print("✓ Use parameters instead of hardcoding")
    print("✓ Ensure every path returns the expected type")
    print("✓ Store results to reuse them")


# ============================================================================
# 6. REAL-WORLD FUNCTION PATTERNS
# ============================================================================

def demonstrate_real_world_patterns():
    """Demonstrate common real-world function patterns"""
    section_header("6. Real-World Function Patterns")

    # Pattern 1: Validation and Return
    def validate_email(email):
        """Validate email format and return boolean"""
        return "@" in email and "." in email

    # Pattern 2: Calculate and Return
    def calculate_grade_points(percentage_score):
        """Convert percentage to grade point"""
        if percentage_score >= 90:
            return 4.0
        elif percentage_score >= 80:
            return 3.5
        elif percentage_score >= 70:
            return 3.0
        else:
            return 0.0

    # Pattern 3: Process and Return Summary
    def summarize_survey_responses(responses):
        """Process responses and return summary statistics"""
        if not responses:
            return {"count": 0, "average": 0}
        
        average = sum(responses) / len(responses)
        return {
            "count": len(responses),
            "average": round(average, 2),
            "highest": max(responses),
            "lowest": min(responses)
        }

    print("--- Pattern 1: Validation ---")
    email = "user@example.com"
    if validate_email(email):
        print(f"✓ Email '{email}' is valid")
    else:
        print(f"✗ Email '{email}' is invalid")

    print("\n--- Pattern 2: Lookup and Convert ---")
    scores = [95, 85, 72, 65]
    for score in scores:
        gpa = calculate_grade_points(score)
        print(f"Score {score}% → GPA {gpa}")

    print("\n--- Pattern 3: Process and Return Complex Results ---")
    survey_data = [4, 5, 3, 4, 5, 4, 3]
    summary = summarize_survey_responses(survey_data)
    print(f"Survey Summary:")
    print(f"  Responses: {summary['count']}")
    print(f"  Average: {summary['average']}")
    print(f"  Range: {summary['lowest']} - {summary['highest']}")

    print("\n✓ Real-world functions follow predictable patterns")
    print("✓ Functions solve specific problems and return results")
    print("✓ Results can be used in further processing")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all demonstrations"""
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*  LEARNING UNIT 4.19: PASSING DATA AND RETURNING RESULTS    *")
    print("*  Write Reusable, Flexible Functions with Data Flow          *")
    print("*" + " " * 68 + "*")
    print("*" * 70)

    demonstrate_parameters_and_arguments()
    demonstrate_passing_data()
    demonstrate_return_statement()
    demonstrate_using_returned_values()
    demonstrate_common_mistakes()
    demonstrate_real_world_patterns()

    section_header("Summary and Key Takeaways")
    print("""
    PARAMETERS & ARGUMENTS:
    ✓ Parameters are placeholders in function definition
    ✓ Arguments are actual values passed when calling functions
    ✓ Use positional arguments, keyword arguments, or both
    ✓ Default parameters provide flexibility

    RETURN STATEMENT:
    ✓ return sends value(s) OUT of the function
    ✓ Without return, function returns None
    ✓ Functions can return single or multiple values
    ✓ You can return any data type (numbers, strings, lists, dicts, etc.)

    USING RETURNED VALUES:
    ✓ Store returned values in variables for reuse
    ✓ Pass returned values to other functions
    ✓ Build powerful logic by composing simple functions
    ✓ This is the foundation of reusable, modular code

    BEST PRACTICES:
    ✓ Return values instead of only printing
    ✓ Use parameters instead of hardcoding values
    ✓ Ensure all execution paths return expected data
    ✓ Make functions do ONE thing well
    ✓ Write functions like machines: data in, results out

    Functions with clear input-output behavior are the foundation of
    scalable, testable, and maintainable Python programs.
    """)

    print("\n" + "=" * 70)
    print("  Demonstration Complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
