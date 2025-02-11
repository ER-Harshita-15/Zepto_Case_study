import pandas as pd

df = pd.read_csv("..\\Data\\Zepto_Analytics_Dataset.csv")

print(df['Loyalty_Points_Earned'].max())
print(df['Loyalty_Points_Earned'].min())
