import pandas as pd

df=pd.read_csv('updated_dataset.csv')
print(df.head())
print(df.info())

# Datatypes Identification
object_columns = df.select_dtypes(include='object').columns.tolist()
int_columns=df.select_dtypes(include='int64').columns.tolist()
float_columns=df.select_dtypes(include='float').columns.tolist()
print(f"Object columns list: {object_columns}")
print(f"Integer columns list: {int_columns}")
print(f"Float columns list: {float_columns}")

# Convert categorical columns (object type) to numerical using Label Encoding
df_encoded = df.copy()
for col in df.select_dtypes(include='object').columns:
    df_encoded[col] = df_encoded[col].astype('category').cat.codes

# Calculate the correlation of 'Cart_Abandonment_Flag' with all other columns
correlation_with_cart_abandonment = df_encoded.corr()['Cart_Abandonment_Flag'].sort_values(ascending=False)

# Display the sorted correlations
print(correlation_with_cart_abandonment)

print(df['Cart_Abandonment_Flag'].value_counts())