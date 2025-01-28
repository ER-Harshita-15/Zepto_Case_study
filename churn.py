import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv('updated_dataset.csv')
#print(df.head())
#print(df.info())

# Assuming df is your DataFrame
object_columns = df.select_dtypes(include='object').columns.tolist()

print(object_columns)



# Assuming df is your DataFrame

# Convert categorical columns (object type) to numerical using Label Encoding
df_encoded = df.copy()
for col in df.select_dtypes(include='object').columns:
    df_encoded[col] = df_encoded[col].astype('category').cat.codes

# Now, calculate the correlation of 'Cart_Abandonment_Flag' with all other columns
correlation_with_cart_abandonment = df_encoded.corr()['Cart_Abandonment_Flag']

print(correlation_with_cart_abandonment)




