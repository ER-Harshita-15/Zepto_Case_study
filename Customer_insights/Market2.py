import pandas as pd

def marketing_analytics(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Get marketing spend from user
    marketing_spend = float(input("Enter total marketing spend: "))
    
    # Customer Acquisition Cost (CAC)
    unique_customers = df["Customer_ID"].nunique()
    CAC = marketing_spend / unique_customers
    
    # Conversion Rate
    conversion_rate = (len(df) / unique_customers) * 100
    
    # Top-selling product categories
    category_sales = df.groupby("Product_Category")["Price"].sum().sort_values(ascending=False)
    
    # Customer demographics
    age_distribution = df["Age"].describe()
    gender_distribution = df["Gender"].value_counts(normalize=True) * 100
    
    # Print results
    print(f"Customer Acquisition Cost (CAC): ${CAC:.2f}")
    print(f"Conversion Rate: {conversion_rate:.2f}%")
    print("\nTop Product Categories:")
    print(category_sales.head())
    print("\nAge Distribution:")
    print(age_distribution)
    print("\nGender Distribution:")
    print(gender_distribution)
    
# Example usage
marketing_analytics("Zepto_Analytics_Dataset.csv")