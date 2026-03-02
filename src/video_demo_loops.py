"""
Video Demonstration Script - Python Loops
==========================================
This file contains the exact code to run during your 2-minute video demonstration.
Simply run this file and explain each section as it executes.

Usage:
    python src/video_demo_loops.py
"""

import time


def pause(seconds=1):
    """Helper function to pause between demonstrations"""
    time.sleep(seconds)
    print()


def main():
    print("=" * 60)
    print("PYTHON LOOPS FUNDAMENTALS - VIDEO DEMONSTRATION")
    print("=" * 60)
    print()
    pause(1)
    
    # =====================================================
    # PART 1: FOR LOOP DEMONSTRATION
    # =====================================================
    print("╔" + "=" * 58 + "╗")
    print("║  PART 1: FOR LOOP - ITERATING OVER DATA" + " " * 17 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    # Example: Filtering survey data
    print("Example: Analyzing Survey Responses")
    print("-" * 40)
    
    survey_responses = [3, 5, 2, 4, 5, 1, 4, 5, 3, 4]
    high_ratings = []
    
    print(f"Survey data: {survey_responses}")
    print()
    
    for rating in survey_responses:
        if rating >= 4:
            high_ratings.append(rating)
    
    print(f"Total responses: {len(survey_responses)}")
    print(f"High ratings (≥4): {len(high_ratings)}")
    print(f"Satisfaction rate: {(len(high_ratings) / len(survey_responses)) * 100:.1f}%")
    
    pause(2)
    
    # =====================================================
    # PART 2: WHILE LOOP DEMONSTRATION
    # =====================================================
    print("╔" + "=" * 58 + "╗")
    print("║  PART 2: WHILE LOOP - CONDITION-BASED REPETITION" + " " * 8 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    print("Example: Processing Data in Batches")
    print("-" * 40)
    
    batch_number = 1
    total_processed = 0
    target = 50
    
    print(f"Target: {target} items")
    print("Processing batches:")
    print()
    
    while total_processed < target:
        print(f"  Batch {batch_number}: Processing 10 items...")
        total_processed += 10
        batch_number += 1
        time.sleep(0.3)  # Visual pause for video
    
    print()
    print(f"✓ Processed {total_processed} items in {batch_number - 1} batches")
    
    pause(2)
    
    # =====================================================
    # PART 3: LOOP CONTROL (BREAK & CONTINUE)
    # =====================================================
    print("╔" + "=" * 58 + "╗")
    print("║  PART 3: LOOP CONTROL - BREAK & CONTINUE" + " " * 16 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    print("Example: Validating and Processing Scores")
    print("-" * 40)
    
    scores = [45, -10, 67, 89, 101, 78, 92, 88]
    valid_scores = []
    target_score = 90
    
    print(f"Score data: {scores}")
    print(f"Target score: {target_score}")
    print(f"Valid range: 0-100")
    print()
    
    for score in scores:
        # Skip invalid scores using continue
        if score < 0 or score > 100:
            print(f"  ⊗ Skipping invalid score: {score}")
            continue
        
        # Process valid score
        valid_scores.append(score)
        print(f"  ✓ Valid score: {score}")
        
        # Exit loop with break when target reached
        if score >= target_score:
            print(f"  ! Target score {target_score} reached! Stopping.")
            break
    
    print()
    print(f"Collected {len(valid_scores)} valid scores: {valid_scores}")
    
    pause(1)
    
    # =====================================================
    # SUMMARY
    # =====================================================
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("""
✓ FOR LOOPS iterate over sequences (lists, ranges, etc.)
  - Ideal when you know the data structure
  - Clean and readable syntax
  
✓ WHILE LOOPS repeat based on conditions
  - Useful when iterations depend on changing conditions
  - Remember to update loop variables!
  
✓ BREAK exits loops early
  - Stop when specific condition is met
  - Saves unnecessary processing
  
✓ CONTINUE skips iterations
  - Skip invalid or unwanted data
  - Continue with next iteration

These are fundamental tools for data processing in Python!
""")


if __name__ == "__main__":
    main()
    print("\n" + "=" * 60)
    print("Video demonstration complete!")
    print("=" * 60)
