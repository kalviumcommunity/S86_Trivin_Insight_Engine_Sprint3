# Data Directory

This directory contains all data files for the Trivin Insight Engine project.

## Structure

### raw/
Contains original, **immutable** survey data files. 
- **NEVER modify files in this folder**
- Store raw survey responses here
- Keep original file names and formats

### processed/
Contains cleaned and transformed data ready for analysis.
- Store processed datasets here
- Output from data cleaning scripts goes here
- Can be regenerated from raw data

### external/
Contains external reference data (if applicable).
- Department mappings
- Industry benchmarks
- Any external datasets used for comparison

## Best Practices
1. Document data sources in this README
2. Keep raw data backed up
3. Use clear, descriptive file names
4. Include date stamps when relevant (e.g., `survey_2026_01.csv`)
