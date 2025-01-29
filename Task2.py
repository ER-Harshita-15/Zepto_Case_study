import pandas as pd
import numpy as np
from datetime import datetime

# Load the dataset
df = pd.read_csv('updated_dataset.csv')

# Convert 'Order_Time' to datetime
df['Order_Time'] = pd.to_datetime(df['Order_Time'])

# Feature engineering: Extract useful time-based features
df['Day_of_Week'] = df['Order_Time'].dt.dayofweek  # 0 = Monday, 6 = Sunday


# Display the dataframe with new features
print(df[['Customer_ID', 'Order_Time', 'Day_of_Week']].head())


import matplotlib.pyplot as plt

# Distribution of Delivery Time
plt.hist(df['Delivery_Time_mins'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Delivery Time (Minutes)')
plt.xlabel('Delivery Time (Minutes)')
plt.ylabel('Frequency')
plt.show()

# Average Delivery Time per Product Category
avg_delivery_by_category = df.groupby('Product_Category')['Delivery_Time_mins'].mean()
print(avg_delivery_by_category)

# Plot Average Delivery Time per Product Category
avg_delivery_by_category.plot(kind='bar', color='orange', title="Average Delivery Time by Product Category")
plt.xlabel('Product Category')
plt.ylabel('Average Delivery Time (Minutes)')
plt.show()


from sklearn.cluster import KMeans

# We will cluster based on Product Category frequency for customer segmentation
product_category_counts = df.groupby('Customer_ID')['Product_Category'].nunique()

# KMeans clustering to identify customer groups based on Product Categories
kmeans = KMeans(n_clusters=3)  # Assume 3 clusters for segmentation, adjust as necessary
df['Customer_Cluster'] = kmeans.fit_predict(product_category_counts.values.reshape(-1, 1))

# Show the cluster assignments for customers
print(df[['Customer_ID', 'Customer_Cluster']].drop_duplicates())


# Group by day of the week to identify patterns in delivery time
avg_delivery_by_day = df.groupby('Day_of_Week')['Delivery_Time_mins'].mean()

# Plot Average Delivery Time by Day of Week
avg_delivery_by_day.plot(kind='line', color='green', title="Average Delivery Time by Day of Week")
plt.xlabel('Day of Week')
plt.ylabel('Average Delivery Time (Minutes)')
plt.show()

# Check if any days have significantly higher delivery times
high_delivery_days = avg_delivery_by_day[avg_delivery_by_day > avg_delivery_by_day.mean()]
print(high_delivery_days)


# Average Delivery Time by Loyalty Tier
avg_delivery_by_loyalty = df.groupby('Loyalty_Tier')['Delivery_Time_mins'].mean()

# Plot Average Delivery Time by Loyalty Tier
avg_delivery_by_loyalty.plot(kind='bar', color='purple', title="Average Delivery Time by Loyalty Tier")
plt.xlabel('Loyalty Tier')
plt.ylabel('Average Delivery Time (Minutes)')
plt.show()
""""yeh bss analysis part hua iska description and insights mai likh dungi ok but the main thing is approach to handle it :
yeh kaam aapko krna hoga kyunki usme googlemap ka api wagera b lagega so we nee d to discuss it even i will share the chat gpt chat with u  """

