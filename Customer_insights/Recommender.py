import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv('updated_dataset.csv')
df.dropna(inplace=True)

# Encode categorical features
label_encoders = {}
for column in ['Gender', 'City', 'Product_Category', 'Payment_Method', 'Age_Group', 'Loyalty_Tier']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Create a feature matrix for products
product_features = df[['Product_ID', 'Product_Category', 'Price', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Browsing_Time_mins', 'Voice_Search_Count', 'Visual_Search_Count']].drop_duplicates().set_index('Product_ID')

# Normalize numerical features
product_features[['Price', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Browsing_Time_mins', 'Voice_Search_Count', 'Visual_Search_Count']] = product_features[['Price', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Browsing_Time_mins', 'Voice_Search_Count', 'Visual_Search_Count']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

# Calculate cosine similarity between products
product_similarity = cosine_similarity(product_features)
product_similarity_df = pd.DataFrame(product_similarity, index=product_features.index, columns=product_features.index)

# Function to recommend products based on a given product
def recommend_products(product_id, num_recommendations=5):
    similar_products = product_similarity_df[product_id].sort_values(ascending=False).head(num_recommendations + 1).index.tolist()
    similar_products.remove(product_id)
    return similar_products

# Function to recommend products based on customer preferences
def recommend_products_for_customer(customer_id, num_recommendations=5):
    customer_data = df[df['Customer_ID'] == customer_id]
    customer_city_encoded = customer_data['City'].iloc[0]
    customer_city = label_encoders['City'].inverse_transform([customer_city_encoded])[0]
    customer_age_group_encoded = customer_data['Age_Group'].iloc[0]
    customer_age_group = label_encoders['Age_Group'].inverse_transform([customer_age_group_encoded])[0]
    
    recommended_products = set()
    for product_id in customer_data['Product_ID']:
        recommended_products.update(recommend_products(product_id, num_recommendations))
    recommended_products = list(recommended_products)[:num_recommendations]
    
    # Get product categories for the recommended products
    recommended_product_categories = df[df['Product_ID'].isin(recommended_products)][['Product_ID', 'Product_Category']].drop_duplicates(subset=['Product_ID'])
    recommended_product_categories['Product_Category'] = label_encoders['Product_Category'].inverse_transform(recommended_product_categories['Product_Category'])
    
    return recommended_products, recommended_product_categories['Product_Category'].tolist(), customer_city, customer_age_group


# Example usage
if __name__ == "__main__":
    customer_id = 'ZP_CUST4000'
    customer_recommendations, product_categories, customer_city, customer_age_group = recommend_products_for_customer(customer_id)
    print(f"\nRecommended Products for Customer ID {customer_id} from City {customer_city} and Age Group {customer_age_group}:")
    print(customer_recommendations)
    print("\nProduct Categories of Recommended Products:")
    print(product_categories)
    