"""
Collections Fundamentals - Learning Unit 4.15
Working with Python Lists, Tuples, and Dictionaries

This module demonstrates:
1. Working with Python Lists
2. Working with Python Tuples
3. Working with Python Dictionaries
4. Choosing the Right Data Structure
5. Practical Applications

Author: Trivin Insight Engine
Date: February 27, 2026
"""


def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


# ============================================================================
# 1. WORKING WITH PYTHON LISTS
# ============================================================================

def demonstrate_lists():
    """Demonstrate Python lists - ordered, mutable collections"""
    section_header("1. Working with Python Lists")
    
    # Creating lists
    print("\n--- CREATING LISTS ---")
    employees = ["Alice", "Bob", "Charlie", "Diana"]
    scores = [85, 92, 78, 95, 88]
    mixed_data = ["John", 30, 75000.50, True]
    empty_list = []
    
    print(f"Employee names: {employees}")
    print(f"Test scores: {scores}")
    print(f"Mixed data: {mixed_data}")
    print(f"Empty list: {empty_list}")
    print(f"Type: {type(employees)}")
    
    # Accessing elements by index
    print("\n--- ACCESSING LIST ELEMENTS ---")
    departments = ["Engineering", "Sales", "Marketing", "HR", "Finance"]
    
    print(f"All departments: {departments}")
    print(f"First department: {departments[0]}")
    print(f"Last department: {departments[-1]}")
    print(f"Second and third: {departments[1:3]}")
    print(f"First three: {departments[:3]}")
    print(f"Last two: {departments[-2:]}")
    
    # List length
    print(f"Number of departments: {len(departments)}")
    
    # Modifying lists (MUTABLE)
    print("\n--- MODIFYING LISTS ---")
    survey_scores = [4, 5, 3, 4, 5]
    print(f"Original scores: {survey_scores}")
    
    # Change an element
    survey_scores[2] = 5  # Change third element
    print(f"After updating index 2 to 5: {survey_scores}")
    
    # Add elements
    survey_scores.append(4)  # Add to end
    print(f"After append(4): {survey_scores}")
    
    survey_scores.insert(0, 3)  # Insert at beginning
    print(f"After insert(0, 3): {survey_scores}")
    
    # Remove elements
    survey_scores.remove(3)  # Remove first occurrence of 3
    print(f"After remove(3): {survey_scores}")
    
    last_score = survey_scores.pop()  # Remove and return last element
    print(f"Popped element: {last_score}")
    print(f"After pop(): {survey_scores}")
    
    # List methods
    print("\n--- LIST METHODS ---")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original: {numbers}")
    
    numbers.sort()  # Sort in place
    print(f"After sort(): {numbers}")
    
    numbers.reverse()  # Reverse in place
    print(f"After reverse(): {numbers}")
    
    count_of_1 = numbers.count(1)
    print(f"Count of 1: {count_of_1}")
    
    index_of_5 = numbers.index(5)
    print(f"Index of 5: {index_of_5}")
    
    # List operations
    print("\n--- LIST OPERATIONS ---")
    team_a = ["Alice", "Bob"]
    team_b = ["Charlie", "Diana"]
    
    # Concatenation
    all_members = team_a + team_b
    print(f"Combined teams: {all_members}")
    
    # Repetition
    repeated = ["X"] * 5
    print(f"Repeated list: {repeated}")
    
    # Membership testing
    print(f"Is 'Alice' in team_a? {'Alice' in team_a}")
    print(f"Is 'Eve' in team_a? {'Eve' in team_a}")
    
    # List iteration
    print("\n--- ITERATING OVER LISTS ---")
    ratings = [4.2, 4.5, 3.8, 4.9, 4.1]
    print("Individual ratings:")
    for i, rating in enumerate(ratings, start=1):
        print(f"  Rating {i}: {rating}")
    
    # List comprehension (bonus)
    print("\n--- LIST COMPREHENSION (BONUS) ---")
    original = [1, 2, 3, 4, 5]
    squared = [x ** 2 for x in original]
    print(f"Original: {original}")
    print(f"Squared: {squared}")
    
    # Filter even numbers
    evens = [x for x in original if x % 2 == 0]
    print(f"Even numbers: {evens}")


# ============================================================================
# 2. WORKING WITH PYTHON TUPLES
# ============================================================================

