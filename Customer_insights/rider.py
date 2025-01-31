import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'D:/ZeptoAnalysis/Customer_insights/UPDATED_DATASET.CSV'
data = pd.read_csv(file_path)

# Create a count plot for Delivery_Time_mins
plt.figure(figsize=(10, 6))
ax = sns.countplot(x='Delivery_Time_mins', data=data)
plt.title('Count Plot for Delivery Time (in minutes)')
plt.xlabel('Delivery Time (minutes)')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Add counts on top of the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Save the plot
#plt.savefig('delivery_time_count_plot.png')


# Add counts on top of the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')
# Show the plot
plt.show()

# Analyze rider performance based on delivery time
average_delivery_time = data['Delivery_Time_mins'].mean()
print(f'Average Delivery Time: {average_delivery_time:.2f} minutes')

# Identify riders with delivery times significantly above average
high_delivery_times = data[data['Delivery_Time_mins'] > average_delivery_time]
print(f'Number of deliveries with high delivery times: {len(high_delivery_times)}')

# Suggest incentives for riders with delivery times below average
low_delivery_times = data[data['Delivery_Time_mins'] <= average_delivery_time]
print(f'Number of deliveries with low delivery times: {len(low_delivery_times)}')

# Plot the distribution of delivery times
plt.figure(figsize=(10, 6))
sns.histplot(data['Delivery_Time_mins'], kde=True)
plt.title('Distribution of Delivery Times')
plt.xlabel('Delivery Time (minutes)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Save the plot
# plt.savefig('delivery_time_distribution.png')
# Identify riders with delivery times less than 10 minutes
fast_deliveries = data[data['Delivery_Time_mins'] < 10]
print(f'Number of deliveries with delivery times less than 10 minutes: {len(fast_deliveries)}')

# Suggest incentives for these riders
riders_with_incentives = fast_deliveries['Rider_ID'].unique()
print(f'Riders eligible for incentives: {riders_with_incentives}')
# Assign assumed Rider IDs to the fast deliveries
fast_deliveries['Assumed_Rider_ID'] = range(1, len(fast_deliveries) + 1)

# Print the assumed Rider IDs
print(f'Assumed Rider IDs for fast deliveries: {fast_deliveries["Assumed_Rider_ID"].tolist()}')

# Save the fast deliveries with assumed Rider IDs to a new CSV file
#fast_deliveries.to_csv('D:/ZeptoAnalysis/Customer_insights/fast_deliveries_with_assumed_rider_ids.csv', index=False)
# Create a DataFrame for good riders who are doing delivery within 10 minutes
good_riders = fast_deliveries[['Rider_ID', 'Delivery_Time_mins']]

# Print the DataFrame of good riders
print("DataFrame of good riders (delivery within 10 minutes):")
print(good_riders)

# Save the DataFrame of good riders to a new CSV file
#good_riders.to_csv('D:/ZeptoAnalysis/Customer_insights/good_riders.csv', index=False)