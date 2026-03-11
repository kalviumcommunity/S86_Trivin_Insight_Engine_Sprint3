"""
Visualizing Data Distributions Using Histograms
================================================

This script demonstrates how to create and interpret histograms for
exploratory data analysis (EDA) of numeric data distributions.

Histograms reveal patterns that summary statistics alone cannot show.

Author: Trivin Insight Engine
Date: March 11, 2026
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_CSV_PATH = PROJECT_ROOT / "data" / "processed" / "employee_survey_cleaned_2026_Q1.csv"


def section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def configure_plotting():
    """Set up matplotlib default styling for better-looking plots."""
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 11
    print("✅ Plotting configuration complete")


def load_dataset(csv_path):
    """Load the employee survey dataset."""
    section_header("1. Loading the Dataset")

    print(f"Reading: {csv_path}")

    if not csv_path.exists():
        print("CSV file not found. Check the project path and try again.")
        return None

    df = pd.read_csv(csv_path)
    print(f"Loaded shape: {df.shape}")
    print("\nColumns:")
    print(df.columns.tolist())
    
    print("\nFirst 3 rows:")
    print(df.head(3))
    
    return df


def understand_histograms():
    """Explain what histograms are and what they show."""
    section_header("2. Understanding Histograms")

    print("""
What is a Histogram?
--------------------
A histogram is a visual representation of the distribution of numeric data.

Key Concepts:
  • Bins: Ranges that group values together (e.g., 0-1, 1-2, 2-3)
  • Frequency: How many values fall into each bin
  • Distribution Shape: The overall pattern of the data

Histogram vs. Bar Chart:
  • Histogram: Shows distribution of CONTINUOUS NUMERIC data
  • Bar Chart: Shows counts or comparisons of CATEGORICAL data

What Histograms Reveal:
  1. Central tendency: Where most values cluster
  2. Spread: How wide the distribution is
  3. Shape: Normal, skewed, uniform, multi-modal
  4. Outliers: Unusual values far from the rest

