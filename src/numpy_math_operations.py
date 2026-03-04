"""
NumPy Mathematical Operations - Learning Unit 4.21
Performing Basic Mathematical Operations on NumPy Arrays

This module demonstrates:
1. Element-wise array operations (add, subtract, multiply, divide)
2. Scalar operations on arrays
3. Comparing NumPy arrays and Python lists for math
4. Avoiding common mistakes with array math

Understanding array-based math is essential before moving on to real data 
analysis and scientific computing.

Author: Trivin Insight Engine
Date: March 4, 2026
"""

import numpy as np


def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# ============================================================================
# 1. ELEMENT-WISE ARRAY OPERATIONS
# ============================================================================

def demonstrate_element_wise_operations():
    """
    Learn how NumPy applies operations element-wise.
    
    Operations are applied to corresponding elements in arrays.
    Arrays must have the same shape for element-wise operations.
    """
    section_header("1. Element-Wise Array Operations")
    
    print("\n--- CREATING TWO ARRAYS OF THE SAME SHAPE ---")
    array_a = np.array([10, 20, 30, 40, 50])
    array_b = np.array([1, 2, 3, 4, 5])
    
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"Shape of A: {array_a.shape}")
    print(f"Shape of B: {array_b.shape}")
    print("✓ Both arrays have the same shape (5,)")
    
    # Addition
    print("\n--- ELEMENT-WISE ADDITION ---")
    result_add = array_a + array_b
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"A + B:   {result_add}")
    print("\nHow it works:")
    print("Position 0: 10 + 1 = 11")
    print("Position 1: 20 + 2 = 22")
    print("Position 2: 30 + 3 = 33")
    print("Position 3: 40 + 4 = 44")
    print("Position 4: 50 + 5 = 55")
    
    # Subtraction
    print("\n--- ELEMENT-WISE SUBTRACTION ---")
    result_sub = array_a - array_b
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"A - B:   {result_sub}")
    print("\nHow it works:")
    print("Position 0: 10 - 1 = 9")
    print("Position 1: 20 - 2 = 18")
    print("Position 2: 30 - 3 = 27")
    print("Position 3: 40 - 4 = 36")
    print("Position 4: 50 - 5 = 45")
    
    # Multiplication
    print("\n--- ELEMENT-WISE MULTIPLICATION ---")
    result_mul = array_a * array_b
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"A * B:   {result_mul}")
    print("\nHow it works:")
    print("Position 0: 10 * 1 = 10")
    print("Position 1: 20 * 2 = 40")
    print("Position 2: 30 * 3 = 90")
    print("Position 3: 40 * 4 = 160")
    print("Position 4: 50 * 5 = 250")
    
    # Division
    print("\n--- ELEMENT-WISE DIVISION ---")
    result_div = array_a / array_b
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"A / B:   {result_div}")
    print("\nHow it works:")
    print("Position 0: 10 / 1 = 10.0")
    print("Position 1: 20 / 2 = 10.0")
    print("Position 2: 30 / 3 = 10.0")
    print("Position 3: 40 / 4 = 10.0")
    print("Position 4: 50 / 5 = 10.0")
    
    # 2D array operations
    print("\n--- ELEMENT-WISE OPERATIONS ON 2D ARRAYS ---")
    matrix_a = np.array([[1, 2, 3],
                         [4, 5, 6]])
    matrix_b = np.array([[10, 20, 30],
                         [40, 50, 60]])
    
    print(f"Matrix A:\n{matrix_a}")
    print(f"\nMatrix B:\n{matrix_b}")
    print(f"\nShape of A: {matrix_a.shape}")
    print(f"Shape of B: {matrix_b.shape}")
    
    print(f"\nA + B:\n{matrix_a + matrix_b}")
    print(f"\nA * B:\n{matrix_a * matrix_b}")
    print(f"\nB / A:\n{matrix_b / matrix_a}")
    
    print("\n✓ Element-wise operations apply to corresponding positions")
    print("✓ This works for arrays of any shape (as long as they match)")


# ============================================================================
# 2. SCALAR OPERATIONS ON ARRAYS
# ============================================================================

