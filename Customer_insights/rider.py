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

