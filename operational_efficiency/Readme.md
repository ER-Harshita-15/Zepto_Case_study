# Operational Efficiency Scripts

This repository contains two Python scripts designed to enhance operational efficiency by analyzing order distribution and calculating rider incentives. Below is a detailed description of each script and how to use them.

## Scripts Overview

### 1. `peakhour.py`

This script calculates the number of orders during peak and off-peak hours and suggests workforce allocation based on the order distribution.

#### Features:
- Loads order data from a CSV file.
- Categorizes orders into peak and off-peak hours.
- Calculates the number of orders during peak and off-peak hours.
- Suggests workforce allocation based on the order distribution.

#### Usage:
1. Ensure you have a CSV file with order data, including a column `Order_Time` in the format `HH:MM:SS`.
2. Update the `file_path` variable with the path to your CSV file.
3. Run the script to display the results.

#### Example:
```python
file_path = '..\\Data\\updated_dataset.csv'
allocation = WorkforceAllocation(file_path)
allocation.display_results()

# Process a sample dataframe
sample_data = pd.DataFrame({
    'Order_Time': ['10:00:00', '12:30:00', '14:45:00', '19:00:00', '19:15:00', '21:30:00', '23:00:00']
})
WorkforceAllocation.process_sample_data(sample_data)
```

### 2. `riderincentive.py`

This script calculates incentives for riders based on their delivery time.

#### Features:
- Loads delivery data from a CSV file.
- Calculates incentives based on delivery time.
- Applies incentive calculation to each row in the dataset.
- Displays a summary of the incentives.

#### Usage:
1. Ensure you have a CSV file with delivery data, including a column `Delivery_Time_mins`.
2. Update the `file_path` variable with the path to your CSV file.
3. Run the script to apply incentives and display the summary.


## Requirements

- Python 3.12.6
- pandas
