"""
this script is used to design targeted promotions and discounts for customers 
based on their demographics and purchasing behavior.
"""

import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from recommendation.personalized_recommendation.recommender import RecommenderSystem

# Load the dataset
df = pd.read_csv('.\\Data\\updated_dataset.csv')

# Initialize the recommender system (ensure this path points to your dataset correctly)
recommender = RecommenderSystem('..\\..\\Data\\updated_dataset.csv')

# Function to design targeted promotions and discounts
def design_promotions_and_discounts(customer_id):
    # Get customer data
    customer_data = df[df['Customer_ID'] == customer_id]
    
    # Get customer demographics
    age_group = customer_data['Age_Group'].iloc[0]
    gender = customer_data['Gender'].iloc[0]
    city = customer_data['City'].iloc[0]
    loyalty_tier = customer_data['Loyalty_Tier'].iloc[0]
    high_spender_flag = customer_data['High_Spender_Flag'].iloc[0]
    
    # Get product recommendations based on customer preferences (from Code B)
    recommended_products, product_categories, customer_city, customer_age_group = recommender.recommend_products_for_customer(customer_id)[:4]
    
    # Design promotions and discounts based on demographics and purchasing behavior
    promotions = {}
    for product, category in zip(recommended_products, product_categories):
        # Apply discount logic based on demographic and behavioral criteria
        if gender == 'Female' and category == 'Groceries':
            promotions[product] = "15% off"
        elif age_group == '18-25' and category == 'Snacks':
            promotions[product] = '20% off'
        elif city == customer_city:
            promotions[product] = '10% off'
        elif loyalty_tier == 'Silver':
            promotions[product] = '25% off'
        elif high_spender_flag == 1:
            promotions[product] = '30% off'
        elif product not in promotions:
            promotions[product] = '5% off'
    
    return promotions

# Streamlit app
st.title("Customer Promotions and Discounts")

# Customer ID input with unique key
customer_id = st.text_input("Enter Customer ID:", "ZP_CUST4000", key="customer_id_input")

# Display customer details and promotions when the button is clicked
if st.button("Get Promotions"):
    # Get promotions for the entered customer
    promotions = design_promotions_and_discounts(customer_id)
    
    # Check if promotions are available
    if promotions:
        st.subheader(f"Targeted Promotions and Discounts for Customer ID {customer_id}")
        
        # Display customer demographics
        customer_data = df[df['Customer_ID'] == customer_id].iloc[0]
        st.write(f"**Customer ID:** {customer_id}")
        st.write(f"**Age Group:** {customer_data['Age_Group']}")
        st.write(f"**Gender:** {customer_data['Gender']}")
        st.write(f"**City:** {customer_data['City']}")
        st.write(f"**Loyalty Tier:** {customer_data['Loyalty_Tier']}")
        st.write(f"**High Spender:** {'Yes' if customer_data['High_Spender_Flag'] == 1 else 'No'}")
        
        # Show product recommendations and their discounts
        st.subheader("Recommended Products and Discounts")
        for product, discount in promotions.items():
            st.write(f"- **Product ID:** {product} - **Discount:** {discount}")
    else:
        st.warning(f"No promotions available for Customer ID {customer_id}")

# Run the app by typing this in your terminal:
# streamlit run your_script.py
