import pandas as pd

# Load the dataset
file_path = 'D:/ZeptoAnalysis/Customer_insights/UPDATED_DATASET.CSV'
data = pd.read_csv(file_path)

# Assume the dataset has a column 'Order_Time' in the format 'HH:MM:SS'
data['Order_Hour'] = pd.to_datetime(data['Order_Time']).dt.hour

# Define peak and off-peak hours
peak_hours = list(range(10, 14)) + list(range(18, 23))  # 11 AM to 3 PM and 6 PM to 10 PM
off_peak_hours = list(set(range(24)) - set(peak_hours))  # Remaining hours

# Categorize orders into peak and off-peak
data['Peak_OffPeak'] = data['Order_Hour'].apply(lambda x: 'Peak' if x in peak_hours else 'Off-Peak')

# Calculate the number of orders in peak and off-peak hours
peak_orders = data[data['Peak_OffPeak'] == 'Peak'].shape[0]
off_peak_orders = data[data['Peak_OffPeak'] == 'Off-Peak'].shape[0]

# Print the results
print(f"Number of orders during peak hours: {peak_orders}")
print(f"Number of orders during off-peak hours: {off_peak_orders}")

# Suggest workforce allocation
total_orders = data.shape[0]
peak_percentage = peak_orders / total_orders
off_peak_percentage = off_peak_orders / total_orders

print(f"Suggested workforce allocation:")
print(f"Peak hours: {peak_percentage * 100:.2f}% of the workforce")
print(f"Off-peak hours: {off_peak_percentage * 100:.2f}% of the workforce")
# Create a small sample dataframe
sample_data = pd.DataFrame({
    'Order_Time': ['10:00:00', '12:30:00', '14:45:00', '19:00:00', '19:15:00', '21:30:00', '23:00:00']
})

# Process the sample dataframe
sample_data['Order_Hour'] = pd.to_datetime(sample_data['Order_Time']).dt.hour
sample_data['Peak_OffPeak'] = sample_data['Order_Hour'].apply(lambda x: 'Peak' if x in peak_hours else 'Off-Peak')

# Calculate the number of orders in peak and off-peak hours for the sample dataframe
sample_peak_orders = sample_data[sample_data['Peak_OffPeak'] == 'Peak'].shape[0]
sample_off_peak_orders = sample_data[sample_data['Peak_OffPeak'] == 'Off-Peak'].shape[0]

# Print the results for the sample dataframe
print(f"Sample Data - Number of orders during peak hours: {sample_peak_orders}")
print(f"Sample Data - Number of orders during off-peak hours: {sample_off_peak_orders}")

# Suggest workforce allocation for the sample dataframe
sample_total_orders = sample_data.shape[0]
sample_peak_percentage = sample_peak_orders / sample_total_orders
sample_off_peak_percentage = sample_off_peak_orders / sample_total_orders

print(f"Sample Data - Suggested workforce allocation:")
print(f"Peak hours: {sample_peak_percentage * 100:.2f}% of the workforce")
print(f"Off-peak hours: {sample_off_peak_percentage * 100:.2f}% of the workforce")