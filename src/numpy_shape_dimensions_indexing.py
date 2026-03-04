"""
NumPy Milestone: Understanding Array Shape, Dimensions, and Index Positions

This script focuses on:
1. Understanding array shape
2. Understanding dimensions (ndim)
3. Accessing elements using index positions
4. Visualizing array layout
5. Avoiding common indexing mistakes

Author: Trivin Insight Engine
Date: March 4, 2026
"""

import numpy as np


def section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 72)
    print(f"  {title}")
    print("=" * 72)


def understand_shape():
    """Demonstrate what shape means in NumPy arrays."""
    section_header("1. Understanding Array Shape")

    array_1d = np.array([10, 20, 30, 40, 50])
    print("\n1D array:", array_1d)
    print("Shape:", array_1d.shape)
    print("Meaning: one axis with 5 values")

    array_2d = np.array([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
    ])
    print("\n2D array:\n", array_2d)
    print("Shape:", array_2d.shape)
    print("Meaning: 3 rows and 3 columns")

    print("\nShape reminder:")
    print("- 1D shape looks like: (length,)")
    print("- 2D shape looks like: (rows, columns)")


def understand_dimensions():
    """Demonstrate ndim and basic axis understanding."""
    section_header("2. Understanding Dimensions (ndim)")

    array_1d = np.array([5, 10, 15, 20])
    array_2d = np.array([
        [1, 2, 3],
        [4, 5, 6],
    ])
    array_3d = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ])

    print("\n1D array:", array_1d)
    print("Shape:", array_1d.shape, "| ndim:", array_1d.ndim)

    print("\n2D array:\n", array_2d)
    print("Shape:", array_2d.shape, "| ndim:", array_2d.ndim)

    print("\n3D array:\n", array_3d)
    print("Shape:", array_3d.shape, "| ndim:", array_3d.ndim)

    print("\nAxis intuition:")
    print("- Axis 0: moves down rows (or blocks in higher dimensions)")
    print("- Axis 1: moves across columns in a 2D array")


def access_by_index_positions():
    """Show safe and correct index-based access for 1D and 2D arrays."""
    section_header("3. Accessing Elements Using Index Positions")

    one_d = np.array([100, 200, 300, 400])
    print("\n1D array:", one_d)
    print("Index 0 ->", one_d[0])
    print("Index 2 ->", one_d[2])
    print("Index 3 ->", one_d[3])

    two_d = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
    ])
    print("\n2D array:\n", two_d)
    print("Shape:", two_d.shape, "(rows, columns)")
    print("Element at row 0, col 0 ->", two_d[0, 0])
    print("Element at row 1, col 2 ->", two_d[1, 2])
    print("Element at row 2, col 3 ->", two_d[2, 3])

    print("\nZero-based indexing reminder:")
    print("- First element is at index 0")
    print("- Last valid row index is rows - 1")
    print("- Last valid column index is columns - 1")

    print("\nCommon indexing mistakes (demonstrated safely):")
    try:
        print(two_d[3, 0])
    except IndexError as error:
        print("- Access two_d[3, 0] -> IndexError:", error)

    try:
        print(two_d[1, 4])
    except IndexError as error:
        print("- Access two_d[1, 4] -> IndexError:", error)


def visualize_layout():
    """Help build a row-column mental model for index positions."""
    section_header("4. Visualizing Array Layout")

    grid = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    print("\nArray grid:\n", grid)
    print("\nIndex map (row, col) -> value")

    for row_idx in range(grid.shape[0]):
        for col_idx in range(grid.shape[1]):
            print(f"({row_idx}, {col_idx}) -> {grid[row_idx, col_idx]}")

    print("\nRow then column order matters:")
    print("- grid[2, 0] =", grid[2, 0], "(third row, first column)")
    print("- grid[0, 2] =", grid[0, 2], "(first row, third column)")


def key_takeaways():
    """Print final summary points for the milestone."""
    section_header("Milestone Summary")
    print("1. Always inspect shape before indexing")
    print("2. ndim tells how many axes the array has")
    print("3. 2D indexing format is [row, column]")
    print("4. NumPy indexing is zero-based")
    print("5. Shape awareness helps prevent index-related bugs")


def run_milestone_demo():
    """Run the complete milestone demonstration."""
    understand_shape()
    understand_dimensions()
    access_by_index_positions()
    visualize_layout()
    key_takeaways()


if __name__ == "__main__":
    run_milestone_demo()
