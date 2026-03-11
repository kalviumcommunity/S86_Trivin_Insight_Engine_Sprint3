# Notebooks Directory

This directory contains Jupyter notebooks for data exploration, analysis, and visualization.

## Notebook Naming Convention
Use numbered prefixes to indicate workflow order:
- `01_data_processing_demo.ipynb` - Data processing and workflow demonstration
- `02_data_types_fundamentals.ipynb` - Python data types basics
- `03_python_collections.ipynb` - Lists, dictionaries, tuples, and sets
- `04_iteration_loops.ipynb` - For loops, while loops, and loop control
- `05_passing_data_and_returning_results.ipynb` - Functions: parameters, arguments, return statements
- `06_numpy_arrays.ipynb` - NumPy arrays fundamentals
- `07_numpy_math_operations.ipynb` - NumPy mathematical operations
- `08_pandas_series_from_lists_arrays.ipynb` - Pandas Series from lists and arrays
- `10_inspecting_dataframes.ipynb` - Inspecting DataFrames using head(), info(), and describe()
- `11_csv_loading_into_dataframes.ipynb` - Loading CSV files into Pandas DataFrames and inspecting structure
- `12_detecting_missing_values.ipynb` - Detecting and analyzing missing values in DataFrames
- `13_handling_missing_values.ipynb` - Handling missing values with appropriate strategies
- `14_identifying_removing_duplicates.ipynb` - Identifying and removing duplicate records in DataFrames
- `15_comparing_distributions_multiple_columns.ipynb` - Comparing distributions across multiple numeric columns using summary statistics

## Learning Notebooks

### Python Fundamentals
- **Jupyter_Basics.ipynb** - Introduction to Jupyter notebooks
- **02_data_types_fundamentals.ipynb** - Numeric types, strings, type conversion
- **03_python_collections.ipynb** - Working with collections
- **04_iteration_loops.ipynb** - For loops, while loops, break, and continue
- **05_passing_data_and_returning_results.ipynb** - **Milestone 4.19** Data flow in functions: passing parameters and returning results

### NumPy Fundamentals
- **06_numpy_arrays.ipynb** - **Milestone 4.20** Creating NumPy arrays from Python lists, array properties, basic operations
- **07_numpy_math_operations.ipynb** - **Milestone 4.21** Performing basic mathematical operations on NumPy arrays

### Pandas Fundamentals
- **08_pandas_series_from_lists_arrays.ipynb** - **Milestone 4.22** Creating Pandas Series from lists and NumPy arrays; understanding index and values
- **10_inspecting_dataframes.ipynb** - Inspecting DataFrame structure with head(), info(), describe()
- **11_csv_loading_into_dataframes.ipynb** - **CSV Loading Milestone** Loading CSV data with `pd.read_csv`, inspecting headers, columns, and row counts
- **12_detecting_missing_values.ipynb** - **Missing Values Detection Milestone** Detecting, counting, and analyzing missing values in DataFrames; understanding data quality issues
- **14_identifying_removing_duplicates.ipynb** - **Duplicate Records Milestone** Detecting duplicates, applying `drop_duplicates`, and verifying data integrity after cleanup
- **15_comparing_distributions_multiple_columns.ipynb** - **Distribution Comparison Milestone** Comparing means, medians, ranges, and standard deviations across multiple numeric columns

### Data Workflow
- **01_data_processing_demo.ipynb** - Complete data lifecycle demonstration

## Best Practices
1. Keep notebooks focused on specific tasks
2. Add markdown cells to explain your analysis
3. Clear all outputs before committing (if using git)
4. Use relative paths to reference data: `../data/raw/`
5. Save generated figures to `../outputs/figures/`
6. Restart kernel and run all cells before finalizing
