import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('updated_dataset.csv')

# Convert delivery time to datetime
data['delivery_time'] = pd.to_datetime(data['delivery_time'])

# Extract hour from delivery time
data['hour'] = data['delivery_time'].dt.hour

# Group by city, product category, and hour
grouped_data = data.groupby(['city', 'product_category', 'hour']).agg({
    'delivery_time': 'mean'
}).reset_index()

# Rename the columns for clarity
grouped_data.rename(columns={'delivery_time': 'average_delivery_time'}, inplace=True)

# Plotting
plt.figure(figsize=(14, 7))
sns.lineplot(data=grouped_data, x='hour', y='average_delivery_time', hue='city', style='product_category')
plt.title('Average Delivery Time by City, Product Category, and Time of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Delivery Time (minutes)')
plt.legend(title='City / Product Category')
plt.show()