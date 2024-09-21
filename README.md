# Descriptive Statistics Script with Polars

This project automatically generates csv with the random data each time it runs. Python function are capable of providing descriptive statistics and summary statistics as well as vizualization for the given data.

## Features

- Reads a dataset from a CSV or Excel file.
- Generates summary statistics:
  - Mean
  - Median
  - Standard Deviation
- Produces at least one data visualization (e.g., histogram, boxplot, etc.).
- Continuous Integration/Continuous Deployment (CI/CD) pipeline integrated with a build status badge.

## Visualizations

- **Histogram**:  
  ![Histogram](https://github.com/nogibjj/Javidan_Polars_Descriptive_Statistics_Script/blob/24f87e79e2c07dded14c51a242ad5cecf8fea8ca/data/histogram.png)
  


- **Scatter Plot**:  
  ![ScatterPlot](https://github.com/nogibjj/Javidan_Polars_Descriptive_Statistics_Script/blob/24f87e79e2c07dded14c51a242ad5cecf8fea8ca/data/scatter_plot.png)


## Summary Statistics Report
- [Summary Statistics Report (PDF)](https://github.com/nogibjj/Javidan_Polars_Descriptive_Statistics_Script/blob/24f87e79e2c07dded14c51a242ad5cecf8fea8ca/data/main.pdf)

## Requirements

- Python 3.x
- Polars
- Matplotlib
- pytest (for testing)
- pylint

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nogibjj/Javidan_Polars_Descriptive_Statistics_Script.git
    cd Javidan_MiniProject2
    ```

2. **Install required dependencies**:
    You can install all required packages by running:
    ```bash
    make setup
    ```

3. **Run the script**:
    To run the descriptive statistics script, use the following command:
    ```bash
    python main.py
    ```

## Usage

- Generate the data using generate_csv
- Specify the engine (Polars)
- Modify the script (`main.py`) to specify the path to your CSV or Excel file.
- Modify list of columns that you want visualization of histogram and scatter plot 

The script will automatically compute and display the descriptive statistics, and generate the data visualization.

## Running Tests

The project includes tests to ensure the correctness of the script. To run the tests, use:

```bash
make test
```

## Linting
To ensure code quality, Pylint is used. You can check for linting issues by running:

```bash
make lint
```