def demonstrate_scalar_operations():
    """
    Apply single values (scalars) to entire arrays.
    
    Scalar operations are "broadcast" across all elements.
    This is one of NumPy's most powerful features.
    """
    section_header("2. Scalar Operations on Arrays")
    
    print("\n--- WHAT IS A SCALAR? ---")
    print("A scalar is a single numerical value (not an array)")
    print("Examples: 5, 10, 2.5, 100")
    
    # Create an array
    print("\n--- CREATING A SAMPLE ARRAY ---")
    array = np.array([10, 20, 30, 40, 50])
    print(f"Original array: {array}")
    print(f"Shape: {array.shape}")
    
    # Addition with scalar
    print("\n--- ADDING A SCALAR TO AN ARRAY ---")
    scalar_value = 5
    result = array + scalar_value
    print(f"Original array: {array}")
    print(f"Scalar value:   {scalar_value}")
    print(f"array + 5:      {result}")
    print("\nHow it works:")
    print("5 is added to EVERY element in the array:")
    print("10+5=15, 20+5=25, 30+5=35, 40+5=45, 50+5=55")
    
    # Subtraction with scalar
    print("\n--- SUBTRACTING A SCALAR FROM AN ARRAY ---")
    result = array - 10
    print(f"Original array: {array}")
    print(f"array - 10:     {result}")
    
    # Multiplication with scalar
    print("\n--- MULTIPLYING AN ARRAY BY A SCALAR ---")
    result = array * 2
    print(f"Original array: {array}")
    print(f"array * 2:      {result}")
    print("\nEvery element is multiplied by 2")
    
    # Division with scalar
    print("\n--- DIVIDING AN ARRAY BY A SCALAR ---")
    result = array / 10
    print(f"Original array: {array}")
    print(f"array / 10:     {result}")
    print("\nEvery element is divided by 10")
    
    # Power operation
    print("\n--- RAISING ARRAY TO A POWER ---")
    small_array = np.array([1, 2, 3, 4, 5])
    result = small_array ** 2
    print(f"Original array: {small_array}")
    print(f"array ** 2:     {result}")
    print("\nEach element is squared: 1²=1, 2²=4, 3²=9, 4²=16, 5²=25")
    
    # Scalar operations on 2D arrays
    print("\n--- SCALAR OPERATIONS ON 2D ARRAYS ---")
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    print(f"Original matrix:\n{matrix}")
    print(f"\nMatrix + 10:\n{matrix + 10}")
    print(f"\nMatrix * 3:\n{matrix * 3}")
    
    print("\n✓ Scalar operations apply to ALL elements")
    print("✓ This is called 'broadcasting'")
    print("✓ Much cleaner than using loops!")


# ============================================================================
# 3. COMPARING NUMPY ARRAYS AND PYTHON LISTS
# ============================================================================

