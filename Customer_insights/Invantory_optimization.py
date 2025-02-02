import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('updated_dataset.csv')

# Function to identify top-selling product categories by city and time
def top_selling_categories_by_city_and_time(df):
    # Group by City, Product_Category, and Order_Time
    grouped = df.groupby(['City', 'Product_Category', 'Order_Time']).agg({'Quantity': 'sum'}).reset_index()
    
    # Sort by Quantity in descending order
    grouped = grouped.sort_values(by='Quantity', ascending=False)
    
    # Get the top-selling categories
    top_selling = grouped.groupby(['City', 'Order_Time']).first().reset_index()
    
    return top_selling

# Get the top-selling product categories by city and time
top_selling_categories = top_selling_categories_by_city_and_time(df)

# Display the result
print(top_selling_categories)

# ...existing code...
# Convert Order_Time to datetime and extract month
df['Order_Time'] = pd.to_datetime(df['Order_Time'])
df['Order_Month'] = df['Order_Time'].dt.to_period('M')

# Function to identify top-selling product categories by city and month
def top_selling_categories_by_city_and_month(df):
    # Group by City, Product_Category, and Order_Month
    grouped = df.groupby(['City', 'Product_Category', 'Order_Month']).agg({'Quantity': 'sum'}).reset_index()
    
    # Sort by Quantity in descending order
    grouped = grouped.sort_values(by='Quantity', ascending=False)
    
    # Get the top-selling categories
    top_selling = grouped.groupby(['City', 'Order_Month']).first().reset_index()
    
    return top_selling

# Get the top-selling product categories by city and month
top_selling_categories_monthly = top_selling_categories_by_city_and_month(df)

# Plot the results
sns.set(style="whitegrid")

# Plot for each city
cities = top_selling_categories_monthly['City'].unique()
for city in cities:
    city_data = top_selling_categories_monthly[top_selling_categories_monthly['City'] == city]
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Order_Month', y='Quantity', hue='Product_Category', data=city_data)
    plt.title(f'Top-Selling Product Categories in {city} by Month')
    plt.xlabel('Month')
    plt.ylabel('Quantity Sold')
    plt.legend(title='Product Category')
    plt.xticks(rotation=45)
    plt.show()