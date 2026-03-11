"""
Visualizing Data Distributions Using Histograms (Non-Interactive)
==================================================================

This script generates all histogram visualizations and saves them to disk
without displaying interactive plots. Useful for automated execution.

Author: Trivin Insight Engine
Date: March 11, 2026
"""

from pathlib import Path

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_CSV_PATH = PROJECT_ROOT / "data" / "processed" / "employee_survey_cleaned_2026_Q1.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures"


def setup():
    """Setup environment and ensure output directory exists."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 11
    print("✅ Setup complete")


def load_data():
    """Load the employee survey dataset."""
    print(f"\n📊 Loading data from: {PROCESSED_CSV_PATH}")
    df = pd.read_csv(PROCESSED_CSV_PATH)
    print(f"✅ Loaded {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def create_basic_histogram(df):
    """Create basic histogram for satisfaction_score."""
    print("\n1️⃣  Creating basic histogram...")
    
    plt.figure(figsize=(10, 6))
    plt.hist(df['satisfaction_score'], bins=10, color='steelblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Satisfaction Score', fontsize=12, fontweight='bold')
    plt.ylabel('Frequency', fontsize=12, fontweight='bold')
    plt.title('Distribution of Employee Satisfaction Scores', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    output_path = OUTPUT_DIR / 'satisfaction_score_histogram.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_path.name}")


def create_histogram_with_stats(df):
    """Create histogram with mean and median lines."""
    print("\n2️⃣  Creating histogram with statistical reference lines...")
    
    mean_val = df['work_life_balance'].mean()
    median_val = df['work_life_balance'].median()
    
    plt.figure(figsize=(10, 6))
    plt.hist(df['work_life_balance'], bins=10, color='seagreen', edgecolor='black', alpha=0.7)
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
    plt.axvline(median_val, color='orange', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
    
    plt.xlabel('Work-Life Balance Score', fontsize=12, fontweight='bold')
    plt.ylabel('Frequency', fontsize=12, fontweight='bold')
    plt.title('Distribution of Work-Life Balance Scores', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    output_path = OUTPUT_DIR / 'work_life_balance_histogram_with_stats.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_path.name}")


def create_comparison_grid(df):
    """Create comparison grid for multiple columns."""
    print("\n3️⃣  Creating comparison grid...")
    
    numeric_columns = ['satisfaction_score', 'work_life_balance', 'management_support', 
                       'career_growth', 'team_collaboration']
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Comparing Distributions Across Survey Metrics', fontsize=16, fontweight='bold', y=0.995)
    
    axes = axes.flatten()
    colors = ['steelblue', 'seagreen', 'coral', 'mediumpurple', 'gold']
    
    for idx, column in enumerate(numeric_columns):
        ax = axes[idx]
        ax.hist(df[column], bins=10, color=colors[idx], edgecolor='black', alpha=0.7)
        ax.set_xlabel(column.replace('_', ' ').title(), fontsize=10, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=10)
        ax.grid(axis='y', alpha=0.3)
        
        mean_val = df[column].mean()
        ax.axvline(mean_val, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
        ax.text(mean_val, ax.get_ylim()[1] * 0.9, f'μ={mean_val:.1f}', 
                color='red', fontsize=9, ha='center', 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    
    axes[5].axis('off')
    plt.tight_layout()
    
    output_path = OUTPUT_DIR / 'histogram_comparison_grid.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_path.name}")


def create_bin_comparison(df):
    """Compare different bin sizes."""
    print("\n4️⃣  Creating bin size comparison...")
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Effect of Bin Size on Histogram Interpretation', fontsize=14, fontweight='bold')
    
    bin_sizes = [5, 10, 20]
    titles = ['5 Bins (Coarse)', '10 Bins (Moderate)', '20 Bins (Fine)']
    
    for idx, (bins, title) in enumerate(zip(bin_sizes, titles)):
        ax = axes[idx]
        ax.hist(df['satisfaction_score'], bins=bins, color='steelblue', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Satisfaction Score', fontsize=10)
        ax.set_ylabel('Frequency', fontsize=10)
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    
    output_path = OUTPUT_DIR / 'bin_size_comparison.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_path.name}")


def create_outlier_detection(df):
    """Create histogram highlighting potential outliers."""
    print("\n5️⃣  Creating outlier detection visualization...")
    
    column = 'avg_engagement'
    
    fig, ax = plt.subplots(figsize=(12, 6))
    n, bins, patches = ax.hist(df[column], bins=15, color='lightblue', edgecolor='black', alpha=0.7)
    
    threshold = 0.05 * n.max()
    for patch, freq in zip(patches, n):
        if freq < threshold and freq > 0:
            patch.set_facecolor('red')
            patch.set_alpha(0.8)
    
    ax.set_xlabel(column.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title(f'Distribution of {column.replace("_", " ").title()} with Outlier Highlighting', 
                fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='lightblue', edgecolor='black', label='Normal frequency'),
        Patch(facecolor='red', edgecolor='black', label='Potential outlier region')
    ]
    ax.legend(handles=legend_elements)
    
    plt.tight_layout()
    
    output_path = OUTPUT_DIR / f'{column}_outlier_detection.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_path.name}")


def create_comprehensive_analysis(df):
    """Create comprehensive distribution analysis."""
    print("\n6️⃣  Creating comprehensive distribution analysis...")
    
    column = 'career_growth'
    
    stats = df[column].describe()
    mean_val = df[column].mean()
    median_val = df[column].median()
    mode_val = df[column].mode()[0] if not df[column].mode().empty else None
    skew = df[column].skew()
    
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.hist(df[column], bins=10, color='coral', edgecolor='black', alpha=0.7)
    
    ax.set_xlabel(column.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title(f'Complete Distribution Analysis: {column.replace("_", " ").title()}', 
                fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
    ax.axvline(median_val, color='orange', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
    ax.legend(loc='upper left')
    
    shape = 'Right-skewed' if skew > 0.25 else 'Left-skewed' if skew < -0.25 else 'Roughly symmetric'
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
    
    output_path = OUTPUT_DIR / f'{column}_comprehensive_analysis.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_path.name}")


def print_summary():
    """Print summary of generated files."""
    print("\n" + "=" * 70)
    print("  🎉 ALL HISTOGRAMS GENERATED SUCCESSFULLY!")
    print("=" * 70)
    print(f"\n📁 Output directory: {OUTPUT_DIR}")
    print("\n📊 Generated visualizations:")
    print("   1. satisfaction_score_histogram.png")
    print("   2. work_life_balance_histogram_with_stats.png")
    print("   3. histogram_comparison_grid.png")
    print("   4. bin_size_comparison.png")
    print("   5. avg_engagement_outlier_detection.png")
    print("   6. career_growth_comprehensive_analysis.png")
    print("\n✅ Milestone complete! Review the figures and prepare your video.")
    print("=" * 70)


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print("  HISTOGRAM VISUALIZATION - AUTOMATED GENERATION")
    print("  Trivin Insight Engine")
    print("=" * 70)
    
    setup()
    df = load_data()
    
    create_basic_histogram(df)
    create_histogram_with_stats(df)
    create_comparison_grid(df)
    create_bin_comparison(df)
    create_outlier_detection(df)
    create_comprehensive_analysis(df)
    
    print_summary()


if __name__ == "__main__":
    main()