def compare_arrays_and_lists():
    """
    Understand key differences between list and array math.
    
    This clarifies why NumPy is preferred for mathematical operations.
    Python lists and NumPy arrays behave very differently!
    """
    section_header("3. Comparing NumPy Arrays and Python Lists")
    
    print("\n--- CREATING LISTS AND ARRAYS ---")
    python_list = [1, 2, 3, 4, 5]
    numpy_array = np.array([1, 2, 3, 4, 5])
    
    print(f"Python list: {python_list}")
    print(f"NumPy array: {numpy_array}")
    print(f"\nList type: {type(python_list)}")
    print(f"Array type: {type(numpy_array)}")
    
    # Addition behavior
    print("\n--- DIFFERENCE 1: ADDITION BEHAVIOR ---")
    print("\nPython Lists:")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"list1: {list1}")
    print(f"list2: {list2}")
    print(f"list1 + list2 = {list1 + list2}")
    print("→ Lists CONCATENATE (join together)")
    
    print("\nNumPy Arrays:")
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    print(f"array1: {array1}")
    print(f"array2: {array2}")
    print(f"array1 + array2 = {array1 + array2}")
    print("→ Arrays ADD ELEMENT-WISE (1+4, 2+5, 3+6)")
    
    # Multiplication behavior
    print("\n--- DIFFERENCE 2: MULTIPLICATION BEHAVIOR ---")
    print("\nPython Lists:")
    list1 = [1, 2, 3]
    print(f"list1: {list1}")
    print(f"list1 * 3 = {list1 * 3}")
    print("→ Lists REPEAT (duplicate the list)")
    
    print("\nNumPy Arrays:")
    array1 = np.array([1, 2, 3])
    print(f"array1: {array1}")
    print(f"array1 * 3 = {array1 * 3}")
    print("→ Arrays MULTIPLY EACH ELEMENT by 3")
    
    # What lists can't do
    print("\n--- WHAT PYTHON LISTS CAN'T DO ---")
    print("\nTrying to subtract lists:")
    print("list1 = [5, 10, 15]")
    print("list2 = [1, 2, 3]")
    print("list1 - list2  → This will cause an ERROR!")
    print("Python lists don't support subtraction")
    
    print("\nWith NumPy arrays:")
    array1 = np.array([5, 10, 15])
    array2 = np.array([1, 2, 3])
    print(f"array1: {array1}")
    print(f"array2: {array2}")
    print(f"array1 - array2 = {array1 - array2}")
    print("→ Arrays support all mathematical operations!")
    
    # Performance comparison (conceptual)
    print("\n--- PERFORMANCE COMPARISON ---")
    print("\nFor mathematical operations on 1 million numbers:")
    print("┌─────────────────┬──────────────────────┐")
    print("│ Method          │ Typical Speed        │")
    print("├─────────────────┼──────────────────────┤")
    print("│ Python Lists    │ ~100ms (slower)      │")
    print("│ NumPy Arrays    │ ~5ms (much faster)   │")
    print("└─────────────────┴──────────────────────┘")
    print("\n✓ NumPy is 10-100x faster for numerical operations")
    
    # When to use each
    print("\n--- WHEN TO USE EACH ---")
    print("\nUse Python Lists when:")
    print("  • You need mixed data types (numbers, strings, etc.)")
    print("  • You need to append/remove items frequently")
    print("  • You're not doing mathematical operations")
    
    print("\nUse NumPy Arrays when:")
    print("  • You're doing mathematical operations")
    print("  • You need high performance")
    print("  • You're working with numerical data")
    print("  • You're doing data analysis or scientific computing")
    
    print("\n✓ For math operations, ALWAYS prefer NumPy arrays")


# ============================================================================
# 4. AVOIDING COMMON MISTAKES
# ============================================================================

