import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
dataset = pd.read_csv('updated_dataset.csv')

# Generate dummy variables for Age_Group
X_dummies = pd.get_dummies(dataset[['Age_Group']], columns=['Age_Group'])

# Concatenate the dummy variables with relevant features
X_final = pd.concat(
    [dataset[['Delivery_Time_mins', 'Discount_Percentage', 'Discount_Applied', 'Quantity']], X_dummies],
    axis=1
)

# Check the resulting feature set
print("Features after preprocessing:\n", X_final.columns)

# Define features (X) and target variable (y)
X = X_final
y = dataset['Cart_Abandonment_Flag']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best CV Accuracy: {grid_search.best_score_:.4f}")


# Make predictions on the test set
y_pred = grid_search.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Classification Report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# Accuracy on training and testing data
train_accuracy = accuracy_score(y_train, grid_search.predict(X_train))
test_accuracy = accuracy_score(y_test, y_pred)

print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}")

# Process new data for prediction
new_data_dummies = pd.get_dummies(dataset[['Delivery_Time_mins', 'Discount_Percentage', 'Discount_Applied', 'Quantity', 'Age_Group']], columns=['Age_Group'])

# Ensure the columns match the training set by adding missing columns
missing_cols = set(X.columns) - set(new_data_dummies.columns)
for col in missing_cols:
    new_data_dummies[col] = 0

# Reorder columns to match the training data
new_data_dummies = new_data_dummies[X.columns]

# Predict using the model
pred = grid_search.predict(new_data_dummies)
print(f"Prediction for index 72: {pred[72]}")

from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(grid_search, X, y, cv=5, scoring='accuracy')
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Accuracy: {cv_scores.mean():.4f}")


from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

train_sizes, train_scores, test_scores = learning_curve(grid_search, X, y, cv=5, scoring='accuracy')
train_mean = train_scores.mean(axis=1)
test_mean = test_scores.mean(axis=1)

plt.plot(train_sizes, train_mean, label='Training Score')
plt.plot(train_sizes, test_mean, label='Validation Score')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Learning Curve')
plt.show()

""""
# Learning Curve to visualize Overfitting
train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, cv=5, n_jobs=-1)

# Calculate the mean and std deviation
train_mean = train_scores.mean(axis=1)
test_mean = test_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_std = test_scores.std(axis=1)

# Plot the Learning Curve
plt.plot(train_sizes, train_mean, label="Training Accuracy", color='blue')
plt.plot(train_sizes, test_mean, label="Testing Accuracy", color='green')
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color='blue', alpha=0.1)
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color='green', alpha=0.1)

plt.xlabel('Training Set Size')
plt.ylabel('Accuracy')
plt.title('Learning Curves (Overfitting Check)')
plt.legend()
plt.show()
"""""""""