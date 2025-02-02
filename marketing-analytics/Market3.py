import streamlit as st
import pandas as pd

# Fixed dataset path
file_path = 'ZEPTO_ANALYTICS_DATASET.CSV'

# Function to perform marketing analytics
def marketing_analytics(file_path, marketing_spend):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Customer Acquisition Cost (CAC) in INR
    unique_customers = df["Customer_ID"].nunique()
    CAC = marketing_spend / unique_customers
    
    # Conversion Rate
    conversion_rate = (len(df) / unique_customers) * 100
    
    # Top-selling product categories
    category_sales = df.groupby("Product_Category")["Price"].sum().sort_values(ascending=False)
    
    # High-performing channels (based on Payment Method)
    channel_performance = df["Payment_Method"].value_counts()
    
    # Age distribution
    age_groups = pd.cut(df["Age"], bins=[0, 18, 25, 35, 45, 55, 65, 100], labels=['0-18', '19-25', '26-35', '36-45', '46-55', '56-65', '65+'])
    age_group_performance = df.groupby(age_groups).size().reset_index(name='Count')
    
    # Suggested budget allocation based on revenue share (in INR)
    category_revenue = df.groupby("Product_Category")["Price"].sum().reset_index()
    category_revenue["Revenue_Share"] = (category_revenue["Price"] / category_revenue["Price"].sum()) * 100
    budget_allocation = category_revenue.copy()
    budget_allocation["Suggested_Budget (INR)"] = (budget_allocation["Revenue_Share"] / 100) * marketing_spend
    
    return CAC, conversion_rate, category_sales, age_group_performance, channel_performance, budget_allocation

# Streamlit Title
st.title("Marketing Analytics Dashboard")

# Sidebar Input for Marketing Spend
marketing_spend = st.sidebar.number_input("Enter total marketing spend (INR):", min_value=1, value=1000000, step=1000)

# Load the fixed dataset
df = pd.read_csv(file_path)

# High-performing Channels (from Payment Method)
high_performing_channels = df["Payment_Method"].value_counts().index.tolist()
selected_channels = st.sidebar.multiselect("Select High-Performing Channels", high_performing_channels, default=high_performing_channels)

# Filter data by selected channels
filtered_df = df[df["Payment_Method"].isin(selected_channels)]

# Perform Analytics
CAC, conversion_rate, category_sales, age_group_performance, channel_performance, budget_allocation = marketing_analytics(file_path, marketing_spend)

# Display Results
st.subheader(f"Customer Acquisition Cost (CAC): ₹{CAC:.2f}")
st.subheader(f"Conversion Rate: {conversion_rate:.2f}%")
    
# Display top product categories
st.subheader("Top Product Categories by Sales:")
st.write(category_sales.head())

# Display Age Distribution
st.subheader("Audience Targeting by Age Group:")
st.write(age_group_performance)

# Display High-Performing Channels
st.subheader("High-Performing Channels for Customer Acquisition:")
st.write(channel_performance)

# Display Suggested Budget Allocation
st.subheader("Suggested Budget Allocation by Product Category:")
st.write(budget_allocation)
