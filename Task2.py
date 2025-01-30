import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df['Order_Time'] = pd.to_datetime(df['Order_Time'])
    df['Day_of_Week'] = df['Order_Time'].dt.dayofweek
    return df

def plot_delivery_time_distribution(df, save_path):
    plt.figure(figsize=(14, 10))  # Increased height
    plt.hist(df['Delivery_Time_mins'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Delivery Time (Minutes)')
    plt.xlabel('Delivery Time (Minutes)')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(save_path, 'delivery_time_distribution.png'))
    plt.close()

def plot_avg_delivery_by_category(df, save_path):
    plt.figure(figsize=(14, 14))  # Increased height
    avg_delivery_by_category = df.groupby('Product_Category')['Delivery_Time_mins'].mean()
    avg_delivery_by_category.plot(kind='bar', color='orange', title="Average Delivery Time by Product Category")
    plt.xlabel('Product Category')
    plt.ylabel('Average Delivery Time (Minutes)')
    plt.savefig(os.path.join(save_path, 'avg_delivery_by_category.png'))
    plt.close()

def customer_segmentation(df):
    product_category_counts = df.groupby('Customer_ID')['Product_Category'].nunique()
    kmeans = KMeans(n_clusters=3)
    df['Customer_Cluster'] = kmeans.fit_predict(product_category_counts.values.reshape(-1, 1))
    return df

def plot_avg_delivery_by_day(df, save_path):
    plt.figure(figsize=(14, 10))  # Increased height
    avg_delivery_by_day = df.groupby('Day_of_Week')['Delivery_Time_mins'].mean()
    avg_delivery_by_day.plot(kind='line', color='green', title="Average Delivery Time by Day of Week")
    plt.xlabel('Day of Week')
    plt.ylabel('Average Delivery Time (Minutes)')
    plt.savefig(os.path.join(save_path, 'avg_delivery_by_day.png'))
    plt.close()

def plot_avg_delivery_by_loyalty(df, save_path):
    plt.figure(figsize=(14, 10))  # Increased height
    avg_delivery_by_loyalty = df.groupby('Loyalty_Tier')['Delivery_Time_mins'].mean()
    avg_delivery_by_loyalty.plot(kind='bar', color='purple', title="Average Delivery Time by Loyalty Tier")
    plt.xlabel('Loyalty Tier')
    plt.ylabel('Average Delivery Time (Minutes)')
    plt.savefig(os.path.join(save_path, 'avg_delivery_by_loyalty.png'))
    plt.close()

def main():
    save_path = 'plots'
    os.makedirs(save_path, exist_ok=True)
    df = load_and_preprocess_data('updated_dataset.csv')
    print(df[['Customer_ID', 'Order_Time', 'Day_of_Week']].head())
    plot_delivery_time_distribution(df, save_path)
    plot_avg_delivery_by_category(df, save_path)
    df = customer_segmentation(df)
    print(df[['Customer_ID', 'Customer_Cluster']].drop_duplicates())
    plot_avg_delivery_by_day(df, save_path)
    high_delivery_days = df.groupby('Day_of_Week')['Delivery_Time_mins'].mean()
    print(high_delivery_days[high_delivery_days > high_delivery_days.mean()])
    plot_avg_delivery_by_loyalty(df, save_path)

if __name__ == "__main__":
    main()

