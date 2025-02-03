# Customer Insights and Personalization

This repository contains two scripts designed to enhance customer engagement through personalized promotions and subscription plans based on customer demographics and purchasing behavior.

## Files

1. **discount.py**
2. **offer-subscription.py**

## discount.py

### Description

This script is used to design targeted promotions and discounts for customers based on their demographics and purchasing behavior.

### Features

- **Customer Data Loading**: Loads customer data from a CSV file.
- **Recommender System Integration**: Utilizes a recommender system to get product recommendations for customers.
- **Promotion Design**: Designs promotions and discounts based on customer demographics and purchasing behavior.
- **Streamlit App**: Provides a user interface to input customer ID and display targeted promotions and discounts.

### Usage

1. **Install Dependencies**: Ensure you have the required libraries installed.
    ```bash
    pip install streamlit pandas
    ```

2. **Run the Script**: Execute the script using Streamlit.
    ```bash
    streamlit run discount.py
    ```

3. **Input Customer ID**: Enter the customer ID in the provided input field to get personalized promotions and discounts.

### Example

```python
# Run the app by typing this in your terminal:
streamlit run discount.py
```

## offer-subscription.py

### Description

This script is used to create a subscription plan for customers based on their purchase history and behavior.

### Features

- **Customer Data Loading**: Loads customer data from a CSV file.
- **Feature Encoding**: Encodes categorical features for analysis.
- **Product Similarity Calculation**: Calculates product similarity using cosine similarity.
- **Customer Behavior Analysis**: Analyzes customer behavior to determine preferred categories and purchase frequency.
- **Subscription Plan Creation**: Creates subscription plans based on customer preferences and behavior.
- **Streamlit App**: Provides a user interface to upload a dataset, input customer ID, and display subscription plans.

### Usage

1. **Install Dependencies**: Ensure you have the required libraries installed.
    ```bash
    pip install streamlit pandas scikit-learn
    ```

2. **Run the Script**: Execute the script using Streamlit.
    ```bash
    streamlit run offer-subscription.py
    ```

3. **Upload Dataset**: Upload the customer dataset in CSV format.
4. **Input Customer ID**: Enter the customer ID in the provided input field to get personalized subscription plans.

### Example

```python
# Run the app by typing this in your terminal:
streamlit run offer-subscription.py
```

## Dataset

Ensure that your dataset contains the following columns for both scripts to function correctly:

- Customer_ID
- Age_Group
- Gender
- City
- Loyalty_Tier
- High_Spender_Flag
- Product_ID
- Product_Category
- Price
- Competitor_Price
- Ad_Click_Through_Rate
- Browsing_Time_mins
- Voice_Search_Count
- Visual_Search_Count
- Order_Time

## Conclusion

These scripts provide a robust framework for personalizing customer interactions through targeted promotions and subscription plans. By leveraging customer data and advanced recommendation systems, businesses can enhance customer satisfaction and loyalty.