def demonstrate_tuples():
    """Demonstrate Python tuples - ordered, immutable collections"""
    section_header("2. Working with Python Tuples")
    
    # Creating tuples
    print("\n--- CREATING TUPLES ---")
    coordinates = (10, 20)
    employee_info = ("John Doe", 1001, "Engineering", 75000)
    single_element = (42,)  # Note the comma!
    from_list = tuple([1, 2, 3])
    
    print(f"Coordinates: {coordinates}")
    print(f"Employee info: {employee_info}")
    print(f"Single element tuple: {single_element}")
    print(f"From list: {from_list}")
    print(f"Type: {type(coordinates)}")
    
    # Accessing tuple elements
    print("\n--- ACCESSING TUPLE ELEMENTS ---")
    person = ("Alice", 30, "Data Scientist", "New York")
    
    print(f"Full tuple: {person}")
    print(f"Name (index 0): {person[0]}")
    print(f"Age (index 1): {person[1]}")
    print(f"Job (index 2): {person[2]}")
    print(f"City (index -1): {person[-1]}")
    print(f"First two elements: {person[:2]}")
    
    # Tuple unpacking
    print("\n--- TUPLE UNPACKING ---")
    name, age, job, city = person
    print(f"Unpacked values:")
    print(f"  Name: {name}")
    print(f"  Age: {age}")
    print(f"  Job: {job}")
    print(f"  City: {city}")
    
    # Swapping values using tuples
    x, y = 10, 20
    print(f"\nBefore swap: x={x}, y={y}")
    x, y = y, x  # Elegant swap using tuple unpacking
    print(f"After swap: x={x}, y={y}")
    
    # Immutability demonstration
    print("\n--- TUPLE IMMUTABILITY ---")
    config = ("localhost", 8080, "production")
    print(f"Original config: {config}")
    
    # This would cause an error (commented out):
    # config[1] = 9090  # TypeError: 'tuple' object does not support item assignment
    print("❌ Cannot modify: config[1] = 9090  (TypeError)")
    print("✓ Tuples are immutable - values cannot be changed after creation")
    
    # To "change" a tuple, create a new one
    new_config = (config[0], 9090, config[2])
    print(f"New config tuple: {new_config}")
    
    # Tuple methods (limited because immutable)
    print("\n--- TUPLE METHODS ---")
    data = (1, 2, 3, 2, 4, 2, 5)
    print(f"Data: {data}")
    print(f"Count of 2: {data.count(2)}")
    print(f"Index of 3: {data.index(3)}")
    print(f"Length: {len(data)}")
    
    # When to use tuples
    print("\n--- WHEN TO USE TUPLES ---")
    print("Use tuples when:")
    print("  ✓ Data should not change (coordinates, RGB colors, dates)")
    print("  ✓ Returning multiple values from a function")
    print("  ✓ Using as dictionary keys (immutable)")
    print("  ✓ Performance is critical (tuples are faster)")
    
    # Example: Function returning tuple
    def get_employee_summary(emp_id):
        """Return employee data as tuple (immutable)"""
        return ("Jennifer Smith", emp_id, "Engineering", 4.7)
    
    employee = get_employee_summary(1001)
    print(f"\nEmployee summary: {employee}")
    print(f"Name: {employee[0]}, Rating: {employee[3]}")


# ============================================================================
# 3. WORKING WITH PYTHON DICTIONARIES
# ============================================================================

