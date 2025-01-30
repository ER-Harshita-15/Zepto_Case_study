"""
this churn prediction model uses Random Forest Classifier to predict the cart abandonment flag
"""

import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, learning_curve, validation_curve, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import os
import numpy as np

class ChurnPredictionRF:
    def __init__(self, filepath):
        self.filepath = filepath
        self.dataset = None
        self.X = None
        self.y = None
        self.grid_search = None

    def load_data(self):
        self.dataset = pd.read_csv(self.filepath)

    def preprocess_data(self):
        # Identify numerical and categorical columns
        numerical_cols = ['Delivery_Time_mins', 'Discount_Percentage', 'Discount_Applied', 'Quantity', 'Price', 'Total_Purchase_Value', 'Lifetime_Value', 'Competitor_Price', 'Ad_Click_Through_Rate']
        categorical_cols = ['Age_Group']

        # Preprocessing for numerical data
        numerical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        # Preprocessing for categorical data
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        # Bundle preprocessing for numerical and categorical data
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, numerical_cols),
                ('cat', categorical_transformer, categorical_cols)
            ])

        # Apply transformations
        self.X = preprocessor.fit_transform(self.dataset)
        self.y = self.dataset['Cart_Abandonment_Flag']

    def train_random_forest(self):
        param_grid = {
            'n_estimators': [1, 10],  # Reduce the number of estimators
            'max_depth': [10, 20],  # Reduce the maximum depth
            'min_samples_split': [50, 70],  # Increase regularization
            'min_samples_leaf': [14, 21]  # Increase regularization
        }
        cv = StratifiedKFold(n_splits=3)
        self.grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=cv, scoring='accuracy')
        self.grid_search.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.grid_search.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        conf_matrix = confusion_matrix(self.y_test, y_pred)
        class_report = classification_report(self.y_test, y_pred)
        return accuracy, conf_matrix, class_report

    def plot_learning_curve(self, save_path):
        train_sizes = np.linspace(0.1, 1.0, 5)
        train_sizes, train_scores, test_scores = learning_curve(self.grid_search, self.X, self.y, train_sizes=train_sizes, cv=3, scoring='accuracy')
        train_mean = train_scores.mean(axis=1)
        test_mean = test_scores.mean(axis=1)
        plt.figure(figsize=(14, 10))
        plt.plot(train_sizes, train_mean, label='Training Score')
        plt.plot(train_sizes, test_mean, label='Validation Score')
        plt.xlabel('Training Size')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.title('Learning Curve')
        plt.savefig(os.path.join(save_path, 'learning_curve_rf.png'))
        plt.close()

    def plot_validation_curve(self, param_name, param_range, save_path):
        train_scores, test_scores = validation_curve(
            RandomForestClassifier(random_state=42), self.X, self.y, param_name=param_name, param_range=param_range, cv=3, scoring='accuracy'
        )
        train_mean = train_scores.mean(axis=1)
        test_mean = test_scores.mean(axis=1)
        plt.figure(figsize=(14, 10))
        plt.plot(param_range, train_mean, label='Training Score')
        plt.plot(param_range, test_mean, label='Validation Score')
        plt.xlabel(param_name)
        plt.ylabel('Accuracy')
        plt.legend()
        plt.title(f'Validation Curve for {param_name}')
        plt.savefig(os.path.join(save_path, f'validation_curve_{param_name}.png'))
        plt.close()

    def run(self):
        save_path = 'plots\\Randomforest'
        os.makedirs(save_path, exist_ok=True)
        print("Loading data...")
        self.load_data()
        print("Preprocessing data...")
        self.preprocess_data()
        print("Splitting data into train and test sets...")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42, shuffle=True, stratify=self.y)
        print("Training Random Forest model...")
        self.train_random_forest()
        print(f"Best Parameters: {self.grid_search.best_params_}")
        print(f"Best CV Accuracy: {self.grid_search.best_score_:.4f}")
        accuracy, conf_matrix, class_report = self.evaluate_model()
        print(f"Accuracy: {accuracy * 100:.2f}%")
        print("Confusion Matrix:\n", conf_matrix)
        print("Classification Report:\n", class_report)
        print("Plotting learning curves...")
        self.plot_learning_curve(save_path)
        print("Plotting validation curves...")
        self.plot_validation_curve('n_estimators', [50, 100], save_path)
        self.plot_validation_curve('max_depth', [10, 20], save_path)
        print("Done!")

if __name__ == "__main__":
    churn_prediction_rf = ChurnPredictionRF('..\\Data\\updated_dataset.csv')
    churn_prediction_rf.run()