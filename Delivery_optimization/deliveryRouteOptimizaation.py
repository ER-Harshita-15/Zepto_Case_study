"""
this script is used to analyze the delivery data and train a model to predict delivery times
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

class DeliveryAnalysis:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.model = None
        self.plot_dir = "plots"
        os.makedirs(self.plot_dir, exist_ok=True)

    def plot_distribution(self):
        plt.figure(figsize=(10, 14))
        sns.histplot(self.df['Delivery_Time_mins'], bins=30, kde=True)
        plt.title('Distribution of Delivery Times')
        plt.xlabel('Delivery Time (minutes)')
        plt.ylabel('Frequency')
        plt.savefig(os.path.join(self.plot_dir, 'delivery_time_distribution.png'))
        plt.close()

    def plot_delivery_by_city(self):
        plt.figure(figsize=(12, 14))
        sns.boxplot(x='City', y='Delivery_Time_mins', data=self.df)
        plt.title('Delivery Times by City')
        plt.xlabel('City')
        plt.ylabel('Delivery Time (minutes)')
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(self.plot_dir, 'delivery_times_by_city.png'))
        plt.close()

    def plot_delivery_by_category(self):
        plt.figure(figsize=(12, 14))
        sns.boxplot(x='Product_Category', y='Delivery_Time_mins', data=self.df)
        plt.title('Delivery Times by Product Category')
        plt.xlabel('Product Category')
        plt.ylabel('Delivery Time (minutes)')
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(self.plot_dir, 'delivery_times_by_category.png'))
        plt.close()
    def plot_delivery_times_by_order_day(self):
        self.df['Order_Day'] = pd.to_datetime(self.df['Order_Time']).dt.dayofweek
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='Order_Day', y='Delivery_Time_mins', data=self.df)
        plt.title('Delivery Times by Order Day')
        plt.xlabel('Order Day (0=Monday, 6=Sunday)')
        plt.ylabel('Delivery Time (minutes)')
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(self.plot_dir, 'delivery_times_by_order_day.png'))
        plt.close()
    def train_model(self):
            # Feature Engineering
            self.df['Order_Hour'] = pd.to_datetime(self.df['Order_Time']).dt.hour
            self.df['Order_Day'] = pd.to_datetime(self.df['Order_Time']).dt.dayofweek
            
            X = self.df[['City', 'Product_Category', 'Payment_Method', 'High_Spender_Flag', 'Order_Hour', 'Order_Day']]
            y = self.df['Delivery_Time_mins']
            
            X = pd.get_dummies(X, columns=['City', 'Product_Category', 'Payment_Method'])
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Hyperparameter Tuning
            param_grid = {
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            }
            
            grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid=param_grid, cv=5, n_jobs=-1, scoring='neg_mean_absolute_error')
            grid_search.fit(X_train, y_train)
            
            self.model = grid_search.best_estimator_
            
            y_pred = self.model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            print(f'Mean Absolute Error: {mae}')
            
            self.plot_feature_importance(X)

    def plot_feature_importance(self, X):
        feature_importances = self.model.feature_importances_
        importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})
        importance_df = importance_df.sort_values(by='Importance', ascending=False)
        
        plt.figure(figsize=(22, 8))
        sns.barplot(x='Importance', y='Feature', data=importance_df)
        plt.title('Feature Importance')
        plt.savefig(os.path.join(self.plot_dir, 'feature_importance.png'))
        plt.close()

if __name__ == "__main__":
    analysis = DeliveryAnalysis('..\\Data\\updated_dataset.csv')
    analysis.plot_distribution()
    analysis.plot_delivery_by_city()
    analysis.plot_delivery_by_category()
    analysis.plot_delivery_times_by_order_day()
    analysis.train_model()