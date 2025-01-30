"""
this module is used to predict the cart abandonment flag using Logistic Regression
"""
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import warnings
import os
import matplotlib.pyplot as plt

class ChurnPrediction:
    def __init__(self, filepath):
        self.filepath = filepath
        self.dataset = None
        self.X = None
        self.y = None
        self.grid_search = None

    def load_data(self):
        self.dataset = pd.read_csv(self.filepath)

    def preprocess_data(self):
        self.X = pd.get_dummies(self.dataset[['Age','Age_Group', 'Quantity', 'Delivery_Time_mins', 'Loyalty_Points_Earned',
                                              'Cart_Abandonment_Flag', 'Browsing_Time_mins', 'Voice_Search_Count', 'Visual_Search_Count', 'High_Spender_Flag','Price', 'Discount_Applied', 
                                              'Total_Purchase_Value', 'Lifetime_Value', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Discount_Percentage']], columns=['Age_Group'])
        self.y = self.dataset['Cart_Abandonment_Flag']

    def train_logistic_regression(self):
        param_grid = {
            'penalty': ['l1', 'l2', 'elasticnet', None],
            'C': [0.01, 0.1, 1, 10],
            'solver': ['liblinear', 'saga']
        }
        self.grid_search = GridSearchCV(LogisticRegression(random_state=42), param_grid, cv=5, scoring='accuracy')
        self.grid_search.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.grid_search.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        conf_matrix = confusion_matrix(self.y_test, y_pred)
        class_report = classification_report(self.y_test, y_pred)
        return accuracy, conf_matrix, class_report

    def plot_predictions(self, y_test, y_pred):
        plt.figure(figsize=(14, 10))
        plt.scatter(y_test, y_pred, alpha=0.3)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.title('Actual vs. Predicted Values')
        plt.tight_layout()
        plt.savefig(os.path.join('plots\\LogisticRegression', 'predictions_scatter_plot.png'))
        print(f'Prediction scatter plot saved to {os.path.join("plots\\LogisticRegression", "predictions_scatter_plot.png")}')
        plt.close()

    def run(self):
        warnings.filterwarnings('ignore')
        save_path = 'plots\\LogisticRegression'
        os.makedirs(save_path, exist_ok=True)
        self.load_data()
        self.preprocess_data()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)
        self.train_logistic_regression()
        print(f"Best Parameters: {self.grid_search.best_params_}")
        accuracy, conf_matrix, class_report = self.evaluate_model()
        print(f"Accuracy: {accuracy * 100:.2f}%")
        print("Confusion Matrix:")
        print(conf_matrix)
        print("Classification Report:")
        print(class_report)
        cv_scores = cross_val_score(self.grid_search.best_estimator_, self.X, self.y, cv=5, scoring='accuracy')
        print(f"Cross-Validation Scores: {cv_scores}")
        print(f"Mean CV Accuracy: {cv_scores.mean():.4f}")
        self.plot_predictions(self.y_test, self.grid_search.predict(self.X_test))

        index_to_predict = 72
        data_dummies = pd.get_dummies(self.dataset[['Delivery_Time_mins', 'Discount_Percentage', 'Discount_Applied', 
                                                    'Quantity', 'Age_Group']], columns=['Age_Group'])
        missing_cols = set(self.X.columns) - set(data_dummies.columns)
        for col in missing_cols:
            data_dummies[col] = 0
        data_dummies = data_dummies[self.X.columns]
        pred = self.grid_search.best_estimator_.predict(data_dummies)
        print(f"Prediction for index {index_to_predict}: {pred[index_to_predict]}")

if __name__ == "__main__":
    churn_prediction = ChurnPrediction('..\\Data\\updated_dataset.csv')
    churn_prediction.run()

