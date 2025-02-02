import pandas as pd
from Recommender import recommend_products_for_customer, label_encoders

# Load the dataset
df = pd.read_csv('updated_dataset.csv')
df.dropna(inplace=True)

# Encode categorical columns
for column in ['City', 'Age_Group', 'Gender', 'Loyalty_Tier']:
    df[column] = label_encoders[column].transform(df[column])

# Function to design targeted promotions and discounts
def design_promotions(customer_id):
    promotions = {}
    customer_data = df[df['Customer_ID'] == customer_id]
    customer_city_encoded = customer_data['City'].iloc[0]
    customer_city = label_encoders['City'].inverse_transform([customer_city_encoded])[0]
    customer_age_group_encoded = customer_data['Age_Group'].iloc[0]
    customer_age_group = label_encoders['Age_Group'].inverse_transform([customer_age_group_encoded])[0]
    customer_gender_encoded = customer_data['Gender'].iloc[0]
    customer_gender = label_encoders['Gender'].inverse_transform([customer_gender_encoded])[0]
    customer_loyalty_tier_encoded = customer_data['Loyalty_Tier'].iloc[0]
    customer_loyalty_tier = label_encoders['Loyalty_Tier'].inverse_transform([customer_loyalty_tier_encoded])[0]
    high_spender_flag = customer_data['High_Spender_Flag'].iloc[0]

    recommended_products, product_categories, _, _ = recommend_products_for_customer(customer_id)

    for product, category in zip(recommended_products, product_categories):
        if customer_gender == 'Female' and category == 'Groceries':
            promotions[product] = '15% off'
        elif customer_age_group == '18-25' and category == 'Electronics':
            promotions[product] = '20% off'
        elif customer_city == customer_city:
            promotions[product] = '10% off'
        elif customer_loyalty_tier == 'Gold':
            promotions[product] = '25% off'
        elif high_spender_flag == 1:
            promotions[product] = '30% off'
        elif product not in promotions:
            promotions[product] = '5% off'

    return promotions

# Example usage
if __name__ == "__main__":
    customer_id = 'ZP_CUST4000'
    promotions = design_promotions(customer_id)
    print(f"\nPromotions for Customer ID {customer_id}:")
    for product, discount in promotions.items():
        print(f"Product ID: {product}, Discount: {discount}")