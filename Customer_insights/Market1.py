import pandas as pd

# Load the dataset
file_path = 'ZEPTO_ANALYTICS_DATASET.CSV'
data = pd.read_csv(file_path)

# Calculate Customer Acquisition Cost (CAC)
# Assuming CAC is the total marketing spend divided by the number of new customers acquired
# For simplicity, let's assume a fixed marketing spend for this example
total_marketing_spend = 100000  # Example value
new_customers_acquired = data['Customer_ID'].nunique()
CAC = total_marketing_spend / new_customers_acquired

# Calculate conversion rates
# Assuming conversion rate is the number of purchases divided by the number of unique visitors
# For simplicity, let's assume a fixed number of unique visitors for this example
unique_visitors = 5000  # Example value
total_purchases = data.shape[0]
conversion_rate = (total_purchases / unique_visitors) * 100

# Identify high-performing channels for customer acquisition
# Assuming 'Payment_Method' as a proxy for acquisition channels
channel_performance = data['Payment_Method'].value_counts()

# Refine audience targeting for higher engagement
# Example: Targeting based on age group
age_groups = pd.cut(data['Age'], bins=[0, 18, 25, 35, 45, 55, 65, 100], labels=['0-18', '19-25', '26-35', '36-45', '46-55', '56-65', '65+'])
age_group_performance = data.groupby(age_groups).size()

# Allocate budgets to maximize ROI
# Example: Allocating budget based on channel performance
budget_allocation = channel_performance / channel_performance.sum() * total_marketing_spend

# Print the results
print(f"Customer Acquisition Cost (CAC): ${CAC:.2f}")
print(f"Conversion Rate: {conversion_rate:.2f}%")
print("\nHigh-Performing Channels for Customer Acquisition:")
print(channel_performance)
print("\nAudience Targeting by Age Group:")
print(age_group_performance)
print("\nBudget Allocation to Maximize ROI:")
print(budget_allocation)