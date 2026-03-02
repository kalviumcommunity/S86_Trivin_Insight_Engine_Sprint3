"""
Loops Fundamentals - Python Iteration for Data Processing
==========================================================

This module demonstrates the fundamentals of iteration using for and while loops.
Loops are essential for repeating operations efficiently in data processing.

Learning Objectives:
- Write for loops to process sequences and collections
- Write while loops for condition-based repetition
- Control loops using break and continue
- Recognize and fix infinite loop scenarios
- Use loops confidently in data workflows
"""


# =========================================
# 1. USING FOR LOOPS FOR ITERATION
# =========================================

def demonstrate_for_loops():
    """
    Demonstrates various for loop patterns for iteration.
    For loops are ideal when you know the sequence you're iterating over.
    """
    print("=" * 60)
    print("1. FOR LOOPS - ITERATING OVER SEQUENCES")
    print("=" * 60)
    
    # Example 1.1: Iterate over a range of numbers
    print("\n1.1 Iterating over a range:")
    print("Processing data points 0 to 4...")
    for i in range(5):
        print(f"  Data point {i}: Value = {i * 10}")
    
    # Example 1.2: Iterate over a list
    print("\n1.2 Iterating over a list:")
    departments = ["Engineering", "Sales", "Marketing", "HR", "Finance"]
    print(f"Departments in company: {len(departments)}")
    for dept in departments:
        print(f"  - {dept}")
    
    # Example 1.3: Iterate with index using enumerate
    print("\n1.3 Iterating with index and value:")
    scores = [85, 92, 78, 95, 88]
    for index, score in enumerate(scores, start=1):
        print(f"  Employee {index}: Score = {score}")
    
    # Example 1.4: Iterate over a dictionary
    print("\n1.4 Iterating over a dictionary:")
    employee_attendance = {
        "Alice": 22,
        "Bob": 20,
        "Charlie": 21,
        "Diana": 23
    }
    for name, days in employee_attendance.items():
        print(f"  {name}: {days} days present")
    
    # Example 1.5: Real-world data processing scenario
    print("\n1.5 Data processing example - filtering data:")
    survey_responses = [3, 5, 2, 4, 5, 1, 4, 5, 3, 4]
    high_ratings = []
    
    for rating in survey_responses:
        if rating >= 4:
            high_ratings.append(rating)
    
    print(f"  Total responses: {len(survey_responses)}")
    print(f"  High ratings (≥4): {len(high_ratings)}")
    print(f"  Percentage satisfied: {(len(high_ratings) / len(survey_responses)) * 100:.1f}%")


# =========================================
# 2. USING WHILE LOOPS FOR CONDITION-BASED REPETITION
# =========================================

def demonstrate_while_loops():
    """
    Demonstrates while loops for condition-based repetition.
    While loops are useful when repetition depends on conditions.
    """
    print("\n" + "=" * 60)
    print("2. WHILE LOOPS - CONDITION-BASED REPETITION")
    print("=" * 60)
    
    # Example 2.1: Basic while loop with counter
    print("\n2.1 Basic while loop:")
    count = 0
    print("Processing batches while count < 5...")
    while count < 5:
        print(f"  Processing batch {count}")
        count += 1  # Critical: update the condition variable
    print(f"  Completed {count} batches")
    
    # Example 2.2: While loop with accumulator
    print("\n2.2 While loop for accumulation:")
    total = 0
    iteration = 1
    target = 100
    
    while total < target:
        total += iteration * 5
        print(f"  Iteration {iteration}: Total = {total}")
        iteration += 1
    
    print(f"  Reached target after {iteration - 1} iterations")
    
    # Example 2.3: Processing data until condition is met
    print("\n2.3 Processing data until threshold:")
    data_queue = [12, 34, 56, 78, 90, 23, 45, 67, 89, 10]
    processed = 0
    index = 0
    threshold = 200
    
    print(f"  Processing until sum reaches {threshold}...")
    while processed < threshold and index < len(data_queue):
        processed += data_queue[index]
        print(f"  Processed item {index + 1}: {data_queue[index]} (Total: {processed})")
        index += 1
    
    print(f"  Stopped after processing {index} items")
    
    # Example 2.4: Simulating data validation
    print("\n2.4 Data validation scenario:")
    attempts = 0
    max_attempts = 3
    simulated_inputs = [15, 150, 50]  # Simulating user inputs (valid range: 0-100)
    
    while attempts < max_attempts:
        value = simulated_inputs[attempts]
        print(f"  Attempt {attempts + 1}: Validating value {value}...")
        
        if 0 <= value <= 100:
            print(f"  ✓ Valid value: {value}")
            break  # Exit loop when valid
        else:
            print(f"  ✗ Invalid value: {value}")
        
        attempts += 1
    
    if attempts == max_attempts:
        print("  Maximum attempts reached")


