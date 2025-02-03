# Product Recommender System

This repository contains the code for a product recommendation system that suggests products based on age group, gender, and city. The recommendation system is built using Python and Streamlit for the user interface.

## Features

- **Age-based Recommendations**: Suggests products based on the selected age group.
- **Gender-based Recommendations**: Suggests products based on the selected gender.
- **City-based Recommendations**: Suggests products based on the selected city.

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run recommender.py
    ```
2. Upload a CSV dataset containing the product information.
3. Select the desired age group, gender, and city from the dropdown menus.
4. Click on the "Get Recommendations" button to view the recommended products.

## Dataset

The CSV dataset should contain the following columns:
- `Age_Group`: The age group of the customers.
- `Gender`: The gender of the customers.
- `City`: The city of the customers.
- `Product_Category`: The category of the products.
