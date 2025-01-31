import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the dataset
file_path = '/D:/ZeptoAnalysis/Customer_insights/UPDATED_DATASET.CSV'
data = pd.read_csv(file_path)

# Convert necessary columns to appropriate data types
data['Discount_Applied'] = pd.to_numeric(data['Discount_Applied'], errors='coerce')
data['Loyalty_Points_Earned'] = pd.to_numeric(data['Loyalty_Points_Earned'], errors='coerce')

# Plot the relationship between Discount_Applied and Loyalty_Points_Earned
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Discount_Applied', y='Loyalty_Points_Earned', hue='Payment_Method', data=data)
plt.title('Relationship between Discounts and Loyalty Points Earned by Payment Method')
plt.xlabel('Discount Applied')
plt.ylabel('Loyalty Points Earned')
plt.legend(title='Payment Method')
plt.show()

# Calculate correlation between Discount_Applied and Loyalty_Points_Earned
correlation = data[['Discount_Applied', 'Loyalty_Points_Earned']].corr()
print("Correlation between Discount Applied and Loyalty Points Earned:")
print(correlation)