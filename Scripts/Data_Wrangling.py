import pandas as pd
import numpy as np

class DataWrangler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.dataset = None

    def load_data(self):
        self.dataset = pd.read_csv(self.filepath)
        return self.dataset

    def preprocess_data(self):
        dataset = self.dataset
        dataset['Order_Time'] = pd.to_datetime(dataset['Order_Time'])
        dataset = dataset.drop_duplicates()
        dataset['Cart_Abandonment_Flag'] = (dataset['Delivery_Time_mins'] > 10).astype(int)
        dataset['Total_Purchase_Value'] = dataset['Price'] * dataset['Quantity']
        customer_ltv = dataset.groupby('Customer_ID')['Total_Purchase_Value'].sum().reset_index()
        customer_ltv.rename(columns={'Total_Purchase_Value': 'Lifetime_Value'}, inplace=True)
        dataset = dataset.merge(customer_ltv, on='Customer_ID', how='left')
        dataset['Competitor_Price'] = dataset['Price'] + np.random.uniform(-50, 50, size=len(dataset))
        dataset['Ad_Click_Through_Rate'] = np.random.uniform(0.01, 1.0, len(dataset))
        dataset['Browsing_Time_mins'] = np.random.randint(5, 200, size=len(dataset))
        dataset['Voice_Search_Count'] = np.random.randint(0, 20, size=len(dataset))
        dataset['Visual_Search_Count'] = np.random.randint(0, 15, size=len(dataset))
        bins = [18, 25, 40, 60, 70]
        labels = ['18-25', '26-40', '41-60', '61-70']
        dataset['Age_Group'] = pd.cut(dataset['Age'], bins=bins, labels=labels, right=False)
        bins = [0, 100, 500, 1000]
        labels = ['Bronze', 'Silver', 'Gold']
        dataset['Loyalty_Tier'] = pd.cut(dataset['Loyalty_Points_Earned'], bins=bins, labels=labels, right=False)
        dataset['Discount_Percentage'] = (dataset['Discount_Applied'] / dataset['Price']) * 100
        threshold = dataset['Total_Purchase_Value'].mean()
        dataset['High_Spender_Flag'] = (dataset['Total_Purchase_Value'] > threshold).astype(int)
        self.dataset = dataset
        return self.dataset

    def run(self):
        self.load_data()
        print("Data describe :\n",self.dataset.describe())
        print("Null values check :\n",self.dataset.isnull().sum())
        print("Data after Preprocessing :\n")
        self.preprocess_data()
        print(self.dataset.head())
        print(self.dataset.info())

if __name__ == "__main__":
    wrangler = DataWrangler('..\\Data\\Zepto_Analytics_Dataset.csv')
    wrangler.run()
