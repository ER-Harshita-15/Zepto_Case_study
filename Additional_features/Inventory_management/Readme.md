# Inventory Management Analysis

This repository contains scripts and a Jupyter notebook for analyzing product inventory and sales data. The analysis includes calculating demand, optimizing inventory, and performing historical seasonal analysis.

## Files

### 1. `stock_dstock.py`

This script calculates the demand for product categories in a city during a specific quarter and displays the stock percentage for each category.

#### Features:
- Upload a CSV file with columns: `Order_Time`, `City`, `Product_Category`, and `Quantity`.
- Convert `Order_Time` to datetime and map months to quarters.
- Group data by `City`, `Product_Category`, and `Quarter` to calculate the total quantity.
- Filter data based on user-selected city and quarter.
- Calculate and display the stock percentage for each product category.
- Option to download the filtered data as a CSV file.

### 2. `inventory_optimization.py`

This script analyzes the sales data of a product inventory and generates insights on the top-selling product categories by city and time.

#### Features:
- Load the dataset and convert `Order_Time` to datetime.
- Group data by `City`, `Product_Category`, and `Order_Time` or `Order_Month` to calculate the total quantity.
- Identify top-selling product categories by city and time.
- Plot top-selling product categories by city and month.
- Plot category-wise sales for each city.

### 3. `historical_seasonal_analysis.ipynb`

This Jupyter notebook performs historical seasonal analysis on the sales data.

#### Features:
- Load the dataset and set `Order_Time` as the index.
- Group data by month and calculate the total purchase value.
- Plot monthly total purchase value.
- Calculate and plot year-over-year growth.
- Perform seasonal decomposition of the total purchase value.
- Analyze and plot monthly total purchase value by city.
- Identify and plot the best and worst performing months for each city.

## Usage

1. **stock_dstock.py**:
    - Run the script using Streamlit: `streamlit run stock_dstock.py`.
    - Upload the CSV file and select the city and quarter to view the demand and stock percentage.

2. **inventory_optimization.py**:
    - Update the `dataset_path` variable with the path to your dataset.
    - Run the script to generate insights and plots.

3. **historical_seasonal_analysis.ipynb**:
    - Open the notebook in Jupyter or any compatible environment.
    - Execute the cells to perform the analysis and generate plots.

## Requirements

- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib
- statsmodels
- Streamlit (for `stock_dstock.py`)

Install the required packages using:
