"""
This script performs customer insights analysis based on channel-dependent data.
"""
import streamlit as st
import pandas as pd

# Load the dataset
file_path = 'ZEPTO_ANALYTICS_DATASET.CSV'
data = pd.read_csv(file_path)

# Streamlit Title
st.title("Customer Insights Analysis - Channel Dependent")

# Conversion rate from USD to INR (Example rate)
usd_to_inr = 83.0  # Example value, 1 USD = 83 INR

# Streamlit Sidebar: Input Parameters
st.sidebar.header("Input Parameters")

# User Inputs
total_marketing_spend = st.sidebar.number_input("Total Marketing Spend (in USD)", min_value=1, value=100000, step=1000)
unique_visitors = st.sidebar.number_input("Unique Visitors", min_value=1, value=5000, step=100)

# Select High Performing Channels
high_performing_channels = data['Payment_Method'].value_counts().index.tolist()
selected_channels = st.sidebar.multiselect("Select High-Performing Channels", high_performing_channels, default=high_performing_channels)

# Filter data based on selected channels
filtered_data = data[data['Payment_Method'].isin(selected_channels)]

# If no channels are selected, use all channels
if selected_channels:
    st.write(f"Showing results for selected channels: {', '.join(selected_channels)}")
else:
    st.write("Showing results for all channels.")

# Calculate Customer Acquisition Cost (CAC)
new_customers_acquired = filtered_data['Customer_ID'].nunique()
CAC = total_marketing_spend / new_customers_acquired

# Convert CAC to INR
CAC_in_inr = CAC * usd_to_inr

# Calculate conversion rates (using filtered data)
total_purchases = filtered_data.shape[0]
conversion_rate = (total_purchases / unique_visitors) * 100

# Identify high-performing channels for customer acquisition
channel_performance = filtered_data['Payment_Method'].value_counts()

# Refine audience targeting for higher engagement (based on filtered data)
age_groups = pd.cut(filtered_data['Age'], bins=[0, 18, 25, 35, 45, 55, 65, 100], labels=['0-18', '19-25', '26-35', '36-45', '46-55', '56-65', '65+'])
age_group_performance = filtered_data.groupby(age_groups).size().reset_index(name='Count')

# Allocate budgets to maximize ROI based on selected channels
budget_allocation = channel_performance / channel_performance.sum() * total_marketing_spend

# Convert budget allocation to INR
budget_allocation_inr = budget_allocation * usd_to_inr

# Display the results
st.subheader(f"Customer Acquisition Cost (CAC): ₹{CAC_in_inr:.2f}")
st.subheader(f"Conversion Rate: {conversion_rate:.2f}%")

# Display High-Performing Channels for Customer Acquisition
st.subheader("High-Performing Channels for Customer Acquisition")
st.write(channel_performance)

# Display Audience Targeting by Age Group (proper format)
st.subheader("Audience Targeting by Age Group")
st.write(age_group_performance)

# Display Budget Allocation to Maximize ROI
st.subheader("Budget Allocation to Maximize ROI (INR)")
st.write(budget_allocation_inr)
