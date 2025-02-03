"""
this is the recommender.py file which contains the code for the product recommendation system.
The recommender system recommends products based on age group, gender, and city.
"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

class ProductRecommender:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)

    def recommend_products_by_age(self, age_group):
        recommended_products = self.df[self.df['Age_Group'] == age_group]['Product_Category'].value_counts().index.tolist()
        return recommended_products

    def recommend_products_by_gender(self, gender):
        recommended_products = self.df[self.df['Gender'] == gender]['Product_Category'].value_counts().index.tolist()
        return recommended_products

    def recommend_products_by_city(self, city):
        recommended_products = self.df[self.df['City'] == city]['Product_Category'].value_counts().index.tolist()
        return recommended_products

# Streamlit UI
st.title("Product Recommender System")

dataset_path = st.file_uploader("Upload CSV dataset", type=["csv"])

if dataset_path is not None:
    recommender = ProductRecommender(dataset_path)
    
    age_group = st.selectbox("Select Age Group", recommender.df['Age_Group'].unique())
    gender = st.selectbox("Select Gender", recommender.df['Gender'].unique())
    city = st.selectbox("Select City", recommender.df['City'].unique())
    
    if st.button("Get Recommendations"):
        age_recommendations = recommender.recommend_products_by_age(age_group)
        gender_recommendations = recommender.recommend_products_by_gender(gender)
        city_recommendations = recommender.recommend_products_by_city(city)
        
        def display_recommendations(title, recommendations):
            st.subheader(title)
            if recommendations:
                st.write("Recommendation from highest to lowest:")
                for idx, product in enumerate(recommendations, start=1):
                    st.write(f"{idx}. {product}")
            else:
                st.write("No recommendations")
        
        display_recommendations(f"Recommended Products for Age Group {age_group}", age_recommendations)
        display_recommendations(f"Recommended Products for Gender {gender}", gender_recommendations)
        display_recommendations(f"Recommended Products for City {city}", city_recommendations)