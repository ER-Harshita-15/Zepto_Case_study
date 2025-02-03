# Data Handling Scripts

This repository contains two Python scripts for data preprocessing and data wrangling. These scripts are essential for preparing the dataset for further analysis and modeling.

## Scripts

### 1. `data_preprocessing.py`

This script is used to preprocess the data. It performs the following tasks:
- Loads the data from a CSV file.
- Identifies the data types of the columns.
- Encodes the categorical columns.
- Calculates the correlation of the columns with the target column (`Cart_Abandonment_Flag`) and prints the correlation values.

#### Usage
To run the script, execute the following command:
```bash
python data_preprocessing.py
```

#### Key Functions
- `load_data()`: Loads the dataset from the specified file path.
- `identify_datatypes()`: Identifies and returns the list of object, integer, and float columns.
- `encode_categorical_columns()`: Encodes the categorical columns using category codes.
- `calculate_correlations()`: Calculates and returns the correlation of columns with the target column.
- `run()`: Executes the entire preprocessing pipeline and prints the results.

### 2. `data_wrangling.py`

This script is used to load the dataset and preprocess it. It performs feature engineering and data cleaning tasks such as:
- Converting `Order_Time` to datetime format.
- Removing duplicate entries.
- Creating new features like `Cart_Abandonment_Flag`, `Total_Purchase_Value`, `Lifetime_Value`, `Competitor_Price`, `Ad_Click_Through_Rate`, `Browsing_Time_mins`, `Voice_Search_Count`, `Visual_Search_Count`, `Age_Group`, `Loyalty_Tier`, `Discount_Percentage`, and `High_Spender_Flag`.

#### Usage
To run the script, execute the following command:
```bash
python data_wrangling.py
```

#### Key Functions
- `load_data()`: Loads the dataset from the specified file path.
- `preprocess_data()`: Performs data cleaning and feature engineering.
- `run()`: Executes the entire data wrangling pipeline and prints the results.

## File Paths
- The `data_preprocessing.py` script expects the dataset at `..\\Data\\updated_dataset.csv`.
- The `data_wrangling.py` script expects the dataset at `..\\Data\\Zepto_Analytics_Dataset.csv`.

Ensure that the datasets are available at the specified paths before running the scripts.

## Requirements
- Python 3.12.6
- pandas
- numpy

Install the required packages using:
```bash
pip install pandas numpy
```