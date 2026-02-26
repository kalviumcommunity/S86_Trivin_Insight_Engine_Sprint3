# Source Code Directory

This directory contains reusable Python scripts and modules.

## Structure

### data/
Data processing and cleaning scripts
- `data_loader.py` - Functions to load raw data
- `data_cleaner.py` - Data cleaning utilities
- `preprocessor.py` - Data preprocessing functions

### visualization/
Visualization scripts and utilities
- `plot_utils.py` - Common plotting functions
- `theme_analysis.py` - Theme visualization functions
- `dashboard.py` - Interactive dashboard creation

### analysis/
Analysis scripts
- `sentiment_analyzer.py` - Sentiment analysis functions
- `trend_analyzer.py` - Trend analysis over time
- `department_analyzer.py` - Department-wise analysis

## Best Practices
1. Write modular, reusable functions
2. Include docstrings for all functions
3. Follow PEP 8 style guidelines
4. Create unit tests in `../tests/` directory
5. Import these modules in notebooks for cleaner code
