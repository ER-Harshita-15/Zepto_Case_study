"""
-> This file contains the code to generate insights from the dataset for customer segmentation. The insights include customer segmentation by 
demographics, loyalty points, purchasing behavior, and cart abandonment. 
-> The insights are printed to the console and visualized using bar plots. 
-> The plots are saved in the 'plots' directory. 
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

class CustomerInsights:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.plots_dir = 'plots'
        os.makedirs(self.plots_dir, exist_ok=True)

    def segment_customers(self):
        self.age_groups = self.df.groupby('Age_Group').size()
        self.gender_groups = self.df.groupby('Gender').size()
        self.city_groups = self.df.groupby('City').size()
        self.loyalty_tiers = self.df.groupby('Loyalty_Tier').size()
        self.high_spenders = self.df[self.df['High_Spender_Flag'] == 1].shape[0]
        self.product_categories = self.df.groupby('Product_Category').size()
        self.payment_methods = self.df.groupby('Payment_Method').size()
        self.cart_abandonment = self.df[self.df['Cart_Abandonment_Flag'] == 1].shape[0]
        self.cart_abandonment_by_delivery_time = self.df[self.df['Cart_Abandonment_Flag'] == 1].groupby('Delivery_Time_mins').size()
        self.cart_abandonment_under_10 = self.df[(self.df['Cart_Abandonment_Flag'] == 1) & (self.df['Delivery_Time_mins'] < 10)].shape[0]

    def print_segments(self):
        print("Customer Segmentation by Demographics:")
        print("Age Groups:\n", self.age_groups)
        print("Gender Groups:\n", self.gender_groups)
        print("City Groups:\n", self.city_groups)

        print("\nCustomer Segmentation by Loyalty Points:")
        print("Loyalty Tiers:\n", self.loyalty_tiers)
        print("High Spenders:", self.high_spenders)

        print("\nCustomer Segmentation by Purchasing Behavior:")
        print("Product Categories:\n", self.product_categories)
        print("Payment Methods:\n", self.payment_methods)
        print("Cart Abandonment:", self.cart_abandonment)

        print("\nCart Abandonment for Delivery Time < 10 minutes:", self.cart_abandonment_under_10)
        if self.cart_abandonment_under_10 == 0:
            print("\nNo Cart Abandonment for Delivery Time < 10 minutes")

    def plot_segments(self):
        self._plot_bar(self.age_groups, 'Customer Segmentation by Age Groups', 'Age Group', 'Number of Customers', 'age_groups.png')
        self._plot_bar(self.gender_groups, 'Customer Segmentation by Gender', 'Gender', 'Number of Customers', 'gender_groups.png')
        self._plot_bar(self.city_groups, 'Customer Segmentation by City', 'City', 'Number of Customers', 'city_groups.png')
        self._plot_bar(self.loyalty_tiers, 'Customer Segmentation by Loyalty Tiers', 'Loyalty Tier', 'Number of Customers', 'loyalty_tiers.png')
        self._plot_bar(pd.Series([self.high_spenders], index=['High Spenders']), 'Number of High Spenders', '', 'Number of Customers', 'high_spenders.png')
        self._plot_bar(self.product_categories, 'Customer Segmentation by Product Categories', 'Product Category', 'Number of Customers', 'product_categories.png')
        self._plot_bar(self.payment_methods, 'Customer Segmentation by Payment Methods', 'Payment Method', 'Number of Customers', 'payment_methods.png')
        self._plot_bar(self.cart_abandonment_by_delivery_time, 'Cart Abandonment by Delivery Time', 'Delivery Time (mins)', 'Number of Cart Abandonments', 'cart_abandonment_by_delivery_time.png')
        self._plot_bar(pd.Series([self.cart_abandonment_under_10], index=['< 10 mins']), 'Cart Abandonment for Delivery Time < 10 minutes', '', 'Number of Cart Abandonments', 'cart_abandonment_under_10.png')

    def _plot_bar(self, data, title, xlabel, ylabel, filename):
        plt.figure(figsize=(14, 12))  # Increased the size of the plots
        if isinstance(data, pd.Series):
            data.plot(kind='bar', color='skyblue')
        else:
            plt.bar(data[0], data[1], color='skyblue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(os.path.join(self.plots_dir, filename))
        plt.close()

if __name__ == "__main__":
    insights = CustomerInsights('..\\..\\..\\Data\\updated_dataset.csv')
    insights.segment_customers()
    insights.print_segments()
    insights.plot_segments()