# =========================================
# 3. CONTROLLING LOOP FLOW
# =========================================

def demonstrate_loop_control():
    """
    Demonstrates loop control using break and continue statements.
    Control statements prevent errors and improve efficiency.
    """
    print("\n" + "=" * 60)
    print("3. CONTROLLING LOOP FLOW - BREAK AND CONTINUE")
    print("=" * 60)
    
    # Example 3.1: Using break to exit early
    print("\n3.1 Using break to exit loop early:")
    print("Searching for first error in data...")
    data_records = [
        {"id": 1, "status": "valid"},
        {"id": 2, "status": "valid"},
        {"id": 3, "status": "error"},
        {"id": 4, "status": "valid"},
        {"id": 5, "status": "error"}
    ]
    
    for record in data_records:
        print(f"  Checking record {record['id']}: {record['status']}")
        if record['status'] == "error":
            print(f"  ! First error found at record {record['id']}")
            break  # Stop processing once error is found
    
    # Example 3.2: Using continue to skip iterations
    print("\n3.2 Using continue to skip iterations:")
    print("Processing only positive values...")
    values = [10, -5, 20, -3, 30, 0, -8, 40]
    
    for value in values:
        if value <= 0:
            print(f"  Skipping non-positive value: {value}")
            continue  # Skip to next iteration
        
        print(f"  Processing positive value: {value}")
    
    # Example 3.3: Combining break and continue
    print("\n3.3 Combining break and continue:")
    print("Processing valid scores until reaching target score...")
    scores = [45, -10, 67, 89, 101, 78, 92, 88]
    valid_scores = []
    target_score = 90
    
    for score in scores:
        # Skip invalid scores (out of range)
        if score < 0 or score > 100:
            print(f"  Skipping invalid score: {score}")
            continue
        
        # Process valid score
        valid_scores.append(score)
        print(f"  Valid score: {score}")
        
        # Stop if we find a score >= target
        if score >= target_score:
            print(f"  ! Target score reached: {score}")
            break
    
    print(f"  Processed {len(valid_scores)} valid scores: {valid_scores}")
    
    # Example 3.4: Nested loops with control
    print("\n3.4 Nested loops with control:")
    print("Finding matching pairs in datasets...")
    dataset_a = [1, 2, 3, 4, 5]
    dataset_b = [3, 6, 9, 12]
    
    found = False
    for a in dataset_a:
        for b in dataset_b:
            if a == b:
                print(f"  Match found: {a}")
                found = True
                break  # Exit inner loop
        if found:
            break  # Exit outer loop
    
    if not found:
        print("  No matches found")


# =========================================
# 4. AVOIDING INFINITE LOOPS
# =========================================

def demonstrate_infinite_loop_prevention():
    """
    Demonstrates common infinite loop pitfalls and how to avoid them.
    Preventing infinite loops saves time and frustration.
    """
    print("\n" + "=" * 60)
    print("4. AVOIDING INFINITE LOOPS")
    print("=" * 60)
    
    # Example 4.1: Common mistake - forgetting to update loop variable
    print("\n4.1 Common mistake - Forgetting to update condition:")
    print("INCORRECT (would cause infinite loop):")
    print("""
    count = 0
    while count < 5:
        print(f"Count: {count}")
        # Missing: count += 1  # <- This causes infinite loop!
    """)
    
    print("CORRECT:")
    count = 0
    while count < 5:
        print(f"  Count: {count}")
        count += 1  # Always update the loop variable!
    
    # Example 4.2: Using safety counter
    print("\n4.2 Using a safety counter to prevent infinite loops:")
    max_iterations = 10
    iteration = 0
    
    print(f"Processing with safety limit of {max_iterations} iterations...")
    while True:  # Potentially infinite
        iteration += 1
        print(f"  Iteration {iteration}")
        
        # Safety check
        if iteration >= max_iterations:
            print(f"  ! Safety limit reached")
            break
        
        # Simulating a condition that might never become False
        if iteration == 7:
            print(f"  Condition met at iteration {iteration}")
            break
    
    # Example 4.3: Ensuring loop condition can change
    print("\n4.3 Ensuring loop variables can change:")
    print("Processing queue until empty...")
    queue = [10, 20, 30, 40, 50]
    
    while len(queue) > 0:  # Condition: queue is not empty
        item = queue.pop(0)  # Remove item - changes the condition!
        print(f"  Processed: {item}, Remaining: {len(queue)}")
    
    print("  Queue is empty - loop terminated correctly")
    
    # Example 4.4: Best practices checklist
    print("\n4.4 Infinite Loop Prevention Checklist:")
    print("""
    ✓ Always update loop variables inside the loop
    ✓ Ensure loop conditions can eventually become False
    ✓ Use for loops when possible (they terminate automatically)
    ✓ Add safety counters for complex while loops
    ✓ Test loops with small examples first
    ✓ Use break statements as emergency exits
    ✓ Keep loop logic simple and readable
    """)


