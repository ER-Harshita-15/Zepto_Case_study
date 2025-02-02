import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import os

class ARIMAModel:
    def __init__(self, filepath, save_path='plots\\ARIMA'):
        self.filepath = filepath
        self.save_path = save_path
        os.makedirs(self.save_path, exist_ok=True)
        self.sales = self.load_data()
        self.model = None

    def load_data(self):
        dataset = pd.read_csv(self.filepath)
        daily_sales = dataset.groupby('Order_Time').sum()['Quantity']
        sales = pd.DataFrame({'ds': pd.to_datetime(daily_sales.index), 'y': daily_sales.values})
        return sales

    def train_arima_model(self, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)):
        self.model = SARIMAX(self.sales['y'], order=order, seasonal_order=seasonal_order)
        self.model = self.model.fit(disp=False, maxiter=1000)

    def forecast_sales(self, periods):
        forecast = self.model.get_forecast(steps=periods)
        forecast_index = pd.date_range(start=self.sales['ds'].iloc[-1] + pd.Timedelta(days=1), periods=periods)
        forecast_df = pd.DataFrame({'ds': forecast_index, 'yhat': forecast.predicted_mean})
        return forecast_df

    def evaluate_model(self, train, test, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)):
        model = SARIMAX(train['y'], order=order, seasonal_order=seasonal_order)
        model = model.fit(disp=False, maxiter=1000)
        forecast_test = model.get_forecast(steps=len(test))
        y_true = test['y'].values
        y_pred = forecast_test.predicted_mean.values
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        return mae, rmse, y_true, y_pred

    def plot_actual_vs_predicted(self, test, y_true, y_pred):
        plt.figure(figsize=(14, 10))  # Increased height
        plt.plot(test['ds'], y_true, label='Actual Sales', color='blue', marker='o')
        plt.plot(test['ds'], y_pred, label='Predicted Sales', color='red', linestyle='--', marker='x')
        plt.title('Actual vs Predicted Sales')
        plt.xlabel('Date')
        plt.ylabel('Sales Quantity')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(self.save_path, 'actual_vs_predicted_sales.png'))
        print(f'Plot saved to {os.path.join(self.save_path, "actual_vs_predicted_sales.png")}')
        plt.close()

    def run(self):
        self.train_arima_model()
        forecast = self.forecast_sales(30)
        train = self.sales[:-30]
        test = self.sales[-30:]
        mae, rmse, y_true, y_pred = self.evaluate_model(train, test)
        print(f'MAE: {mae}')
        print(f'RMSE: {rmse}')
        self.plot_actual_vs_predicted(test, y_true, y_pred)

if __name__ == "__main__":
    arima_model = ARIMAModel('..\\Data\\Zepto_Analytics_Dataset.csv')
    arima_model.run()

