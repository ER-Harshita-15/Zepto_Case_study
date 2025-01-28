import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, learning_curve
import matplotlib.pyplot as plt

# Load the dataset
dataset= pd.read_csv('updated_dataset.csv')

# Generate dummy variables for Age_Group
X_dummies = pd.get_dummies(dataset[['Age', 'Delivery_Time_mins', 'Age_Group']], columns=['Age_Group'])

# Check the columns generated after dummy encoding
print("Columns after pd.get_dummies():", dataset.columns)

non_encoded_columns = dataset[['Age', 'Delivery_Time_mins']]

# Concatenate the non-encoded columns with the dummied columns
X_final = pd.concat([non_encoded_columns, X_dummies.drop(columns=['Age', 'Delivery_Time_mins'])], axis=1)

# Check the resulting X
print(X_final)

# Adjust the feature set (X) based on the actual columns
X = X_final
y = dataset['Cart_Abandonment_Flag']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the RandomForest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

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

# Predict on training and testing data
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Accuracy on training and testing data
train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, test_pred)

print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}")

# Generate dummy variables for Age_Group
data_dummies = pd.get_dummies(dataset[['Age', 'Delivery_Time_mins', 'Age_Group']], columns=['Age_Group'])

# Ensure the columns match the training set by adding missing columns with zeros
missing_cols = set(X.columns) - set(data_dummies.columns)
for col in missing_cols:
    data_dummies[col] = 0

# Reorder columns to match the training data
data_dummies = data_dummies[X.columns]
print(data_dummies)

# Predict using the model
pred = model.predict(data_dummies)
print(pred[72])

"""""""""
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