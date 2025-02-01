import pandas as pd
from Customer_insights.recommendation import recommend_products_for_customer
from Customer_insights.recommendation.DemoGraphs import recommend_products_by_age, recommend_products_by_gender, recommend_products_by_city

# Load the dataset
df = pd.read_csv('updated_dataset.csv')

# Function to design subscription plans tailored to customer needs
def design_subscription_plans(customer_id):
    # Get customer data
    customer_data = df[df['Customer_ID'] == customer_id]
    
    # Get customer demographics
    age_group = customer_data['Age_Group'].iloc[0]
    gender = customer_data['Gender'].iloc[0]
    city = customer_data['City'].iloc[0]
    
    # Get product recommendations based on customer preferences
    recommended_products, product_categories, customer_city, customer_age_group = recommend_products_for_customer(customer_id)
    
    # Get product recommendations based on demographics
    age_based_recommendations = recommend_products_by_age(age_group)
    gender_based_recommendations = recommend_products_by_gender(gender)
    city_based_recommendations = recommend_products_by_city(city)
    
    # Combine all recommendations
    all_recommendations = set(recommended_products + age_based_recommendations + gender_based_recommendations + city_based_recommendations)
    
    # Design subscription plans
    subscription_plans = {}
    for product in all_recommendations:
        if product in recommended_products:
            subscription_plans[product] = 'Monthly'
        elif product in age_based_recommendations:
            subscription_plans[product] = 'Quarterly'
        elif product in gender_based_recommendations:
            subscription_plans[product] = 'Bi-Annually'
        elif product in city_based_recommendations:
            subscription_plans[product] = 'Annually'
    
    return subscription_plans

# Example usage
customer_id = 'ZP_CUST4000'
subscription_plans = design_subscription_plans(customer_id)
print(f"\nTailored Subscription Plans for Customer ID {customer_id}:")
print(subscription_plans)
# Convert subscription plans dictionary to DataFrame for tabular display
subscription_plans_df = pd.DataFrame(list(subscription_plans.items()), columns=['Product', 'Subscription Plan'])

# Display the subscription plans in tabular form
print("\nTailored Subscription Plans for Customer ID {}:".format(customer_id))
print(subscription_plans_df)