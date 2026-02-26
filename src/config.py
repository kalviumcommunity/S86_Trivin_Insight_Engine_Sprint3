# Configuration file for Trivin Insight Engine

# Project metadata
PROJECT_NAME = "Trivin Insight Engine"
VERSION = "1.0.0"

# Directory paths (relative to project root)
DATA_RAW_DIR = "data/raw"
DATA_PROCESSED_DIR = "data/processed"
DATA_EXTERNAL_DIR = "data/external"

OUTPUTS_FIGURES_DIR = "outputs/figures"
OUTPUTS_REPORTS_DIR = "outputs/reports"
OUTPUTS_MODELS_DIR = "outputs/models"

NOTEBOOKS_DIR = "notebooks"
SRC_DIR = "src"

# Analysis parameters
RANDOM_STATE = 42  # For reproducibility
TEST_SIZE = 0.2    # For train-test split if needed

# Visualization settings
FIGURE_DPI = 300
FIGURE_FORMAT = "png"
DEFAULT_FIGSIZE = (12, 6)

# Text analysis settings
MIN_WORD_LENGTH = 3
STOP_WORDS_LANGUAGE = "english"

# Date format for reports
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
