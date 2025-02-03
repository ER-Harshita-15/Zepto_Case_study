"""
This script is used to analyze the sales data of a product inventory 
and generate insights on the top-selling product categories by city and time.
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class ProductSalesAnalysis:
    def __init__(self, dataset_path, plot_dir='plots'):
        # Load the dataset
        self.df = pd.read_csv(dataset_path)
        self.df['Order_Time'] = pd.to_datetime(self.df['Order_Time'])
        self.df['Order_Month'] = self.df['Order_Time'].dt.to_period('M')
        
        # Create the plot directory if it doesn't exist
        self.plot_dir = plot_dir
        if not os.path.exists(self.plot_dir):
            os.makedirs(self.plot_dir)

    def top_selling_categories_by_city_and_time(self):
        # Group by City, Product_Category, and Order_Time
        grouped = self.df.groupby(['City', 'Product_Category', 'Order_Time']).agg({'Quantity': 'sum'}).reset_index()
        
        # Sort by Quantity in descending order
        grouped = grouped.sort_values(by='Quantity', ascending=False)
        
        # Get the top-selling categories
        top_selling = grouped.groupby(['City', 'Order_Time']).first().reset_index()
        
        return top_selling

    def top_selling_categories_by_city_and_month(self):
        # Group by City, Product_Category, and Order_Month
        grouped = self.df.groupby(['City', 'Product_Category', 'Order_Month']).agg({'Quantity': 'sum'}).reset_index()
        
        # Sort by Quantity in descending order
        grouped = grouped.sort_values(by='Quantity', ascending=False)
        
        # Get the top-selling categories
        top_selling = grouped.groupby(['City', 'Order_Month']).first().reset_index()
        
        return top_selling

    def plot_top_selling_categories(self):
        # Get the top-selling product categories by city and month
        top_selling_categories_monthly = self.top_selling_categories_by_city_and_month()

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
            
            # Save the plot
            plot_filename = f'{self.plot_dir}/{city}_top_selling_categories.png'
            plt.savefig(plot_filename)
            plt.close()  # Close the plot to avoid overlap in the next iteration

    def plot_category_wise_selling(self):
        # Group by City, Product_Category, and Order_Month for category-wise selling
        category_sales = self.df.groupby(['City', 'Product_Category', 'Order_Month']).agg({'Quantity': 'sum'}).reset_index()
        
        # Plot the results
        sns.set(style="whitegrid")

        # Plot for each city
        cities = category_sales['City'].unique()
        for city in cities:
            city_data = category_sales[category_sales['City'] == city]
            plt.figure(figsize=(12, 6))
            sns.barplot(x='Order_Month', y='Quantity', hue='Product_Category', data=city_data)
            plt.title(f'Category-Wise Selling in {city} by Month')
            plt.xlabel('Month')
            plt.ylabel('Quantity Sold')
            plt.legend(title='Product Category')
            plt.xticks(rotation=45)
            
            # Save the plot
            plot_filename = f'{self.plot_dir}/{city}_category_wise_selling.png'
            plt.savefig(plot_filename)
            plt.close()  # Close the plot to avoid overlap in the next iteration

# Usage
dataset_path = '..\\Data\\updated_dataset.csv'  # Replace with your dataset path
analysis = ProductSalesAnalysis(dataset_path)

# Get and display the top-selling product categories by city and time
top_selling_categories = analysis.top_selling_categories_by_city_and_time()
print(top_selling_categories)

# Plot the top-selling product categories by city and month and save the plots
analysis.plot_top_selling_categories()

# Plot category-wise sales for each city and save the plots
analysis.plot_category_wise_selling()
