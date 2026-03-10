# Trivin Insight Engine

## Project Overview
A data science project focused on analyzing employee engagement surveys to understand what drives dissatisfaction. This project explores and visualizes survey data to identify common dissatisfaction themes, department-wise trends, and changes over time.

## Problem Statement
A company conducting employee engagement surveys wants to understand what drives dissatisfaction but only has raw survey responses. The goal is to explore and visualize survey data to identify:
- Common dissatisfaction themes
- Department-wise trends
- Changes over time

## Project Structure
```
Trivin_Insight_Engine/
├── data/
│   ├── raw/              # Original, immutable survey data
│   ├── processed/        # Cleaned and transformed data
│   └── external/         # External reference data
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/                  # Source code and scripts
│   ├── data/            # Data processing and cleaning scripts
│   ├── visualization/   # Visualization scripts and utilities
│   └── analysis/        # Analysis scripts
├── outputs/              # Generated outputs (excluded from git)
│   ├── figures/         # Plots, charts, and visualizations
│   ├── reports/         # Analysis reports and summaries
│   └── models/          # Saved models (if applicable)
├── docs/                 # Project documentation
├── tests/               # Unit tests for scripts
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone this repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Place raw survey data in `data/raw/`
2. Run data processing notebooks in `notebooks/`
3. View generated visualizations in `outputs/figures/`
4. Read analysis reports in `outputs/reports/`

### Python Fundamentals Milestones
Run the learning scripts from the project root:

```bash
python src/data_types_fundamentals.py
python src/collections_fundamentals.py
python src/loops_fundamentals.py
python src/functions_fundamentals.py
python src/readability_pep8_basics.py
python src/numpy_shape_dimensions_indexing.py
python src/pandas_series_from_lists_arrays.py
python src/pandas_dataframe_indexing_slicing.py
python src/pandas_csv_loading_fundamentals.py
python src/duplicate_records_handling_demo.py
```

Video walkthrough demo scripts:

```bash
python src/video_demo_loops.py
python src/video_demo_functions.py
python src/video_demo_readability.py
```

## Data Guidelines
- **Never modify files in `data/raw/`** - Keep original data immutable
- Store processed data in `data/processed/`
- All generated outputs go to `outputs/` folder

## Contributing
- Use clear, descriptive variable names
- Document your code and analysis
- Keep notebooks organized and commented
- Update README when adding new features

## Team
Sprint 3 - Trivin

---