def demonstrate_dictionaries():
    """Demonstrate Python dictionaries - key-value pairs, mutable"""
    section_header("3. Working with Python Dictionaries")
    
    # Creating dictionaries
    print("\n--- CREATING DICTIONARIES ---")
    employee = {
        "name": "Alice Johnson",
        "id": 1001,
        "department": "Data Science",
        "salary": 75000
    }
    
    scores = {"math": 85, "science": 92, "english": 88}
    empty_dict = {}
    from_pairs = dict([("a", 1), ("b", 2)])
    
    print(f"Employee: {employee}")
    print(f"Scores: {scores}")
    print(f"Empty dict: {empty_dict}")
    print(f"From pairs: {from_pairs}")
    print(f"Type: {type(employee)}")
    
    # Accessing values by key
    print("\n--- ACCESSING DICTIONARY VALUES ---")
    print(f"Employee name: {employee['name']}")
    print(f"Employee ID: {employee['id']}")
    print(f"Department: {employee['department']}")
    
    # Safe access with .get()
    print(f"\nUsing .get() method:")
    print(f"Salary: {employee.get('salary')}")
    print(f"Age (not exists): {employee.get('age')}")  # Returns None
    print(f"Age with default: {employee.get('age', 'Not specified')}")
    
    # Modifying dictionaries (MUTABLE)
    print("\n--- MODIFYING DICTIONARIES ---")
    survey_data = {
        "respondent_id": 1,
        "satisfaction": 4.5,
        "department": "Engineering"
    }
    print(f"Original: {survey_data}")
    
    # Update existing key
    survey_data["satisfaction"] = 4.8
    print(f"After updating satisfaction: {survey_data}")
    
    # Add new key-value pair
    survey_data["response_date"] = "2026-02-27"
    print(f"After adding date: {survey_data}")
    
    # Remove key-value pair
    removed_value = survey_data.pop("department")
    print(f"Removed department: {removed_value}")
    print(f"After removal: {survey_data}")
    
    # Dictionary methods
    print("\n--- DICTIONARY METHODS ---")
    data = {"a": 1, "b": 2, "c": 3}
    
    print(f"Dictionary: {data}")
    print(f"Keys: {list(data.keys())}")
    print(f"Values: {list(data.values())}")
    print(f"Items (key-value pairs): {list(data.items())}")
    
    # Check if key exists
    print(f"\n'a' in data? {'a' in data}")
    print(f"'z' in data? {'z' in data}")
    
    # Iterating over dictionaries
    print("\n--- ITERATING OVER DICTIONARIES ---")
    department_counts = {
        "Engineering": 25,
        "Sales": 18,
        "Marketing": 12,
        "HR": 8
    }
    
    print("Department employee counts:")
    for dept, count in department_counts.items():
        print(f"  {dept}: {count} employees")
    
    # Dictionary update
    print("\n--- UPDATING DICTIONARIES ---")
    base_config = {"host": "localhost", "port": 8080}
    updates = {"port": 9090, "timeout": 30}
    
    print(f"Base config: {base_config}")
    print(f"Updates: {updates}")
    
    base_config.update(updates)
    print(f"After update: {base_config}")
    
    # Nested dictionaries
    print("\n--- NESTED DICTIONARIES ---")
    employees = {
        "emp001": {
            "name": "Alice",
            "department": "Engineering",
            "salary": 75000
        },
        "emp002": {
            "name": "Bob",
            "department": "Sales",
            "salary": 65000
        }
    }
    
    print("Employees database:")
    for emp_id, emp_data in employees.items():
        print(f"  {emp_id}: {emp_data['name']} - {emp_data['department']}")
    
    # Complex data example
    print("\n--- COMPLEX DATA STRUCTURE ---")
    survey_response = {
        "response_id": 101,
        "employee": {
            "id": 1001,
            "name": "Jennifer Smith",
            "department": "Data Science"
        },
        "scores": {
            "work_life_balance": 4.5,
            "career_growth": 4.2,
            "management": 4.8
        },
        "comments": ["Great team", "Good benefits"],
        "recommend": True
    }
    
    print(f"Response ID: {survey_response['response_id']}")
    print(f"Employee: {survey_response['employee']['name']}")
    print(f"Management score: {survey_response['scores']['management']}")
    print(f"First comment: {survey_response['comments'][0]}")
    print(f"Would recommend: {survey_response['recommend']}")


# ============================================================================
# 4. CHOOSING THE RIGHT DATA STRUCTURE
# ============================================================================

