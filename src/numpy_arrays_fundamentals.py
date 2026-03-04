"""
NumPy Arrays Fundamentals - Learning Unit 4.20
Creating NumPy Arrays from Python Lists

This module demonstrates:
1. Understanding NumPy Arrays vs Python Lists
2. Creating NumPy Arrays from Lists
3. Inspecting Array Properties
4. Basic Operations on Arrays
5. Recognizing Key Differences Between Lists and Arrays

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
# 1. UNDERSTANDING NUMPY ARRAYS VS PYTHON LISTS
# ============================================================================

def demonstrate_arrays_vs_lists():
    """Understand the differences between NumPy arrays and Python lists"""
    section_header("1. Understanding NumPy Arrays vs Python Lists")

    print("\n--- WHAT ARE PYTHON LISTS? ---")
    python_list = [1, 2, 3, 4, 5]
    print(f"Python list: {python_list}")
    print(f"Type: {type(python_list)}")
    print(f"Python lists are flexible - they can hold mixed types:")
    mixed_list = [1, "two", 3.0, True]
    print(f"Mixed list: {mixed_list}")

    print("\n--- WHAT ARE NUMPY ARRAYS? ---")
    numpy_array = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {numpy_array}")
    print(f"Type: {type(numpy_array)}")
    print(f"NumPy arrays are homogeneous - all elements must be the same type:")
    
    # NumPy automatically converts to consistent type
    array_from_mixed = np.array([1, 2, 3, 4])
    print(f"Array: {array_from_mixed}")
    print(f"Data type: {array_from_mixed.dtype}")

    print("\n--- WHY USE NUMPY ARRAYS? ---")
    print("1. SPEED: NumPy operations are 10-100x faster than Python lists")
    print("2. MEMORY: NumPy arrays use less memory than Python lists")
    print("3. CONVENIENCE: Easier syntax for mathematical operations")
    print("4. CONSISTENCY: All elements are the same type (predictable behavior)")
    print("5. INTEGRATION: Essential for Pandas, Scikit-learn, and other libraries")

    print("\n--- PERFORMANCE COMPARISON (Conceptual) ---")
    print("Python list: Stores references to individual objects in memory")
    print("NumPy array: Stores efficient numeric values in contiguous memory")
    print("Result: NumPy is significantly faster for numerical computations")


# ============================================================================
# 2. CREATING NUMPY ARRAYS FROM PYTHON LISTS
# ============================================================================

def demonstrate_creating_arrays():
    """Learn how to create NumPy arrays from Python lists"""
    section_header("2. Creating NumPy Arrays from Python Lists")

    # Creating a one-dimensional array
    print("\n--- CREATING ONE-DIMENSIONAL ARRAYS ---")
    
    python_list_1d = [10, 20, 30, 40, 50]
    array_1d = np.array(python_list_1d)
    print(f"Python list: {python_list_1d}")
    print(f"NumPy array: {array_1d}")
    print(f"Array contents: \n{array_1d}")

    # Creating a 2D array (matrix) from nested lists
    print("\n--- CREATING TWO-DIMENSIONAL ARRAYS (MATRICES) ---")
    
    python_list_2d = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    array_2d = np.array(python_list_2d)
    print(f"Python nested list:\n{python_list_2d}")
    print(f"NumPy 2D array:\n{array_2d}")

    # Creating arrays with different data types
    print("\n--- ARRAYS WITH DIFFERENT DATA TYPES ---")
    
    # Integer array
    int_array = np.array([1, 2, 3, 4, 5])
    print(f"Integer array: {int_array}")
    print(f"Data type: {int_array.dtype}")

    # Float array
    float_array = np.array([1.5, 2.5, 3.5, 4.5])
    print(f"\nFloat array: {float_array}")
    print(f"Data type: {float_array.dtype}")

    # Explicitly specify data type
    print("\n--- SPECIFYING DATA TYPE EXPLICITLY ---")
    
    explicit_int = np.array([1, 2, 3], dtype=int)
    print(f"Explicit int array: {explicit_int}")
    print(f"Data type: {explicit_int.dtype}")

    explicit_float = np.array([1, 2, 3], dtype=float)
    print(f"\nExplicit float array: {explicit_float}")
    print(f"Data type: {explicit_float.dtype}")

    # Creating arrays with convenience functions
    print("\n--- CREATING ARRAYS WITH CONVENIENCE FUNCTIONS ---")
    
    zeros = np.zeros(5)
    print(f"Array of zeros (length 5): {zeros}")

    ones = np.ones(5)
    print(f"Array of ones (length 5): {ones}")

    range_array = np.arange(0, 10, 2)
    print(f"Array with arange(0, 10, 2): {range_array}")

    linspace_array = np.linspace(0, 10, 5)
    print(f"Array with linspace(0, 10, 5): {linspace_array}")


# ============================================================================
# 3. INSPECTING ARRAY PROPERTIES
# ============================================================================

def demonstrate_array_properties():
    """Understand array structure and properties"""
    section_header("3. Inspecting Array Properties")

    # One-dimensional array
    print("\n--- ONE-DIMENSIONAL ARRAY PROPERTIES ---")
    
    array_1d = np.array([10, 20, 30, 40, 50])
    print(f"Array: {array_1d}")
    print(f"Shape: {array_1d.shape}")  # Number of elements in each dimension
    print(f"Data type: {array_1d.dtype}")  # Type of elements
    print(f"Size: {array_1d.size}")  # Total number of elements
    print(f"Ndim (Number of dimensions): {array_1d.ndim}")  # Number of axes
    print(f"Itemsize (Size per element in bytes): {array_1d.itemsize}")

    # Two-dimensional array (matrix)
    print("\n--- TWO-DIMENSIONAL ARRAY PROPERTIES ---")
    
    array_2d = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print(f"Array:\n{array_2d}")
    print(f"Shape: {array_2d.shape}")  # (rows, columns)
    print(f"Data type: {array_2d.dtype}")
    print(f"Size: {array_2d.size}")  # Total elements (2 * 3 = 6)
    print(f"Ndim: {array_2d.ndim}")  # 2 dimensions

    # Three-dimensional array
    print("\n--- THREE-DIMENSIONAL ARRAY ---")
    
    array_3d = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ])
    print(f"Array:\n{array_3d}")
    print(f"Shape: {array_3d.shape}")  # (2, 2, 2)
    print(f"Ndim: {array_3d.ndim}")  # 3 dimensions

    # Understanding shape
    print("\n--- UNDERSTANDING SHAPE ---")
    print("Shape tells us the size of each dimension:")
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(f"Array shape: {array.shape}")
    print(f"This means: 3 rows, 4 columns")
    print(f"Total elements: 3 × 4 = {array.size}")


# ============================================================================
# 4. BASIC OPERATIONS ON ARRAYS
# ============================================================================

def demonstrate_array_operations():
    """Learn basic operations on NumPy arrays"""
    section_header("4. Basic Operations on Arrays")

    # Arithmetic operations
    print("\n--- ARITHMETIC OPERATIONS ---")
    
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([10, 20, 30, 40, 50])
    
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    
    print(f"\nAddition: {array1 + array2}")
    print(f"Subtraction: {array2 - array1}")
    print(f"Multiplication: {array1 * array2}")
    print(f"Division: {array2 / array1}")

    # Element-wise operations
    print("\n--- ELEMENT-WISE OPERATIONS (KEY DIFFERENCE FROM LISTS) ---")
    
    print("\nWith Python lists:")
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"[1, 2, 3] + [1, 2, 3] = {list1 + list2}")
    print("Lists concatenate, not add element-wise!")
    
    print("\nWith NumPy arrays:")
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([1, 2, 3])
    print(f"array([1, 2, 3]) + array([1, 2, 3]) = {arr1 + arr2}")
    print("Arrays add element-wise!")

    # Scalar operations
    print("\n--- SCALAR OPERATIONS ---")
    
    array = np.array([1, 2, 3, 4, 5])
    print(f"Original array: {array}")
    print(f"Add 10: {array + 10}")
    print(f"Multiply by 2: {array * 2}")
    print(f"Square each element: {array ** 2}")
    print(f"Square root of each: {np.sqrt(array)}")

    # Useful aggregate functions
    print("\n--- AGGREGATE FUNCTIONS ---")
    
    array = np.array([10, 20, 30, 40, 50])
    print(f"Array: {array}")
    print(f"Sum: {np.sum(array)}")
    print(f"Mean: {np.mean(array)}")
    print(f"Minimum: {np.min(array)}")
    print(f"Maximum: {np.max(array)}")
    print(f"Standard deviation: {np.std(array)}")

    # 2D array operations
    print("\n--- OPERATIONS ON 2D ARRAYS ---")
    
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(f"Matrix:\n{matrix}")
    print(f"\nAdd 100: \n{matrix + 100}")
    print(f"\nMultiply by 2: \n{matrix * 2}")
    print(f"\nSum of all elements: {np.sum(matrix)}")
    print(f"Sum of each row: {np.sum(matrix, axis=1)}")
    print(f"Sum of each column: {np.sum(matrix, axis=0)}")


# ============================================================================
# 5. RECOGNIZING KEY DIFFERENCES BETWEEN LISTS AND ARRAYS
# ============================================================================

def demonstrate_list_vs_array_differences():
    """Highlight important differences between lists and arrays"""
    section_header("5. Key Differences Between Lists and Arrays")

    print("\n--- 1. MATHEMATICAL OPERATIONS ---")
    print("Lists:")
    py_list = [1, 2, 3]
    print(f"  Original: {py_list}")
    print(f"  [1,2,3] * 2 = {py_list * 2}  (concatenation)")
    
    print("\nArrays:")
    np_array = np.array([1, 2, 3])
    print(f"  Original: {np_array}")
    print(f"  array * 2 = {np_array * 2}  (element-wise multiplication)")

    print("\n--- 2. HOMOGENEOUS vs HETEROGENEOUS ---")
    print("Lists (heterogeneous):")
    mixed_list = [1, "text", 3.14, True]
    print(f"  {mixed_list} - can hold different types")
    
    print("\nArrays (homogeneous):")
    mixed_attempt = np.array([1, "text", 3.14, True])
    print(f"  {mixed_attempt}")
    print(f"  Data type: {mixed_attempt.dtype}")
    print("  NumPy converted everything to strings!")

    print("\n--- 3. MEMORY EFFICIENCY ---")
    py_list = [1, 2, 3, 4, 5]
    np_array = np.array([1, 2, 3, 4, 5])
    print(f"Python list stores object references")
    print(f"NumPy array stores data in contiguous memory")
    print(f"Result: Arrays are much more memory-efficient for numbers")

    print("\n--- 4. PERFORMANCE ---")
    print("For 1 million element operations:")
    print("  Python lists: Much slower (loops through each element)")
    print("  NumPy arrays: Much faster (optimized C code under the hood)")

    print("\n--- 5. BROADCASTING (Array Advantage) ---")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    single_value = 10
    print(f"Matrix + single value:")
    print(f"{matrix} + {single_value}")
    print(f"Result:\n{matrix + single_value}")
    print("NumPy automatically broadcasts the scalar to match the shape!")


# ============================================================================
# 6. REAL-WORLD EXAMPLE: SURVEY DATA
# ============================================================================

def demonstrate_survey_data_example():
    """Practical example using survey data"""
    section_header("6. Real-World Example: Employee Survey Data")

    print("\n--- SURVEY SCORES AS LISTS vs ARRAYS ---")
    
    # Simulate satisfaction scores from 5 employees on a scale of 1-10
    satisfaction_list = [7, 8, 6, 9, 8]
    satisfaction_array = np.array([7, 8, 6, 9, 8])
    
    print(f"Satisfaction scores (list): {satisfaction_list}")
    print(f"Satisfaction scores (array): {satisfaction_array}")

    print("\n--- COMPUTING STATISTICS WITH ARRAYS ---")
    print(f"Average satisfaction: {np.mean(satisfaction_array):.2f}")
    print(f"Median satisfaction: {np.median(satisfaction_array):.2f}")
    print(f"Highest score: {np.max(satisfaction_array)}")
    print(f"Lowest score: {np.min(satisfaction_array)}")

    print("\n--- SCALING SCORES WITH ARRAYS ---")
    print("If we want to scale scores from 0-10 to 0-100:")
    scaled_scores = satisfaction_array * 10
    print(f"Original scores: {satisfaction_array}")
    print(f"Scaled scores: {scaled_scores}")

    print("\n--- MULTI-DEPARTMENT SURVEY ---")
    print("3 departments, 4 employees each, satisfaction scores:")
    survey_data = np.array([
        [7, 8, 6, 9],      # Department A
        [8, 7, 8, 7],      # Department B
        [6, 9, 8, 8]       # Department C
    ])
    print(f"Survey data:\n{survey_data}")
    print(f"\nShape: {survey_data.shape} (3 departments, 4 employees)")
    print(f"Average satisfaction by department: {np.mean(survey_data, axis=1)}")
    print(f"Average satisfaction overall: {np.mean(survey_data):.2f}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def run_all_demonstrations():
    """Run all demonstrations"""
    demonstrate_arrays_vs_lists()
    demonstrate_creating_arrays()
    demonstrate_array_properties()
    demonstrate_array_operations()
    demonstrate_list_vs_array_differences()
    demonstrate_survey_data_example()
    
    print("\n" + "=" * 70)
    print("  ✓ NumPy Arrays Fundamentals - All Demonstrations Complete")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. NumPy arrays are faster and more memory-efficient than lists")
    print("2. Create arrays from lists using np.array()")
    print("3. Use shape and dtype to understand array structure")
    print("4. NumPy operations are element-wise (unlike list concatenation)")
    print("5. Arrays are essential for numerical computing in Python")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_all_demonstrations()
