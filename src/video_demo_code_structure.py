"""
Video Demonstration Script - Structuring Python Code
====================================================
This file contains the exact code to run during your ~2-minute video demonstration
for Learning Unit 4.21: Structuring Python Code for Readability and Reuse.

Usage:
    python src/video_demo_code_structure.py

What to explain in your video:
1. Overview of script structure (sections)
2. Function reuse (DRY principle)
3. Separation of logic and execution
4. Why structure improves readability

Author: Trivin Insight Engine
Date: March 3, 2026
"""

import time


# ============================================================================
# HELPER FUNCTIONS (Explain: These are defined BEFORE we use them)
# ============================================================================

def pause(seconds=1):
    """Helper function to pause between demonstrations"""
    time.sleep(seconds)
    print()


def calculate_percentage(value, total):
    """
    Reusable function to calculate percentage.
    
    EXPLAIN: This function can be used many times,
    instead of writing the same calculation repeatedly.
    """
    if total == 0:
        return 0.0
    return (value / total) * 100


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

def main():
    """
    Main function demonstrating code structure principles.
    
    EXPLAIN: This is the main execution function that calls everything else.
    It keeps our code organized and easy to follow.
    """
    
    print("=" * 70)
    print("STRUCTURING PYTHON CODE FOR READABILITY - VIDEO DEMONSTRATION")
    print("=" * 70)
    print()
    pause(1)

    # =====================================================
    # PART 1: CODE ORGANIZATION (SECTIONS)
    # SAY: "Code is organized into clear sections"
    # =====================================================
    print("╔" + "=" * 68 + "╗")
    print("║  PART 1: ORGANIZED CODE STRUCTURE" + " " * 34 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    print("This script demonstrates proper organization:")
    print("  1. Imports at the top")
    print("  2. Helper functions defined early")
    print("  3. Main logic separated")
    print("  4. Execution at the bottom")
    print()
    print("✓ Anyone can navigate this code easily")
    
    pause(3)

    # =====================================================
    # PART 2: FUNCTION REUSE (DRY PRINCIPLE)
    # SAY: "Functions eliminate code repetition"
    # =====================================================
    print("╔" + "=" * 68 + "╗")
    print("║  PART 2: FUNCTION REUSE (DRY PRINCIPLE)" + " " * 28 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    print("WITHOUT functions (repetitive):")
    print("  response_rate = (360 / 450) * 100")
    print("  completion_rate = (175 / 200) * 100")
    print("  attendance_rate = (42 / 50) * 100")
    print()
    
    print("WITH a reusable function:")
    
    # Using our calculate_percentage function
    response_rate = calculate_percentage(360, 450)
    completion_rate = calculate_percentage(175, 200)
    attendance_rate = calculate_percentage(42, 50)
    
    print(f"  response_rate = calculate_percentage(360, 450) → {response_rate:.1f}%")
    print(f"  completion_rate = calculate_percentage(175, 200) → {completion_rate:.1f}%")
    print(f"  attendance_rate = calculate_percentage(42, 50) → {attendance_rate:.1f}%")
    print()
    print("✓ Function defined once, used multiple times")
    print("✓ Changes made in one place, not three")
    
    pause(3)

    # =====================================================
    # PART 3: SEPARATED LOGIC AND EXECUTION
    # SAY: "Logic is separated from execution for clarity"
    # =====================================================
    print("╔" + "=" * 68 + "╗")
    print("║  PART 3: SEPARATED LOGIC AND EXECUTION" + " " * 29 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    # Define a clear, single-purpose function
    def calculate_bonus(salary, bonus_percent=0.15):
        """Calculate employee bonus - simple and clear"""
        return salary * bonus_percent
    
    # Clean execution using the function
    employee_salary = 75000
    employee_bonus = calculate_bonus(employee_salary)
    
    print("Function definition (logic):")
    print("  def calculate_bonus(salary, bonus_percent=0.15):")
    print("      return salary * bonus_percent")
    print()
    print("Clean execution:")
    print(f"  employee_salary = {employee_salary}")
    print(f"  employee_bonus = calculate_bonus(employee_salary)")
    print(f"  Result: ${employee_bonus:,.2f}")
    print()
    print("✓ Functions defined first, then used")
    print("✓ Execution code is readable and simple")
    
    pause(3)

    # =====================================================
    # PART 4: READABILITY BENEFITS
    # SAY: "Good structure makes code maintainable"
    # =====================================================
    print("╔" + "=" * 68 + "╗")
    print("║  PART 4: WHY STRUCTURE MATTERS" + " " * 37 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    print("Well-structured code is:")
    print("  ✓ Easy to read and understand")
    print("  ✓ Easy to debug when issues arise")
    print("  ✓ Easy to modify and extend")
    print("  ✓ Easy for others to collaborate on")
    print()
    
    # Real example with good structure
    survey_scores = [4, 5, 3, 4, 5, 4, 3, 5]
    average_score = sum(survey_scores) / len(survey_scores)
    
    print("Example - Clear variable names and flow:")
    print(f"  survey_scores = {survey_scores}")
    print(f"  average_score = {average_score:.2f}")
    print(f"  satisfaction_rate = {calculate_percentage(average_score, 5):.1f}%")
    print()
    print("✓ Code reads like a story from top to bottom")
    
    pause(2)

    # =====================================================
    # VIDEO SUMMARY
    # =====================================================
    print("\n" + "=" * 70)
    print("VIDEO SUMMARY - LEARNING UNIT 4.21")
    print("=" * 70)
    print("""
✓ You saw code organized into clear sections
✓ You saw functions eliminate repetition (DRY)
✓ You saw logic separated from execution
✓ You learned why structure improves readability and collaboration

KEY STRUCTURE PATTERN:
  1. Imports at top
  2. Constants and configuration
  3. Helper functions (defined early)
  4. Main logic functions
  5. Execution code (clean and minimal)

This structure makes code maintainable and scalable!
""")
    print("=" * 70)
    print("End of demonstration - Ready for your video!")
    print("=" * 70)


# ============================================================================
# ENTRY POINT
# EXPLAIN: This ensures code only runs when file is executed directly
# ============================================================================

if __name__ == "__main__":
    # EXPLAIN: All logic flows through main(), keeping execution organized
    main()