def demonstrate_structure_choice():
    """Demonstrate when to use each data structure"""
    section_header("4. Choosing the Right Data Structure")
    
    print("\n--- COMPARISON TABLE ---")
    print(f"{'Feature':<20} {'List':<15} {'Tuple':<15} {'Dictionary':<20}")
    print("-" * 70)
    print(f"{'Ordered':<20} {'Yes':<15} {'Yes':<15} {'No (3.7+: Yes)':<20}")
    print(f"{'Mutable':<20} {'Yes':<15} {'No':<15} {'Yes':<20}")
    print(f"{'Indexed by':<20} {'Position (0,1,2...)':<15} {'Position':<15} {'Key (any hashable)':<20}")
    print(f"{'Duplicates':<20} {'Yes':<15} {'Yes':<15} {'Keys: No, Values: Yes':<20}")
    print(f"{'Syntax':<20} {'[1, 2, 3]':<15} {'(1, 2, 3)':<15} {'{\"a\": 1, \"b\": 2}':<20}")
    
    # Use case examples
    print("\n--- USE CASE: LISTS ---")
    print("✓ Use lists when:")
    print("  - Order matters")
    print("  - You need to modify contents")
    print("  - You have a collection of similar items")
    print("  - You need to sort or filter items")
    
    # Example: Survey responses over time
    daily_scores = [4.2, 4.5, 4.3, 4.7, 4.4]
    print(f"\nExample - Daily survey scores: {daily_scores}")
    print(f"Average: {sum(daily_scores) / len(daily_scores):.2f}")
    
    print("\n--- USE CASE: TUPLES ---")
    print("✓ Use tuples when:")
    print("  - Data should never change")
    print("  - Protecting data from accidental modification")
    print("  - Returning multiple values from functions")
    print("  - Using as dictionary keys")
    
    # Example: Database record
    employee_record = (1001, "Alice Johnson", "2020-01-15", "Engineering")
    print(f"\nExample - Employee record: {employee_record}")
    print("(Cannot accidentally change hire date or ID)")
    
    # Using tuple as dictionary key
    location_data = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles"
    }
    print(f"\nUsing tuples as dictionary keys:")
    print(f"Location at (40.7128, -74.0060): {location_data[(40.7128, -74.0060)]}")
    
    print("\n--- USE CASE: DICTIONARIES ---")
    print("✓ Use dictionaries when:")
    print("  - You need to look up values by meaningful keys")
    print("  - Modeling real-world entities with attributes")
    print("  - Data has labeled fields")
    print("  - You need fast lookups")
    
    # Example: Employee profile
    employee_profile = {
        "id": 1001,
        "name": "Alice Johnson",
        "email": "alice.j@company.com",
        "department": "Data Science",
        "skills": ["Python", "SQL", "Machine Learning"],
        "ratings": {"technical": 4.8, "communication": 4.5}
    }
    print(f"\nExample - Employee profile:")
    print(f"  Name: {employee_profile['name']}")
    print(f"  Department: {employee_profile['department']}")
    print(f"  Skills: {', '.join(employee_profile['skills'])}")
    
    # Comparative example
    print("\n--- SAME DATA, DIFFERENT STRUCTURES ---")
    
    # As list (positional)
    person_list = ["John", 30, "Engineer"]
    print(f"As list: {person_list}")
    print(f"  Access by position: name={person_list[0]}, age={person_list[1]}")
    print("  Issue: What does index 2 mean? Not self-documenting")
    
    # As tuple (positional, immutable)
    person_tuple = ("John", 30, "Engineer")
    print(f"\nAs tuple: {person_tuple}")
    print(f"  Access by position: name={person_tuple[0]}, age={person_tuple[1]}")
    print("  Benefit: Cannot accidentally modify")
    
    # As dictionary (labeled, clear)
    person_dict = {"name": "John", "age": 30, "job": "Engineer"}
    print(f"\nAs dictionary: {person_dict}")
    print(f"  Access by key: name={person_dict['name']}, age={person_dict['age']}")
    print("  Benefit: Self-documenting, keys explain meaning")
    
    # Performance considerations
    print("\n--- PERFORMANCE NOTES ---")
    print("List: Fast index access O(1), slow search O(n)")
    print("Tuple: Faster than list (immutable), less memory")
    print("Dictionary: Very fast key lookup O(1), more memory")


# ============================================================================
# 5. PRACTICAL APPLICATIONS
# ============================================================================

