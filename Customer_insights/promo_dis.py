import pandas as pd
from Recommender import recommend_products_for_customer
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('updated_dataset.csv')

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
    
    # Get product recommendations based on customer preferences
    recommended_products, product_categories, customer_city = recommend_products_for_customer(customer_id)[:3]
    
    # Design promotions and discounts based on demographics and purchasing behavior
    promotions = {}
    for product, category in zip(recommended_products, product_categories):
        if gender == 'Female' and category == 'Groceries':
            promotions[product] = '15% off'
        elif age_group == '18-25' and category == 'Electronics':
            promotions[product] = '20% off'
        elif city == customer_city:
            promotions[product] = '10% off'
        elif loyalty_tier == 'Gold':
            promotions[product] = '25% off'
        elif high_spender_flag == 1:
            promotions[product] = '30% off'
        elif product not in promotions:
            promotions[product] = '5% off'
    return promotions

# Example usage
customer_id = 'ZP_CUST4000'
promotions = design_promotions_and_discounts(customer_id)
if promotions:
    print(f"\nTargeted Promotions and Discounts for Customer ID {customer_id}:")
    print(promotions)
else:
    print(f"No promotions available for Customer ID {customer_id}")

# Convert promotions dictionary to DataFrame for tabular display
promotions_df = pd.DataFrame(list(promotions.items()), columns=['Product', 'Discount'])

# Display the promotions in tabular form
print("\nTargeted Promotions and Discounts for Customer ID {}:".format(customer_id))
print(promotions_df)

# Plotting the promotions
plt.figure(figsize=(12, 8))
promotions_df['Discount'] = promotions_df['Discount'].str.replace('% off', '').astype('float')
promotions_df.set_index('Product')['Discount'].plot(kind='bar', color='skyblue')
plt.title('Targeted Promotions and Discounts')
plt.xlabel('Product')
plt.ylabel('Discount (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