# =========================================
# 5. PRACTICAL DATA WORKFLOW EXAMPLES
# =========================================

def demonstrate_data_workflow():
    """
    Demonstrates practical loop usage in data processing workflows.
    This shows how loops are used in real-world scenarios.
    """
    print("\n" + "=" * 60)
    print("5. PRACTICAL DATA WORKFLOW EXAMPLES")
    print("=" * 60)
    
    # Example 5.1: Data cleaning
    print("\n5.1 Data cleaning workflow:")
    raw_data = [100, 200, -999, 150, None, 180, -999, 220]
    cleaned_data = []
    
    print("Cleaning data (removing nulls and error codes)...")
    for value in raw_data:
        if value is None or value == -999:
            print(f"  Skipping invalid value: {value}")
            continue
        cleaned_data.append(value)
        print(f"  Kept valid value: {value}")
    
    print(f"\nOriginal size: {len(raw_data)}, Cleaned size: {len(cleaned_data)}")
    
    # Example 5.2: Data transformation
    print("\n5.2 Data transformation workflow:")
    celsius_temps = [0, 10, 20, 25, 30, 35]
    fahrenheit_temps = []
    
    print("Converting Celsius to Fahrenheit...")
    for celsius in celsius_temps:
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_temps.append(fahrenheit)
        print(f"  {celsius}°C = {fahrenheit}°F")
    
    # Example 5.3: Data aggregation
    print("\n5.3 Data aggregation workflow:")
    sales_data = [
        {"region": "North", "amount": 1000},
        {"region": "South", "amount": 1500},
        {"region": "North", "amount": 1200},
        {"region": "East", "amount": 800},
        {"region": "South", "amount": 900},
        {"region": "North", "amount": 1100}
    ]
    
    regional_totals = {}
    for sale in sales_data:
        region = sale["region"]
        amount = sale["amount"]
        
        if region not in regional_totals:
            regional_totals[region] = 0
        
        regional_totals[region] += amount
    
    print("Regional sales totals:")
    for region, total in regional_totals.items():
        print(f"  {region}: ${total}")
    
    # Example 5.4: Batch processing
    print("\n5.4 Batch processing workflow:")
    records = list(range(1, 16))  # 15 records
    batch_size = 5
    batch_number = 1
    
    print(f"Processing {len(records)} records in batches of {batch_size}...")
    
    index = 0
    while index < len(records):
        batch = records[index:index + batch_size]
        print(f"  Batch {batch_number}: Processing records {batch}")
        batch_number += 1
        index += batch_size
    
    print("All batches processed successfully")


# =========================================
# MAIN EXECUTION
# =========================================

def main():
    """
    Main function to run all loop demonstrations.
    """
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "PYTHON LOOPS FUNDAMENTALS" + " " * 23 + "║")
    print("║" + " " * 10 + "Iteration & Data Processing" + " " * 21 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Run all demonstrations
    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_loop_control()
    demonstrate_infinite_loop_prevention()
    demonstrate_data_workflow()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("""
You've learned:
✓ How to write for loops for known sequences
✓ How to write while loops for condition-based repetition
✓ How to control loop flow with break and continue
✓ How to identify and prevent infinite loops
✓ How to apply loops in data processing workflows

Next steps:
- Practice writing your own loops
- Combine loops with conditional logic
- Use loops in real data processing tasks
- Record your video demonstration
    """)


if __name__ == "__main__":
    main()