def demonstrate_practical_applications():
    """Real-world examples using collections effectively"""
    section_header("5. Practical Applications")
    
    print("\n--- EMPLOYEE SURVEY SYSTEM ---")
    
    # Using all three collections together
    
    # List of survey questions (ordered)
    questions = [
        "Rate your work-life balance (1-5)",
        "Rate career growth opportunities (1-5)",
        "Rate your immediate manager (1-5)",
        "Would you recommend this company?"
    ]
    
    print("Survey Questions (List):")
    for i, question in enumerate(questions, start=1):
        print(f"  Q{i}. {question}")
    
    # Employee info tuple (immutable)
    employee_info = (1001, "Jennifer Smith", "Data Science", "2020-01-15")
    emp_id, emp_name, emp_dept, emp_hire_date = employee_info
    
    print(f"\nEmployee Info (Tuple - Immutable):")
    print(f"  ID: {emp_id}")
    print(f"  Name: {emp_name}")
    print(f"  Department: {emp_dept}")
    print(f"  Hire Date: {emp_hire_date}")
    
    # Survey response as dictionary (key-value pairs)
    survey_response = {
        "employee_id": emp_id,
        "response_date": "2026-02-27",
        "scores": {
            "work_life_balance": 4.5,
            "career_growth": 4.2,
            "management": 4.8,
            "overall": 4.5
        },
        "would_recommend": True,
        "comments": "Great team culture and learning opportunities",
        "response_time_minutes": 8
    }
    
    print(f"\nSurvey Response (Dictionary):")
    print(f"  Employee ID: {survey_response['employee_id']}")
    print(f"  Date: {survey_response['response_date']}")
    print(f"  Scores:")
    for category, score in survey_response['scores'].items():
        print(f"    - {category.replace('_', ' ').title()}: {score}")
    print(f"  Recommends company: {survey_response['would_recommend']}")
    print(f"  Comments: {survey_response['comments']}")
    
    # Multiple survey responses (list of dictionaries)
    print("\n--- MULTIPLE SURVEY RESPONSES ---")
    all_responses = [
        {
            "employee_id": 1001,
            "department": "Data Science",
            "overall_score": 4.5,
            "would_recommend": True
        },
        {
            "employee_id": 1002,
            "department": "Engineering",
            "overall_score": 4.8,
            "would_recommend": True
        },
        {
            "employee_id": 1003,
            "department": "Sales",
            "overall_score": 3.9,
            "would_recommend": False
        }
    ]
    
    print("All Survey Responses:")
    for response in all_responses:
        recommend_text = "Yes" if response['would_recommend'] else "No"
        print(f"  Emp {response['employee_id']} ({response['department']}): "
              f"Score {response['overall_score']}, Recommend: {recommend_text}")
    
    # Calculate statistics
    total_score = sum(r['overall_score'] for r in all_responses)
    avg_score = total_score / len(all_responses)
    recommend_count = sum(1 for r in all_responses if r['would_recommend'])
    recommend_rate = (recommend_count / len(all_responses)) * 100
    
    print(f"\nSummary Statistics:")
    print(f"  Total responses: {len(all_responses)}")
    print(f"  Average score: {avg_score:.2f}")
    print(f"  Recommendation rate: {recommend_rate:.1f}%")
    
    # Department-wise aggregation
    print("\n--- DEPARTMENT ANALYSIS ---")
    dept_scores = {}  # Dictionary to store department data
    
    for response in all_responses:
        dept = response['department']
        score = response['overall_score']
        
        if dept not in dept_scores:
            dept_scores[dept] = []
        dept_scores[dept].append(score)
    
    print("Average scores by department:")
    for dept, scores in dept_scores.items():
        avg = sum(scores) / len(scores)
        print(f"  {dept}: {avg:.2f} (from {len(scores)} response(s))")
    
    # Configuration using named constants
    print("\n--- CONFIGURATION EXAMPLE ---")
    
    # Tuple for configuration (immutable)
    DB_CONFIG = ("localhost", 5432, "survey_db", "readonly_user")
    host, port, database, user = DB_CONFIG
    print(f"Database Config (Tuple):")
    print(f"  Host: {host}:{port}")
    print(f"  Database: {database}")
    print(f"  User: {user}")
    
    # Dictionary for settings (flexible)
    APP_SETTINGS = {
        "max_response_time": 30,
        "auto_save": True,
        "language": "en",
        "theme": "light",
        "notifications": True
    }
    print(f"\nApp Settings (Dictionary):")
    for key, value in APP_SETTINGS.items():
        print(f"  {key}: {value}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all demonstrations"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*  LEARNING UNIT 4.15: PYTHON COLLECTIONS               *")
    print("*  Lists, Tuples, and Dictionaries                     *")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    
    # Run all demonstrations
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_structure_choice()
    demonstrate_practical_applications()
    
    # Summary
    section_header("Summary and Key Takeaways")
    print("""
    ✓ Lists: Ordered, mutable, indexed by position [1, 2, 3]
    ✓ Tuples: Ordered, immutable, indexed by position (1, 2, 3)
    ✓ Dictionaries: Unordered*, mutable, accessed by key {"a": 1}
    
    When to use:
    • Lists → Dynamic collections that change
    • Tuples → Fixed data that shouldn't change
    • Dictionaries → Data with meaningful labels/keys
    
    Best practices:
    • Choose the right structure for your data
    • Use tuples for data integrity
    • Use dictionaries for self-documenting code
    • Combine structures for complex data
    
    *Python 3.7+ maintains insertion order for dictionaries
    """)
    
    print("\n" + "=" * 60)
    print("  Demonstration Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
