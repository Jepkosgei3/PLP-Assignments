# Data Analysis with Pandas and Matplotlib

## Project Description
This project demonstrates basic data analysis and visualization techniques using Python's pandas and matplotlib libraries. The analysis is performed on the classic Iris dataset, covering data loading, exploration, cleaning, statistical analysis, and visualization.

## Features
- Data loading and inspection
- Missing value detection and handling
- Statistical analysis (mean, median, standard deviation)
- Data grouping and aggregation
- Four types of visualizations:
  - Line chart
  - Bar chart
  - Histogram
  - Scatter plot

## Installation
1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the analysis script:
```bash
python data-analytics.py
```

Or open in Jupyter Notebook:
```bash
jupyter notebook
```

## File Structure
- `data-analytics.py`: Main analysis script
- `requirements.txt`: Python dependencies
- `iris_analysis.png`: Output visualization (generated after running)
- `README.md`: This documentation file

## Results
After running the script, you'll get:
1. Console output showing:
   - First 5 rows of data
   - Dataset structure information
   - Missing value counts
   - Statistical summaries
2. Visualization file (`iris_analysis.png`) containing four plots

## Customization
To analyze your own dataset:
1. Replace the data loading code in `data-analytics.py`
2. Adjust column names in the analysis and visualization code
3. Update the visualization titles and labels accordingly
