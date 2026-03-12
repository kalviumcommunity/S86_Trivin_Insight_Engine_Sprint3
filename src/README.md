# Source Code Directory

This directory contains reusable Python scripts and modules.

## Structure

### Fundamentals Modules
Core Python learning scripts for milestone demonstrations:
- `data_types_fundamentals.py` - Numeric and string data types
- `collections_fundamentals.py` - Lists, tuples, and dictionaries
- `loops_fundamentals.py` - For/while loops, break, and continue
- `functions_fundamentals.py` - Defining and calling functions, arguments, and scope
- `readability_pep8_basics.py` - Readable variable names and useful comments (PEP 8 basics)
- `code_structure_fundamentals.py` - Structuring code for readability and reuse (LU 4.21)

### NumPy Fundamentals Modules
NumPy array learning scripts:
- `numpy_shape_dimensions_indexing.py` - Array shape, dimensions, and index positions
- `numpy_arrays_fundamentals.py` - Creating NumPy arrays, array properties, basic operations (LU 4.20)
- `numpy_math_operations.py` - Mathematical operations on NumPy arrays (LU 4.21)

### Pandas Fundamentals Modules
Pandas learning scripts:
- `pandas_series_from_lists_arrays.py` - Creating Pandas Series from lists and NumPy arrays (LU 4.22)
- `pandas_dataframe_indexing_slicing.py` - Selecting DataFrame rows and columns using indexing and slicing
- `pandas_csv_loading_fundamentals.py` - Loading CSV data into Pandas DataFrames, then inspecting and verifying structure
- `missing_values_detection_demo.py` - Detecting and analyzing missing values in DataFrames; includes comprehensive detection workflow
- `distribution_comparison_demo.py` - Comparing distributions across multiple numeric columns using summary statistics only
- `column_name_standardization_demo.py` - Standardizing column names and data formats; snake_case convention, text normalization
- `data_standardization_complete_workflow.py` - Complete workflow: standardization, duplicates removal, summary statistics
- `duplicate_records_handling_demo.py` - Identifying exact and partial duplicates, removing duplicates intentionally, and verifying deduplication results
- `dataframe_inspection_demo.py` - Inspecting DataFrames using head(), info(), and describe()
- `line_plot_trends_demo.py` - Identifying trends over time with line plots; sorting dates, smoothing noise, and spotting spikes or drops

### Reference Files
Quick reference guides to keep open while coding:
- `code_structure_reference.py` - Quick reference for code structure best practices

### Video Demo Scripts
Short scripts for screen-record walkthrough submissions:
- `video_demo_loops.py` - ~2-minute loop walkthrough
- `video_demo_functions.py` - ~2-minute functions walkthrough
- `video_demo_readability.py` - ~2-minute readability and naming walkthrough
- `video_demo_code_structure.py` - ~2-minute code structure walkthrough (LU 4.21)
- `missing_values_detection_demo.py` - ~2-minute missing value detection demonstration (comprehensive with all key concepts)
- `column_name_standardization_demo.py` - ~2-minute column standardization and data format demonstration

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
