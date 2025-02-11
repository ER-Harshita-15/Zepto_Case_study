import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset directly without user input
dataset_path = "..\\..\\..\\Data\\updated_dataset.csv"
df = pd.read_csv(dataset_path)

class ProductRecommender:
    def __init__(self, dataframe):
        self.df = dataframe

    def recommend_products_by_age(self, age_group):
        return self.df[self.df['Age_Group'] == age_group]['Product_Category'].value_counts().index.tolist()

    def recommend_products_by_gender(self, gender):
        return self.df[self.df['Gender'] == gender]['Product_Category'].value_counts().index.tolist()

    def recommend_products_by_city(self, city):
        return self.df[self.df['City'] == city]['Product_Category'].value_counts().index.tolist()

# Initialize recommender
recommender = ProductRecommender(df)

# Streamlit UI
st.title("Product Recommender System")

age_group = st.selectbox("Select Age Group", df['Age_Group'].unique())
gender = st.selectbox("Select Gender", df['Gender'].unique())
city = st.selectbox("Select City", df['City'].unique())

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