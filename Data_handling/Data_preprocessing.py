"""
-> This script is used to preprocess the data. 
-> It loads the data, 
-> identifies the data types of the columns, 
-> encodes the categorical columns, 
-> calculates the correlation of the columns with the target column and prints the correlation values.
"""
import pandas as pd

class DataPreprocessing:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
        self.df_encoded = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath)

    def identify_datatypes(self):
        object_columns = self.df.select_dtypes(include='object').columns.tolist()
        int_columns = self.df.select_dtypes(include='int64').columns.tolist()
        float_columns = self.df.select_dtypes(include='float').columns.tolist()
        return object_columns, int_columns, float_columns

    def encode_categorical_columns(self):
        self.df_encoded = self.df.copy()
        for col in self.df.select_dtypes(include='object').columns:
            self.df_encoded[col] = self.df_encoded[col].astype('category').cat.codes

    def calculate_correlations(self):
        correlation_with_cart_abandonment = self.df_encoded.corr()['Cart_Abandonment_Flag'].sort_values(ascending=False)
        return correlation_with_cart_abandonment

    def run(self):
        self.load_data()
        print(self.df.head(),"\n")
        print(self.df.info(),"\n")
        object_columns, int_columns, float_columns = self.identify_datatypes()
        print(f"Object columns list: {object_columns}\n")
        print(f"Integer columns list: {int_columns}\n")
        print(f"Float columns list: {float_columns}\n")
        self.encode_categorical_columns()
        correlation_with_cart_abandonment = self.calculate_correlations()
        print("Correlation with cart abandonment :\n",correlation_with_cart_abandonment.sort_values(ascending=False),"\n")
        print(self.df['Cart_Abandonment_Flag'].value_counts())

if __name__ == "__main__":
    data_preprocessing = DataPreprocessing('..\\Data\\updated_dataset.csv')
    data_preprocessing.run()