Common Distribution Shapes:
  • Normal (Bell-Shaped): Symmetric, most values in the middle
  • Right-Skewed: Long tail on the right, most values on the left
  • Left-Skewed: Long tail on the left, most values on the right
  • Uniform: Values spread evenly
  • Bimodal: Two distinct peaks
    """)


def create_single_histogram(df, column='satisfaction_score'):
    """Create a histogram for a single numeric column."""
    section_header(f"3. Creating a Histogram for '{column}'")

    # Show basic statistics first
    print(f"\n{column} Statistics:")
    print(df[column].describe())
    print(f"Data type: {df[column].dtype}")

    # Create histogram
    plt.figure(figsize=(10, 6))
    
    plt.hist(df[column], bins=10, color='steelblue', edgecolor='black', alpha=0.7)
    
    plt.xlabel(column.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    plt.ylabel('Frequency (Number of Employees)', fontsize=12, fontweight='bold')
    plt.title(f'Distribution of {column.replace("_", " ").title()}', 
              fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / 'outputs' / 'figures' / f'{column}_histogram.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\n✅ Histogram created and saved")
    print("\nInterpretation Questions:")
    print("  1. Where are most values located? (low, middle, or high scores)")
    print("  2. Is the distribution symmetric or skewed?")
    print("  3. Are there any gaps or unusual patterns?")
    print("  4. Do you see any potential outliers?")


def create_histogram_with_statistics(df, column='work_life_balance'):
    """Create a histogram with mean and median reference lines."""
    section_header(f"4. Histogram with Statistical Reference Lines: '{column}'")

    # Calculate statistics
    mean_val = df[column].mean()
    median_val = df[column].median()
    
    print(f"\n{column} Key Statistics:")
    print(f"  Mean:   {mean_val:.2f}")
    print(f"  Median: {median_val:.2f}")
    print(f"  Difference: {mean_val - median_val:.2f}")
    
    # Interpret skewness
    if mean_val > median_val + 0.25:
        skew_interpretation = "Right-skewed (positive skew) - tail pulls mean higher"
    elif mean_val < median_val - 0.25:
        skew_interpretation = "Left-skewed (negative skew) - tail pulls mean lower"
    else:
        skew_interpretation = "Roughly symmetric - mean and median are close"
    
    print(f"  Shape: {skew_interpretation}")

    # Create histogram
    plt.figure(figsize=(10, 6))
    
    plt.hist(df[column], bins=10, color='seagreen', edgecolor='black', alpha=0.7)
    
    plt.xlabel(column.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    plt.ylabel('Frequency', fontsize=12, fontweight='bold')
    plt.title(f'Distribution of {column.replace("_", " ").title()}', 
              fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add mean and median lines
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {mean_val:.2f}')
    plt.axvline(median_val, color='orange', linestyle='--', linewidth=2, 
                label=f'Median: {median_val:.2f}')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / 'outputs' / 'figures' / f'{column}_histogram_with_stats.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Histogram with reference lines created")
    print("\n💡 Interpretation Tip:")
    print("   If mean > median: Likely right-skewed (tail pulls mean higher)")
    print("   If mean < median: Likely left-skewed (tail pulls mean lower)")
    print("   If mean ≈ median: Likely roughly symmetric")


def compare_multiple_histograms(df, numeric_columns):
    """Create a grid of histograms to compare multiple columns."""
    section_header("5. Comparing Multiple Distributions")

    print("\nColumns being compared:")
    for col in numeric_columns:
        print(f"  - {col}")

    # Create grid
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Comparing Distributions Across Survey Metrics', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    axes = axes.flatten()
    colors = ['steelblue', 'seagreen', 'coral', 'mediumpurple', 'gold', 'lightblue']
    
    for idx, column in enumerate(numeric_columns):
        ax = axes[idx]
        
        # Create histogram
        ax.hist(df[column], bins=10, color=colors[idx], edgecolor='black', alpha=0.7)
        
        # Labels
        ax.set_xlabel(column.replace('_', ' ').title(), fontsize=10, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=10)
        ax.grid(axis='y', alpha=0.3)
        
        # Add mean line
        mean_val = df[column].mean()
        ax.axvline(mean_val, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
        ax.text(mean_val, ax.get_ylim()[1] * 0.9, f'μ={mean_val:.1f}', 
                color='red', fontsize=9, ha='center', 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    
    # Hide extra subplot
    axes[5].axis('off')
    
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / 'outputs' / 'figures' / 'histogram_comparison_grid.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Comparison grid created")
    print("\nComparison Questions to Consider:")
    print("  1. Which column has the widest spread?")
    print("  2. Which column appears most skewed?")
    print("  3. Which columns have similar distributions?")
    print("  4. Do any columns show unusual patterns?")


def demonstrate_bin_effect(df, column='satisfaction_score'):
    """Show how different bin sizes affect histogram interpretation."""
    section_header("6. Effect of Bin Size on Interpretation")

    print(f"\nComparing bin sizes for: {column}")
    print("\nGuideline:")
    print("  • Too few bins: Might hide important details")
    print("  • Too many bins: Might create too much noise")
    print("  • Recommended: 10-20 bins for most datasets")

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Effect of Bin Size on Histogram Interpretation', 
                 fontsize=14, fontweight='bold')
    
    bin_sizes = [5, 10, 20]
    titles = ['5 Bins (Coarse)', '10 Bins (Moderate)', '20 Bins (Fine)']
    
    for idx, (bins, title) in enumerate(zip(bin_sizes, titles)):
        ax = axes[idx]
        ax.hist(df[column], bins=bins, color='steelblue', edgecolor='black', alpha=0.7)
        ax.set_xlabel(column.replace('_', ' ').title(), fontsize=10)
        ax.set_ylabel('Frequency', fontsize=10)
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / 'outputs' / 'figures' / 'bin_size_comparison.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Bin size comparison created")
    print("💡 Notice how different bin sizes reveal or hide patterns")


def detect_outliers_visually(df, column='avg_engagement'):
    """Create a histogram that highlights potential outlier regions."""
    section_header(f"7. Visual Outlier Detection: '{column}'")

    print(f"\nAnalyzing {column} for outliers...")

    plt.figure(figsize=(12, 6))
    
    # Create histogram
    n, bins, patches = plt.hist(df[column], bins=15, color='lightblue', 
                                 edgecolor='black', alpha=0.7)
    
    # Highlight potential outlier bins (frequency < 5% of max frequency)
    threshold = 0.05 * n.max()
    outlier_count = 0
    for i, (patch, freq) in enumerate(zip(patches, n)):
        if freq < threshold and freq > 0:
            patch.set_facecolor('red')
            patch.set_alpha(0.8)
            outlier_count += 1
    
    plt.xlabel(column.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    plt.ylabel('Frequency', fontsize=12, fontweight='bold')
    plt.title(f'Distribution of {column.replace("_", " ").title()} with Outlier Highlighting', 
              fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='lightblue', edgecolor='black', label='Normal frequency'),
        Patch(facecolor='red', edgecolor='black', label='Potential outlier region')
    ]
    plt.legend(handles=legend_elements)
    
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / 'outputs' / 'figures' / f'{column}_outlier_detection.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\n✅ Outlier detection histogram created")
    print(f"📊 Red bars indicate bins with very low frequency (< {threshold:.1f} observations)")
    print("   These may contain outliers worth investigating.")
    print(f"\nBins flagged as potential outlier regions: {outlier_count}")


def comprehensive_distribution_analysis(df, column='career_growth'):
    """Create a comprehensive histogram with full statistical summary."""
    section_header(f"8. Comprehensive Distribution Analysis: '{column}'")

    # Calculate statistics
    stats = df[column].describe()
    mean_val = df[column].mean()
    median_val = df[column].median()
    mode_val = df[column].mode()[0] if not df[column].mode().empty else None
    skew = df[column].skew()
    
    print(f"\nComplete Statistical Summary for {column}:")
    print(f"  Count:     {stats['count']:.0f}")
    print(f"  Mean:      {mean_val:.2f}")
    print(f"  Median:    {median_val:.2f}")
    print(f"  Mode:      {mode_val}")
    print(f"  Std Dev:   {stats['std']:.2f}")
    print(f"  Min:       {stats['min']:.0f}")
    print(f"  Max:       {stats['max']:.0f}")
    print(f"  Range:     {stats['max'] - stats['min']:.0f}")
    print(f"  Skewness:  {skew:.2f}")
    
    shape = 'Right-skewed' if skew > 0.25 else 'Left-skewed' if skew < -0.25 else 'Roughly symmetric'
    print(f"  Shape:     {shape}")

    # Create comprehensive figure
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Histogram
    ax.hist(df[column], bins=10, color='coral', edgecolor='black', alpha=0.7)
    
    ax.set_xlabel(column.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title(f'Complete Distribution Analysis: {column.replace("_", " ").title()}', 
                 fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    # Reference lines
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, 
               label=f'Mean: {mean_val:.2f}')
    ax.axvline(median_val, color='orange', linestyle='--', linewidth=2, 
               label=f'Median: {median_val:.2f}')
    ax.legend(loc='upper left')
    
    # Statistics text box
    stats_text = f"""Summary Statistics:
───────────────────
Count:     {stats['count']:.0f}
Mean:      {mean_val:.2f}
Median:    {median_val:.2f}
Mode:      {mode_val}
Std Dev:   {stats['std']:.2f}
Min:       {stats['min']:.0f}
Max:       {stats['max']:.0f}
Range:     {stats['max'] - stats['min']:.0f}
Skewness:  {skew:.2f}

Shape: {shape}
"""
    
    ax.text(0.98, 0.97, stats_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
            fontfamily='monospace')
    
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / 'outputs' / 'figures' / f'{column}_comprehensive_analysis.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Comprehensive analysis visualization created")


def print_key_takeaways():
    """Print summary of key learnings."""
    section_header("9. Key Takeaways")

    print("""
What You Learned:
─────────────────
  ✅ Histograms visualize distributions of continuous numeric data
  ✅ Bins group values to show frequency patterns
  ✅ Shape matters: Normal, skewed, uniform, bimodal tell different stories
  ✅ Mean vs. Median helps identify skewness
  ✅ Outliers appear as isolated bars in extreme ranges
  ✅ Visual + Statistics = Complete understanding

Best Practices:
───────────────
  • Always label axes clearly
  • Choose appropriate bin sizes (typically 10-20)
  • Use histograms for NUMERIC data only
  • Combine visuals with summary statistics
  • Look for patterns: skew, outliers, gaps, multiple peaks

Common Mistakes to Avoid:
─────────────────────────
  ❌ Using histograms for categorical data (use bar charts instead)
  ❌ Too many or too few bins
  ❌ Forgetting axis labels
  ❌ Overinterpreting noise in small datasets
  ❌ Ignoring outliers visible in the histogram

Remember: Visualization is exploration, not just presentation.
    """)


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print("  HISTOGRAM VISUALIZATION FOR EXPLORATORY DATA ANALYSIS")
    print("  Trivin Insight Engine - Data Distribution Visualization")
    print("=" * 70)

    # Setup
    configure_plotting()

    # Load data
    df = load_dataset(PROCESSED_CSV_PATH)
    if df is None:
        return

    # Educational content
    understand_histograms()

    # Demonstrations
    create_single_histogram(df, column='satisfaction_score')
    
    create_histogram_with_statistics(df, column='work_life_balance')
    
    # Define numeric columns
    numeric_columns = [
        'satisfaction_score',
        'work_life_balance',
        'management_support',
        'career_growth',
        'team_collaboration'
    ]
    
    compare_multiple_histograms(df, numeric_columns)
    
    demonstrate_bin_effect(df, column='satisfaction_score')
    
    detect_outliers_visually(df, column='avg_engagement')
    
    comprehensive_distribution_analysis(df, column='career_growth')
    
    # Summary
    print_key_takeaways()

    print("\n" + "=" * 70)
    print("  MILESTONE COMPLETE!")
    print("  All histograms saved to: outputs/figures/")
    print("=" * 70)
    print("\nNext Steps:")
    print("  1. Review all generated histograms")
    print("  2. Practice interpreting distribution shapes")
    print("  3. Prepare your 2-minute video walkthrough")
    print("  4. Apply histogram analysis to other datasets")


if __name__ == "__main__":
    main()
