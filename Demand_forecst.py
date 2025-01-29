
import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv('Zepto_Analytics_Dataset.csv')

# Group by 'Order_Time' and sum the 'Quantity'
daily_sales = dataset.groupby('Order_Time').sum()['Quantity']


# Prepare data for Prophet (Sales data)
sales = pd.DataFrame({'ds': daily_sales.index, 'y': daily_sales.values})

# Create and fit the model on the entire dataset (initial fit)
model = Prophet()
model.fit(sales)

# Forecast future sales (next 30 days)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Split the dataset into train and test sets (e.g., using the last 30 days as test data)
train = sales[:-30]
test = sales[-30:]

# Create a new Prophet model instance for fitting (new instance)
model = Prophet()

# Fit the model on the training data
model.fit(train)

# Make predictions on the test set
forecast_test = model.predict(test)

# Extract actual and predicted values from the test set
y_true = test['y'].values
y_pred = forecast_test['yhat'].values

# Calculate MAE and RMSE
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))

# Print MAE and RMSE
print(f'MAE: {mae}')
print(f'RMSE: {rmse}')

# Plot the actual vs predicted sales on a line plot
plt.figure(figsize=(10,6))
plt.plot(test['ds'], y_true, label='Actual Sales', color='blue', marker='o')
plt.plot(test['ds'], y_pred, label='Predicted Sales', color='red', linestyle='--', marker='x')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Sales Quantity')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

