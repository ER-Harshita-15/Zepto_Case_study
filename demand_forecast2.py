import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('updated_dataset.csv')

df['Order_Time'] = pd.to_datetime(df['Order_Time'])
df['Month'] = df['Order_Time'].dt.month
df['Day_of_Week'] = df['Order_Time'].dt.dayofweek
df['Hour'] = df['Order_Time'].dt.hour

product_sales = df.groupby('Product_ID').agg({'Quantity': 'sum', 'Total_Purchase_Value': 'sum'}).reset_index()

df['Rolling_Mean_Quantity'] = df.groupby('Product_ID')['Quantity'].rolling(30).mean().reset_index(level=0, drop=True)

# Convert 'Product_ID' into numeric labels
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Product_ID'] = le.fit_transform(df['Product_ID'])

from sklearn.model_selection import train_test_split
X = df[['Product_ID', 'Price', 'Month', 'Day_of_Week', 'Hour', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Rolling_Mean_Quantity']]
y = df['Quantity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)



import xgboost as xgb
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error, mean_squared_error
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
import numpy as np

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f'MAE: {mae}, RMSE: {rmse}')


# Generate predictions for the test set
y_pred = model.predict(X_test)

# Plotting Actual vs Predicted values
plt.figure(figsize=(12, 6))
plt.plot(y_test.reset_index(drop=True), label='Actual', color='blue', linestyle='-', marker='o')
plt.plot(y_pred, label='Predicted', color='red', linestyle='--', marker='x')

# Customize the plot
plt.title('Actual vs. Predicted Demand (Quantity) Using XGBoost')
plt.xlabel('Test Sample Index')
plt.ylabel('Quantity (Demand)')
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

future_data = pd.DataFrame({
    'Product_ID': [123],
    'Price': [499],
    'Month': [5],
    'Day_of_Week': [3],
    'Hour': [15],
    'Competitor_Price': [400],
    'Ad_Click_Through_Rate': [0.35],
    'Rolling_Mean_Quantity': [20]  # Example for future rolling mean
})
future_demand = model.predict(future_data)
print(f'Predicted Demand: {future_demand}')

"""Inventory Replenishment Strategy
Yeh work bacha hua.. dekho demand_forecst wala file me b yahi sab kaam karne ki koshish kar rahi thi but arima ya prophet se
nhi ho rha mujhse so here is used xgboost for predicting the future sales ... iss wale ko aap evaluate kr lena ok sahi bana h ya nhi 
and then vo wale ko aapko fix karna hoga kyunki unme mae and rsme ki values jayda aarahi h and rememeber vo wala krna b jaruri 
h just because time series analysis wahi show karega ok. 
now here what you have to do is:
Based on predicted demand, create a dynamic replenishment strategy that adjusts stock levels.
Ensure real-time data feeds into the model to make adjustments as needed (e.g., if the predicted demand increases, reorder the product)."""

