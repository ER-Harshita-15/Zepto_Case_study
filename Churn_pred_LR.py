import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Load the dataset
dataset = pd.read_csv('updated_dataset.csv')

print(dataset.columns)


# Preprocessing: Generate dummy variables for Age_Group
X = pd.get_dummies(dataset[['Age','Age_Group', 'Quantity', 'Delivery_Time_mins', 'Loyalty_Points_Earned',
                             'Cart_Abandonment_Flag', 'Browsing_Time_mins', 'Voice_Search_Count', 'Visual_Search_Count', 'High_Spender_Flag','Price', 'Discount_Applied', 
                             'Total_Purchase_Value', 'Lifetime_Value', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Discount_Percentage']], columns=['Age_Group'])

# Target variable
y = dataset['Cart_Abandonment_Flag']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Logistic Regression model
log_reg = LogisticRegression(random_state=42)

#Hyper parameter tuning
param_grid = {
    'penalty': ['l1', 'l2', 'elasticnet', None],
    'C': [0.01, 0.1, 1, 10],  # Lower C for stronger regularization
    'solver': ['liblinear', 'saga']
}

grid_search = GridSearchCV(log_reg, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Best parameters and model
print(f"Best Parameters: {grid_search.best_params_}")
best_model = grid_search.best_estimator_

# Train the best Logistic Regression model
best_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = best_model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Classification Report
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)

# Cross-Validation Scores
cv_scores = cross_val_score(best_model, X, y, cv=5, scoring='accuracy')
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Accuracy: {cv_scores.mean():.4f}")

# Test a specific prediction
index_to_predict = 72
data_dummies = pd.get_dummies(dataset[['Delivery_Time_mins', 'Discount_Percentage', 'Discount_Applied', 
                                       'Quantity', 'Age_Group']], columns=['Age_Group'])

# Ensure consistency in columns
missing_cols = set(X.columns) - set(data_dummies.columns)
for col in missing_cols:
    data_dummies[col] = 0
data_dummies = data_dummies[X.columns]

# Predict for a specific instance
pred = best_model.predict(data_dummies)
print(f"Prediction for index {index_to_predict}: {pred[index_to_predict]}")

