import pandas as pd
dataset=pd.read_csv('Zepto_Analytics_Dataset.csv')
daily_sales = dataset.groupby('Order_Time').sum()['Quantity']
from prophet import Prophet
sales = pd.DataFrame({'ds': daily_sales.index, 'y': daily_sales.values})
model = Prophet()
model.fit(sales)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
print(forecast)