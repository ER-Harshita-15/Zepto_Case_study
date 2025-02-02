import pandas as pd

# Load the dataset
df = pd.read_csv('updated_dataset.csv')

# Segment customers by demographics
age_groups = df.groupby('Age_Group').size()
gender_groups = df.groupby('Gender').size()
city_groups = df.groupby('City').size()

# Segment customers by loyalty points
loyalty_tiers = df.groupby('Loyalty_Tier').size()
high_spenders = df[df['High_Spender_Flag'] == 1].shape[0]

# Segment customers by purchasing behavior
product_categories = df.groupby('Product_Category').size()
payment_methods = df.groupby('Payment_Method').size()
cart_abandonment = df[df['Cart_Abandonment_Flag'] == 1].shape[0]

# Print the results
print("Customer Segmentation by Demographics:")
print("Age Groups:\n", age_groups)
print("Gender Groups:\n", gender_groups)
print("City Groups:\n", city_groups)

print("\nCustomer Segmentation by Loyalty Points:")
print("Loyalty Tiers:\n", loyalty_tiers)
print("High Spenders:", high_spenders)

print("\nCustomer Segmentation by Purchasing Behavior:")
print("Product Categories:\n", product_categories)
print("Payment Methods:\n", payment_methods)
print("Cart Abandonment:", cart_abandonment)

""""
import matplotlib.pyplot as plt

# Plotting Age Groups
plt.figure(figsize=(10, 6))
age_groups.plot(kind='bar', color='skyblue')
plt.title('Customer Segmentation by Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')
plt.show()

# Plotting Gender Groups
plt.figure(figsize=(10, 6))
gender_groups.plot(kind='bar', color='lightgreen')
plt.title('Customer Segmentation by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.show()

# Plotting City Groups
plt.figure(figsize=(10, 6))
city_groups.plot(kind='bar', color='salmon')
plt.title('Customer Segmentation by City')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.show()

# Plotting Loyalty Tiers
plt.figure(figsize=(10, 6))
loyalty_tiers.plot(kind='bar', color='orange')
plt.title('Customer Segmentation by Loyalty Tiers')
plt.xlabel('Loyalty Tier')
plt.ylabel('Number of Customers')
plt.show()

# Plotting High Spenders
plt.figure(figsize=(10, 6))
plt.bar(['High Spenders'], [high_spenders], color='purple')
plt.title('Number of High Spenders')
plt.ylabel('Number of Customers')
plt.show()

# Plotting Product Categories
plt.figure(figsize=(10, 6))
product_categories.plot(kind='bar', color='teal')
plt.title('Customer Segmentation by Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Number of Customers')
plt.show()

# Plotting Payment Methods
plt.figure(figsize=(10, 6))
payment_methods.plot(kind='bar', color='gold')
plt.title('Customer Segmentation by Payment Methods')
plt.xlabel('Payment Method')
plt.ylabel('Number of Customers')
plt.show()


# Segment customers by cart abandonment and delivery time
cart_abandonment_by_delivery_time = df[df['Cart_Abandonment_Flag'] == 1].groupby('Delivery_Time_mins').size()

# Plotting Cart Abandonment by Delivery Time
plt.figure(figsize=(10, 6))
cart_abandonment_by_delivery_time.plot(kind='bar', color='red')
plt.title('Cart Abandonment by Delivery Time')
plt.xlabel('Delivery Time (mins)')
plt.ylabel('Number of Cart Abandonments')
plt.show()

# Segment customers by cart abandonment for delivery time < 10 minutes
cart_abandonment_under_10 = df[(df['Cart_Abandonment_Flag'] == 1) & (df['Delivery_Time_mins'] < 10)].shape[0]

# Print the result
print("\nCart Abandonment for Delivery Time < 10 minutes:", cart_abandonment_under_10)

# Plotting Cart Abandonment for Delivery Time < 10 minutes
plt.figure(figsize=(10, 6))
plt.bar(['< 10 mins'], [cart_abandonment_under_10], color='blue')
plt.title('Cart Abandonment for Delivery Time < 10 minutes')
plt.ylabel('Number of Cart Abandonments')
plt.show() 
if cart_abandonment_under_10 == 0:
    print("\nNo Cart Abandonment for Delivery Time < 10 minutes")

"""


# Personalized product recommendations based on insights

# Function to recommend products based on age group
def recommend_products_by_age(age_group):
    recommended_products = df[df['Age_Group'] == age_group]['Product_Category'].value_counts().index.tolist()
    return recommended_products

# Function to recommend products based on gender
def recommend_products_by_gender(gender):
    recommended_products = df[df['Gender'] == gender]['Product_Category'].value_counts().index.tolist()
    return recommended_products

# Function to recommend products based on city
def recommend_products_by_city(city):
    recommended_products = df[df['City'] == city]['Product_Category'].value_counts().index.tolist()
    return recommended_products

""""
# Example usage
if __name__ == "__main__":
    age_group = '41-60'
    gender = 'Male'
    city = 'Bangalore'
    
    age_recommendations = recommend_products_by_age(age_group)
    gender_recommendations = recommend_products_by_gender(gender)
    city_recommendations = recommend_products_by_city(city)
    
    print(f"\nRecommended Products for Age Group {age_group}:")
    print(age_recommendations)
    print(f"\nRecommended Products for Gender {gender}:")
    print(gender_recommendations)
    print(f"\nRecommended Products for City {city}:")
    print(city_recommendations)
"""
