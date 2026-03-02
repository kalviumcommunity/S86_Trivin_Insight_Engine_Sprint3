"""
Video Demonstration Script - Python Functions
==============================================
This file contains the exact code to run during your ~2-minute video demonstration.

Usage:
    python src/video_demo_functions.py
"""

import time


def pause(seconds=1):
    """Helper function to pause between demonstrations"""
    time.sleep(seconds)
    print()


def main():
    print("=" * 60)
    print("PYTHON FUNCTIONS FUNDAMENTALS - VIDEO DEMONSTRATION")
    print("=" * 60)
    print()
    pause(1)

    # =====================================================
    # PART 1: DEFINING AND CALLING A FUNCTION
    # =====================================================
    print("╔" + "=" * 58 + "╗")
    print("║  PART 1: DEFINING AND CALLING A FUNCTION" + " " * 16 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    def greet():
        print("Hello! This is a reusable function.")

    print("Defined function: greet()")
    print("Calling greet() now:")
    greet()

    pause(2)

    # =====================================================
    # PART 2: PARAMETERS AND ARGUMENTS
    # =====================================================
    print("╔" + "=" * 58 + "╗")
    print("║  PART 2: PARAMETERS AND ARGUMENTS" + " " * 25 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    def add_numbers(a, b):
        return a + b

    x = 12
    y = 8
    result = add_numbers(x, y)

    print(f"Function call: add_numbers({x}, {y})")
    print(f"Result: {result}")

    pause(2)

    # =====================================================
    # PART 3: FUNCTION EXECUTION FLOW + SCOPE
    # =====================================================
    print("╔" + "=" * 58 + "╗")
    print("║  PART 3: EXECUTION FLOW AND SCOPE" + " " * 24 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    message = "I am global"

    def show_scope(name):
        local_text = "I am local"
        print(f"Inside function for {name}:")
        print(f"  local_text -> {local_text}")
        print(f"  message -> {message}")

    print("Before calling show_scope('Trivin')")
    show_scope("Trivin")
    print("After function call, execution returns to main flow")

    pause(1)

    print("\n" + "=" * 60)
    print("VIDEO SUMMARY")
    print("=" * 60)
    print("""
✓ You defined a function using def
✓ You called functions by name
✓ You passed arguments into parameters
✓ You observed function execution flow
✓ You saw local vs global variable behavior

This covers Milestone 4.18 requirements.
""")


if __name__ == "__main__":
    main()
