import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import sys
import os

# Ensure the recommendation modules are in the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from recommendation.insights_recommendation.recommender import ProductRecommender
from recommendation.personalized_recommendation.recommender import RecommenderSystem

class SubscriptionOffer:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.df.dropna(inplace=True)
        self.label_encoders = {}
        for column in ['Gender', 'City', 'Product_Category', 'Payment_Method', 'Age_Group', 'Loyalty_Tier']:
            le = LabelEncoder()
            self.df[column] = le.fit_transform(self.df[column])
            self.label_encoders[column] = le

    def analyze_customer_behavior(self, customer_id):
        customer_data = self.df[self.df['Customer_ID'] == customer_id]
        if customer_data.empty:
            return None, None, None, None
        
        # Get customer details
        customer_city_encoded = customer_data['City'].iloc[0]
        customer_city = self.label_encoders['City'].inverse_transform([customer_city_encoded])[0]
        customer_age_group_encoded = customer_data['Age_Group'].iloc[0]
        customer_age_group = self.label_encoders['Age_Group'].inverse_transform([customer_age_group_encoded])[0]
        
        # Get preferred product categories
        preferred_categories = customer_data['Product_Category'].value_counts().index.tolist()
        preferred_categories = self.label_encoders['Product_Category'].inverse_transform(preferred_categories)
        
        # Get purchase frequency
        purchase_frequency = customer_data['Order_Time'].nunique()
        
        return customer_city, customer_age_group, preferred_categories, purchase_frequency

    def create_subscription_plans(self, preferred_categories, purchase_frequency):
        subscription_plans = []
        
        # Basic Plan
        basic_plan = {
            'name': 'Basic Plan',
            'description': 'Monthly subscription with limited access to products.',
            'products': preferred_categories[:3],
            'frequency': 'Monthly',
            'price': 9.99
        }
        subscription_plans.append(basic_plan)
        
        # Standard Plan
        standard_plan = {
            'name': 'Standard Plan',
            'description': 'Bi-weekly subscription with access to more products.',
            'products': preferred_categories[:5],
            'frequency': 'Bi-weekly',
            'price': 19.99
        }
        subscription_plans.append(standard_plan)
        
        # Premium Plan
        premium_plan = {
            'name': 'Premium Plan',
            'description': 'Weekly subscription with access to all preferred products.',
            'products': preferred_categories,
            'frequency': 'Weekly',
            'price': 29.99
        }
        subscription_plans.append(premium_plan)
        
        return subscription_plans

# Streamlit app
st.title("Customer Subscription Plans")

st.subheader("Upload CSV dataset")
subscription_dataset_path = st.file_uploader("Drag and drop file here", type=["csv"], key="subscription_dataset")

if subscription_dataset_path is not None:
    subscription_offer = SubscriptionOffer(subscription_dataset_path)
    product_recommender = ProductRecommender(subscription_dataset_path)

    customer_id = st.text_input("Enter Customer ID:", "ZP_CUST4000", key="subscription_customer_id")
    if st.button("Get Subscription Plans", key="subscription_plans"):
        customer_city, customer_age_group, preferred_categories, purchase_frequency = subscription_offer.analyze_customer_behavior(customer_id)
        
        if not preferred_categories:
            st.warning("No data found for this customer ID. Please check the ID and try again.")
        else:
            st.subheader("Customer Details")
            st.write(f"**Customer ID:** {customer_id}")
            st.write(f"**Customer City:** {customer_city}")
            st.write(f"**Customer Age Group:** {customer_age_group}")
            
            st.subheader("Preferred Product Categories")
            for category in preferred_categories:
                st.write(f"- {category}")
            
            st.subheader("Subscription Plans")
            subscription_plans = subscription_offer.create_subscription_plans(preferred_categories, purchase_frequency)
            for plan in subscription_plans:
                st.write(f"### {plan['name']}")
                st.write(f"**Description:** {plan['description']}")
                st.write(f"**Products:** {', '.join(plan['products'])}")
                st.write(f"**Frequency:** {plan['frequency']}")
                st.write(f"**Price:** ${plan['price']}")

            # Additional product recommendations
            st.subheader("Additional Product Recommendations")
            recommended_products_by_age = product_recommender.recommend_products_by_age(customer_age_group)
            recommended_products_by_gender = product_recommender.recommend_products_by_gender(self.df[self.df['Customer_ID'] == customer_id]['Gender'].iloc[0])
            recommended_products_by_city = product_recommender.recommend_products_by_city(customer_city)

            st.write("Recommended Products by Age Group:")
            for product in recommended_products_by_age:
                st.write(f"- {product}")

            st.write("Recommended Products by Gender:")
            for product in recommended_products_by_gender:
                st.write(f"- {product}")

            st.write("Recommended Products by City:")
            for product in recommended_products_by_city:
                st.write(f"- {product}")