def demonstrate_common_mistakes():
    """
    Recognize common pitfalls with array math.
    
    Understanding what can go wrong helps you write better code.
    """
    section_header("4. Avoiding Common Mistakes")
    
    # Mistake 1: Shape mismatch
    print("\n--- MISTAKE 1: INCOMPATIBLE SHAPES ---")
    array1 = np.array([1, 2, 3])
    array2 = np.array([1, 2, 3, 4, 5])
    
    print(f"Array 1: {array1} (shape: {array1.shape})")
    print(f"Array 2: {array2} (shape: {array2.shape})")
    print("\nTrying to add these arrays:")
    
    try:
        result = array1 + array2
        print(f"Result: {result}")
    except ValueError as e:
        print(f"❌ ERROR: {e}")
        print("\n✓ Solution: Ensure arrays have compatible shapes!")
    
    print("\nCorrect approach:")
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([10, 20, 30, 40, 50])
    print(f"Array 1: {array1} (shape: {array1.shape})")
    print(f"Array 2: {array2} (shape: {array2.shape})")
    result = array1 + array2
    print(f"Result: {result}")
    print("✓ Both arrays have shape (5,) - operation succeeds!")
    
    # Mistake 2: Mixing data types incorrectly
    print("\n--- MISTAKE 2: MIXING DATA TYPES ---")
    int_array = np.array([1, 2, 3, 4, 5])
    float_array = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    
    print(f"Integer array: {int_array} (dtype: {int_array.dtype})")
    print(f"Float array: {float_array} (dtype: {float_array.dtype})")
    
    result = int_array + float_array
    print(f"\nResult: {result}")
    print(f"Result dtype: {result.dtype}")
    print("✓ NumPy automatically converts to float (no data loss)")
    
    # Mistake 3: Modifying arrays in-place unexpectedly
    print("\n--- MISTAKE 3: UNEXPECTED IN-PLACE MODIFICATION ---")
    original = np.array([1, 2, 3, 4, 5])
    reference = original  # This doesn't create a copy!
    
    print(f"Original array: {original}")
    print(f"Reference: {reference}")
    
    reference[0] = 999
    print(f"\nAfter modifying reference[0] = 999:")
    print(f"Reference: {reference}")
    print(f"Original: {original}")
    print("❌ Original was also modified!")
    
    print("\n✓ Solution: Use .copy() to create independent arrays:")
    original = np.array([1, 2, 3, 4, 5])
    independent_copy = original.copy()
    
    print(f"Original: {original}")
    print(f"Copy: {independent_copy}")
    
    independent_copy[0] = 999
    print(f"\nAfter modifying copy[0] = 999:")
    print(f"Copy: {independent_copy}")
    print(f"Original: {original}")
    print("✓ Original is unchanged!")
    
    # Mistake 4: Division by zero
    print("\n--- MISTAKE 4: DIVISION BY ZERO ---")
    numerator = np.array([10, 20, 30])
    denominator = np.array([2, 0, 5])
    
    print(f"Numerator: {numerator}")
    print(f"Denominator: {denominator}")
    
    print("\nDivision (with zero in denominator):")
    with np.errstate(divide='warn'):
        result = numerator / denominator
        print(f"Result: {result}")
    
    print("\n⚠️ Division by zero produces 'inf' (infinity)")
    print("✓ Always validate your data before division!")
    
    # Mistake 5: Assuming list operations work on arrays
    print("\n--- MISTAKE 5: ASSUMING LIST METHODS WORK ---")
    python_list = [1, 2, 3]
    numpy_array = np.array([1, 2, 3])
    
    print(f"Python list: {python_list}")
    print(f"NumPy array: {numpy_array}")
    
    print("\nAppending to a list:")
    python_list.append(4)
    print(f"list.append(4) → {python_list}")
    
    print("\nTrying to append to an array:")
    print("array.append(4) → This will cause an ERROR!")
    print("Arrays don't have an append() method")
    
    print("\n✓ Use np.append() instead:")
    numpy_array = np.append(numpy_array, 4)
    print(f"np.append(array, 4) → {numpy_array}")
    
    print("\n✓ Or better yet, use lists during construction,")
    print("  then convert to array when ready for computation")
    
    # Best practices summary
    print("\n--- BEST PRACTICES SUMMARY ---")
    print("✓ Check array shapes before operations")
    print("✓ Use .copy() when you need independent arrays")
    print("✓ Validate data before division")
    print("✓ Remember: arrays are not lists!")
    print("✓ Keep arrays homogeneous (same data type)")


# ============================================================================
# 5. PRACTICAL EXAMPLES
# ============================================================================

