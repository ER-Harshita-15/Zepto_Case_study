"""
This script loads the updated dataset, preprocesses the data, trains an XGBoost model, evaluates the model, 
plots the actual vs. predicted demand, and predicts the 'future demand' for a new product.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import os

class XGBoostModel:
    def __init__(self, filepath, save_path='plots\\XGBoost'):
        self.filepath = filepath
        self.save_path = save_path
        os.makedirs(self.save_path, exist_ok=True)
        self.df = self.load_and_preprocess_data()
        self.model = None

    def load_and_preprocess_data(self):
        df = pd.read_csv(self.filepath)
        df['Order_Time'] = pd.to_datetime(df['Order_Time'])
        df['Month'] = df['Order_Time'].dt.month
        df['Day_of_Week'] = df['Order_Time'].dt.dayofweek
        df['Hour'] = df['Order_Time'].dt.hour
        df['Rolling_Mean_Quantity'] = df.groupby('Product_ID')['Quantity'].rolling(30).mean().reset_index(level=0, drop=True)
        le = LabelEncoder()
        df['Product_ID'] = le.fit_transform(df['Product_ID'])
        return df

    def preprocess_data(self):
        X = self.df[['Product_ID', 'Price', 'Month', 'Day_of_Week', 'Hour', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Rolling_Mean_Quantity']]
        y = self.df['Quantity']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_xgboost_model(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model = xgb.XGBRegressor()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        return X_test, y_test, y_pred, mae, rmse

    def plot_actual_vs_predicted(self, y_test, y_pred):
        plt.figure(figsize=(14, 10)) 
        plt.plot(y_test.reset_index(drop=True), label='Actual', color='blue', linestyle='-', marker='o')
        plt.plot(y_pred, label='Predicted', color='red', linestyle='--', marker='x')
        plt.title('Actual vs. Predicted Demand (Quantity) Using XGBoost')
        plt.xlabel('Test Sample Index')
        plt.ylabel('Quantity (Demand)')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_path, 'actual_vs_predicted_demand.png'))
        print(f'Plot saved to {os.path.join(self.save_path, "actual_vs_predicted_demand.png")}')
        plt.close()

    def predict_future_demand(self):
        future_data = pd.DataFrame({
            'Product_ID': [123],
            'Price': [499],
            'Month': [5],
            'Day_of_Week': [3],
            'Hour': [15],
            'Competitor_Price': [400],
            'Ad_Click_Through_Rate': [0.35],
            'Rolling_Mean_Quantity': [20]
        })
        future_demand = self.model.predict(future_data)
        print(f'Predicted Demand: {future_demand}')

    def run(self):
        X_test, y_test, y_pred, mae, rmse = self.train_xgboost_model()
        print(f'MAE: {mae}, RMSE: {rmse}')
        self.plot_actual_vs_predicted(y_test, y_pred)
        self.predict_future_demand()

if __name__ == "__main__":
    xgb_model = XGBoostModel('..\\Data\\updated_dataset.csv')
    xgb_model.run()

