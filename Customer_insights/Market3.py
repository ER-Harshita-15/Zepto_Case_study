import pandas as pd

def marketing_analytics(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Get marketing spend from user (in rupees)
    marketing_spend = float(input("Enter total marketing spend (INR): "))
    
    # Customer Acquisition Cost (CAC) in INR
    unique_customers = df["Customer_ID"].nunique()
    CAC = marketing_spend / unique_customers
    
    # Conversion Rate
    conversion_rate = (len(df) / unique_customers) * 100
    
    # Top-selling product categories
    category_sales = df.groupby("Product_Category")["Price"].sum().sort_values(ascending=False)
    
    # Customer demographics
    age_distribution = df["Age"].describe()
    gender_distribution = df["Gender"].value_counts(normalize=True) * 100
    
    # High-spending customer segments
    customer_spending = df.groupby(["Age", "Gender"])["Price"].sum().reset_index()
    top_segments = customer_spending.sort_values(by="Price", ascending=False).head(5)
    
    # Revenue contribution by product category
    category_revenue = df.groupby("Product_Category")["Price"].sum().reset_index()
    category_revenue["Revenue_Share"] = (category_revenue["Price"] / category_revenue["Price"].sum()) * 100
    
    # Suggested budget allocation based on revenue share (in INR)
    budget_allocation = category_revenue.copy()
    budget_allocation["Suggested_Budget (INR)"] = (budget_allocation["Revenue_Share"] / 100) * marketing_spend
    
    # Print results
    print(f"Customer Acquisition Cost (CAC): ₹{CAC:.2f}")
    print(f"Conversion Rate: {conversion_rate:.2f}%")
    print("\nTop Product Categories:")
    print(category_sales.head())
    print("\nAge Distribution:")
    print(age_distribution)
    print("\nGender Distribution:")
    print(gender_distribution)
    print("\nTop High-Spending Customer Segments:")
    print(top_segments)
    print("\nSuggested Budget Allocation (INR):")
    print(budget_allocation)
    
# Example usage
marketing_analytics("Zepto_Analytics_Dataset.csv")
