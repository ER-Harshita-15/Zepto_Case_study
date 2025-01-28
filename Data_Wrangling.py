import pandas as pd
dataset=pd.read_csv('Zepto_Analytics_Dataset.csv')
#DATA PREPROCESSING
#print(dataset.head())
#print(dataset.info())

#DATA CLEANING
null_values=dataset.isnull().sum()
#print(null_values)
#print(dataset.dtypes)
dataset['Order_Time']=pd.to_datetime(dataset['Order_Time'])
#print(dataset['Order_Time'].dtypes)
#print(dataset['Order_Time'])
#dataset = dataset.drop_duplicates()
#print(dataset.info())

#DATA TRANSFORMING
dataset['Cart_Abandonment_Flag']=(dataset['Delivery_Time_mins']>10).astype(int)
#print(dataset[['Cart_Abandonment_Flag','Delivery_Time_mins']])
counts=dataset['Cart_Abandonment_Flag'].value_counts()
#print(counts) #we can represent its % ratio also
dataset['Total_Purchase_Value'] = dataset['Price'] * dataset['Quantity']

customer_ltv = dataset.groupby('Customer_ID')['Total_Purchase_Value'].sum().reset_index()
customer_ltv.rename(columns={'Total_Purchase_Value': 'Lifetime_Value'}, inplace=True)
dataset = dataset.merge(customer_ltv, on='Customer_ID', how='left')

import numpy as np
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

dataset.to_csv('updated_dataset.csv', index=False)


print(dataset.head())
print(dataset.info())
