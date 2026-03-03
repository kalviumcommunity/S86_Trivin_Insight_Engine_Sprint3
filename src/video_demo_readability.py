"""
Video Demonstration Script - Readable Variable Names and Comments
=================================================================
This file contains the exact code to run during your ~2-minute video demonstration.

Usage:
    python src/video_demo_readability.py
"""

import time


def pause(seconds=1):
    """Helper function to pause between demonstrations"""
    time.sleep(seconds)
    print()


def main():
    print("=" * 70)
    print("READABLE VARIABLE NAMES & COMMENTS - VIDEO DEMONSTRATION")
    print("=" * 70)
    print()
    pause(1)

    # =====================================================
    # PART 1: GOOD VS POOR VARIABLE NAMES
    # =====================================================
    print("╔" + "=" * 68 + "╗")
    print("║  PART 1: GOOD VS POOR VARIABLE NAMES" + " " * 30 + "║")
    print("╚" + "=" * 68 + "╝")
    print()

    x = 120
    tmp = 0.72
    val = "Sales"

    print("Poor naming:")
    print(f"  x = {x}, tmp = {tmp}, val = {val}")

    total_employee_count = 120
    quarterly_attrition_rate = 0.72
    department_name = "Sales"

    print("\nReadable naming:")
    print(
        "  total_employee_count = "
        f"{total_employee_count}, quarterly_attrition_rate = "
        f"{quarterly_attrition_rate}, department_name = {department_name}"
    )

    pause(2)

    # =====================================================
    # PART 2: PEP 8 NAMING CONVENTIONS
    # =====================================================
    print("╔" + "=" * 68 + "╗")
    print("║  PART 2: PEP 8 NAMING STYLE" + " " * 40 + "║")
    print("╚" + "=" * 68 + "╝")
    print()

    average_satisfaction_score = 4.4
    MAX_SURVEY_SCORE = 5

    print("snake_case variable:")
    print(f"  average_satisfaction_score = {average_satisfaction_score}")

    print("\nUPPER_CASE constant:")
    print(f"  MAX_SURVEY_SCORE = {MAX_SURVEY_SCORE}")

    pause(2)

    # =====================================================
    # PART 3: USEFUL COMMENTS (WHY, NOT WHAT)
    # =====================================================
    print("╔" + "=" * 68 + "╗")
    print("║  PART 3: USEFUL COMMENTS" + " " * 43 + "║")
    print("╚" + "=" * 68 + "╝")
    print()

    raw_score = 38
    max_possible_score = 50

    # Convert to percentage so different surveys can be compared consistently.
    score_percentage = (raw_score / max_possible_score) * 100

    print("Useful comment example:")
    print("  # Convert to percentage so different surveys can be compared consistently")
    print(f"  score_percentage = {score_percentage:.1f}")

    pause(1)

    print("\n" + "=" * 70)
    print("VIDEO SUMMARY")
    print("=" * 70)
    print("""
✓ You saw poor vs good variable names
✓ You saw corrected names using PEP 8 style
✓ You saw useful comments that explain intent
✓ You learned why readability improves collaboration

This covers the readability milestone requirements.
""")


if __name__ == "__main__":
    main()
