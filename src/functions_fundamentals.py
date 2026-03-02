"""
Functions Fundamentals - Learning Unit 4.18
Defining and Calling Python Functions

This module demonstrates:
1. Defining a Function
2. Calling a Function
3. Using Parameters and Arguments
4. Understanding Function Scope (Basics)
5. Practical Function Examples

Author: Trivin Insight Engine
Date: March 2, 2026
"""


def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


# ============================================================================
# 1. DEFINING A FUNCTION
# ============================================================================

def demonstrate_function_definition():
    """Demonstrate how to define simple functions with def"""
    section_header("1. Defining a Function")

    def welcome_message():
        """A simple function with no parameters"""
        print("Welcome to Python Functions Fundamentals!")
        print("Functions help us organize and reuse code.")

    print("Function defined: welcome_message()")
    print("Calling function now:")
    welcome_message()

    print("\nFunction body runs only when the function is called.")


# ============================================================================
# 2. CALLING A FUNCTION
# ============================================================================

def demonstrate_function_calling():
    """Demonstrate function calling and execution flow"""
    section_header("2. Calling a Function")

    def print_divider():
        print("-" * 40)

    def announce_step(step_name):
        print(f"Starting step: {step_name}")

    print("Execution starts in demonstrate_function_calling()")
    print_divider()
    announce_step("Load Data")
    announce_step("Clean Data")
    announce_step("Generate Report")
    print_divider()
    print("Execution returns after each function call completes.")


# ============================================================================
# 3. USING PARAMETERS AND ARGUMENTS
# ============================================================================

def demonstrate_parameters_and_arguments():
    """Demonstrate parameters, arguments, and return values"""
    section_header("3. Using Parameters and Arguments")

    def calculate_average(score1, score2, score3):
        """Return average of three scores"""
        return (score1 + score2 + score3) / 3

    def format_employee_summary(name, department, rating):
        """Create a formatted employee summary string"""
        return f"Employee: {name} | Department: {department} | Rating: {rating:.1f}/5"

    avg_score = calculate_average(4.2, 3.8, 4.5)
    print(f"Average score from calculate_average(4.2, 3.8, 4.5): {avg_score:.2f}")

    summary = format_employee_summary("Aarav", "Engineering", 4.6)
    print(summary)

    print("\nOrder matters for positional arguments.")
    print("Meaningful parameter names improve readability.")


# ============================================================================
# 4. UNDERSTANDING FUNCTION SCOPE (BASICS)
# ============================================================================

def demonstrate_function_scope():
    """Demonstrate local and global variable behavior"""
    section_header("4. Understanding Function Scope (Basics)")

    global_message = "I am a global variable"

    def scope_example():
        local_message = "I am local to scope_example()"
        print(f"Inside function -> local_message: {local_message}")
        print(f"Inside function -> global_message: {global_message}")

    scope_example()

    print(f"Outside function -> global_message: {global_message}")
    print("Outside function -> local_message is not accessible (local scope)")

    counter = 0

    def increment(value):
        value += 1
        print(f"Inside function increment(): {value}")
        return value

    print(f"Before function call, counter = {counter}")
    counter = increment(counter)
    print(f"After function call, counter = {counter}")


# ============================================================================
# 5. PRACTICAL FUNCTION EXAMPLES
# ============================================================================

def demonstrate_practical_examples():
    """Practical examples showing reusable function logic"""
    section_header("5. Practical Function Examples")

    def is_valid_score(score):
        return 0 <= score <= 100

    def classify_score(score):
        if score >= 90:
            return "Excellent"
        if score >= 75:
            return "Good"
        if score >= 50:
            return "Average"
        return "Needs Improvement"

    def analyze_scores(scores):
        valid_scores = [score for score in scores if is_valid_score(score)]

        if len(valid_scores) == 0:
            print("No valid scores to analyze.")
            return

        average_score = sum(valid_scores) / len(valid_scores)
        print(f"Input scores: {scores}")
        print(f"Valid scores: {valid_scores}")
        print(f"Average score: {average_score:.2f}")
        print(f"Overall classification: {classify_score(average_score)}")

    sample_scores = [95, 82, 76, 120, 67, -5, 88]
    analyze_scores(sample_scores)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all demonstrations"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*  LEARNING UNIT 4.18: DEFINING AND CALLING FUNCTIONS   *")
    print("*  Clean, Reusable Python Code                           *")
    print("*" + " " * 58 + "*")
    print("*" * 60)

    demonstrate_function_definition()
    demonstrate_function_calling()
    demonstrate_parameters_and_arguments()
    demonstrate_function_scope()
    demonstrate_practical_examples()

    section_header("Summary and Key Takeaways")
    print("""
    ✓ Functions are defined with the def keyword
    ✓ Functions run only when called
    ✓ Parameters accept input; arguments pass values
    ✓ Local variables exist only inside functions
    ✓ Functions reduce repetition and improve readability
    ✓ Small, focused functions are easier to test and maintain

    Functions are core building blocks for modular Python programs.
    """)

    print("\n" + "=" * 60)
    print("  Demonstration Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