def demonstrate_practical_examples():
    """
    Real-world scenarios using array math operations.
    
    These examples show how array operations simplify common tasks.
    """
    section_header("5. Practical Examples")
    
    # Example 1: Converting temperatures
    print("\n--- EXAMPLE 1: TEMPERATURE CONVERSION ---")
    print("Converting Celsius to Fahrenheit: F = (C × 9/5) + 32")
    
    celsius_temps = np.array([0, 10, 20, 30, 40, 100])
    print(f"\nTemperatures in Celsius: {celsius_temps}")
    
    fahrenheit_temps = (celsius_temps * 9/5) + 32
    print(f"Temperatures in Fahrenheit: {fahrenheit_temps}")
    
    print("\nWithout NumPy, you'd need a loop:")
    print("fahrenheit = []")
    print("for c in celsius:")
    print("    f = (c * 9/5) + 32")
    print("    fahrenheit.append(f)")
    print("\n✓ NumPy makes this a one-liner!")
    
    # Example 2: Calculating total costs
    print("\n--- EXAMPLE 2: CALCULATING TOTAL COSTS ---")
    print("Items purchased with quantities and prices")
    
    quantities = np.array([3, 5, 2, 4])
    prices = np.array([10.99, 5.49, 25.00, 8.75])
    
    print(f"\nQuantities: {quantities}")
    print(f"Prices:     {prices}")
    
    total_per_item = quantities * prices
    print(f"Total/item: {total_per_item}")
    
    grand_total = np.sum(total_per_item)
    print(f"\nGrand total: ${grand_total:.2f}")
    
    # Example 3: Normalizing data
    print("\n--- EXAMPLE 3: NORMALIZING DATA (SCALING TO 0-1) ---")
    print("Common step in data preprocessing")
    
    raw_scores = np.array([45, 67, 89, 23, 91, 56, 78])
    print(f"\nRaw scores: {raw_scores}")
    
    min_score = np.min(raw_scores)
    max_score = np.max(raw_scores)
    
    normalized = (raw_scores - min_score) / (max_score - min_score)
    print(f"Normalized: {normalized}")
    print(f"\nAll values are now between 0 and 1")
    print(f"Minimum: {np.min(normalized):.2f}")
    print(f"Maximum: {np.max(normalized):.2f}")
    
    # Example 4: Calculating percentage change
    print("\n--- EXAMPLE 4: PERCENTAGE CHANGE ---")
    print("Comparing values across time periods")
    
    week1_sales = np.array([100, 150, 120, 180, 95])
    week2_sales = np.array([110, 145, 135, 190, 100])
    
    print(f"\nWeek 1 sales: {week1_sales}")
    print(f"Week 2 sales: {week2_sales}")
    
    change = week2_sales - week1_sales
    percent_change = (change / week1_sales) * 100
    
    print(f"\nAbsolute change: {change}")
    print(f"Percent change:  {percent_change}")
    
    print("\n✓ Positive values = increase")
    print("✓ Negative values = decrease")
    
    # Example 5: Statistical calculations
    print("\n--- EXAMPLE 5: STANDARDIZING DATA (Z-SCORES) ---")
    print("Converting to standard deviations from mean")
    
    data = np.array([85, 90, 78, 92, 88, 76, 95, 89, 91, 87])
    print(f"\nData: {data}")
    
    mean = np.mean(data)
    std = np.std(data)
    
    print(f"Mean: {mean:.2f}")
    print(f"Standard deviation: {std:.2f}")
    
    z_scores = (data - mean) / std
    print(f"\nZ-scores: {z_scores}")
    print("\n✓ Z-score tells you how many standard deviations")
    print("  a value is from the mean")
    print(f"✓ Values close to 0 are near average")
    print(f"✓ Values above 2 or below -2 are outliers")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def run_all_demonstrations():
    """Run all demonstrations for NumPy mathematical operations"""
    print("\n" + "=" * 70)
    print("  NumPy Mathematical Operations - Complete Learning Guide")
    print("  Performing Basic Mathematical Operations on NumPy Arrays")
    print("=" * 70)
    
    demonstrate_element_wise_operations()
    demonstrate_scalar_operations()
    compare_arrays_and_lists()
    demonstrate_common_mistakes()
    demonstrate_practical_examples()
    
    print("\n" + "=" * 70)
    print("  ✓ All Demonstrations Complete!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("─" * 70)
    print("1. Element-wise operations apply to corresponding array positions")
    print("2. Scalar operations broadcast across all elements")
    print("3. NumPy arrays behave differently than Python lists for math")
    print("4. Always check array shapes before operations")
    print("5. NumPy makes numerical computation concise and efficient")
    print("─" * 70)
    print("\nWhat You've Learned:")
    print("✓ Add, subtract, multiply, and divide NumPy arrays")
    print("✓ Apply scalar operations across arrays")
    print("✓ Understand element-wise behavior clearly")
    print("✓ Avoid common mistakes with array math")
    print("✓ Use NumPy for efficient numerical computation")
    print("─" * 70)
    print("\nNext Steps:")
    print("• Practice with your own numerical data")
    print("• Explore more NumPy functions (sqrt, power, exp, log)")
    print("• Learn about broadcasting with different shaped arrays")
    print("• Apply these concepts to real datasets")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_all_demonstrations()
