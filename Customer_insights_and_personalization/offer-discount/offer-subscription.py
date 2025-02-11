import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Preload dataset
DATASET_PATH = "..\\..\\Data\\updated_dataset.csv"  # Ensure this file exists in the working directory

def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    df.dropna(inplace=True)
    return df

class SubscriptionOffer:
    def __init__(self, df):
        self.df = df
        self.label_encoders = {}
        self._encode_features()
        self.product_features = self._create_product_features()
        self.product_similarity_df = self._calculate_similarity()

    def _encode_features(self):
        for column in ['Gender', 'City', 'Product_Category', 'Payment_Method', 'Age_Group', 'Loyalty_Tier', 'High_Spender_Flag']:
            le = LabelEncoder()
            self.df[column] = le.fit_transform(self.df[column])
            self.label_encoders[column] = le

    def _create_product_features(self):
        product_features = self.df[['Product_ID', 'Product_Category', 'Price', 'Competitor_Price', 'Ad_Click_Through_Rate', 'Browsing_Time_mins', 'Voice_Search_Count', 'Visual_Search_Count']].drop_duplicates().set_index('Product_ID')
        product_features.iloc[:, 1:] = product_features.iloc[:, 1:].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
        return product_features

    def _calculate_similarity(self):
        product_similarity = cosine_similarity(self.product_features)
        return pd.DataFrame(product_similarity, index=self.product_features.index, columns=self.product_features.index)

    def analyze_customer_behavior(self, customer_id):
        customer_data = self.df[self.df['Customer_ID'] == customer_id]
        if customer_data.empty:
            return None, None, None, None, None, None, None

        customer_city = self.label_encoders['City'].inverse_transform([customer_data['City'].iloc[0]])[0]
        customer_age_group = self.label_encoders['Age_Group'].inverse_transform([customer_data['Age_Group'].iloc[0]])[0]
        loyalty_tier = self.label_encoders['Loyalty_Tier'].inverse_transform([customer_data['Loyalty_Tier'].iloc[0]])[0]
        high_spender = customer_data['High_Spender_Flag'].iloc[0]
        gender = self.label_encoders['Gender'].inverse_transform([customer_data['Gender'].iloc[0]])[0]
        preferred_categories = customer_data['Product_Category'].value_counts().index.tolist()
        preferred_categories = self.label_encoders['Product_Category'].inverse_transform(preferred_categories)
        purchase_frequency = customer_data['Order_Time'].nunique()
        
        return customer_city, customer_age_group, preferred_categories, purchase_frequency, loyalty_tier, high_spender, gender

    def create_subscription_plans(self, preferred_categories, purchase_frequency, loyalty_tier, high_spender, gender):
        base_prices = {'Monthly Plan': 199, 'Quarterly Plan': 499, 'Annual Plan': 799}
        discounts = {'gold': 0.4, 'silver': 0.25, 'bronze': 0.15}
        extra_discount = 0.2 if high_spender else 0.0
        gender_discounts = {'Male': 0.1, 'Non-Binary': 0.0}
        gender_delivery = {'Female': 'Free delivery on groceries for every plan',
                           'Non-Binary': 'Free delivery on monthly subscription for all purchases'}

        discount = discounts.get(loyalty_tier.lower(), 0) + extra_discount
        subscription_plans = []

        for plan_name, base_price in base_prices.items():
            final_price = base_price * (1 - discount)
            benefits = []

            if gender == 'Male' and (plan_name == 'Annual Plan' or plan_name == 'Quarterly Plan'):
                final_price *= (1 - gender_discounts['Male'])
                benefits.append('10% discount on Annual and Quarterly plans')

            if gender in gender_delivery:
                if gender == 'Female':
                    benefits.append('Free delivery on groceries for every plan')
                elif gender == 'Non-Binary' and plan_name == 'Monthly Plan':
                    benefits.append('Free delivery on monthly subscription for all purchases')

            plan = {
                'name': plan_name,
                'description': f'{plan_name} with priority on preferred products.',
                'products': preferred_categories[:5],
                'frequency': plan_name.split()[0],
                'price': round(final_price, 2),
                'benefits': benefits
            }
            subscription_plans.append(plan)

        return subscription_plans

# Load dataset
st.title("Customer Subscription Plans")
df = load_dataset()
subscription_offer = SubscriptionOffer(df)

customer_id = st.text_input("Enter Customer ID:", "ZP_CUST4000", key="subscription_customer_id")

if st.button("Get Subscription Plans", key="subscription_plans"):
    customer_city, customer_age_group, preferred_categories, purchase_frequency, loyalty_tier, high_spender, gender = subscription_offer.analyze_customer_behavior(customer_id)
    
    if not preferred_categories:
        st.warning("No data found for this customer ID. Please check the ID and try again.")
    else:
        st.subheader("Customer Details")
        st.write(f"**Customer ID:** {customer_id}")
        st.write(f"**Customer City:** {customer_city}")
        st.write(f"**Customer Age Group:** {customer_age_group}")
        st.write(f"**Loyalty Tier:** {loyalty_tier}")
        st.write(f"**High Spender:** {'Yes' if high_spender else 'No'}")
        st.write(f"**Gender:** {gender}")
        
        st.subheader("Subscription Plans")
        subscription_plans = subscription_offer.create_subscription_plans(preferred_categories, purchase_frequency, loyalty_tier, high_spender, gender)
        for plan in subscription_plans:
            st.write(f"### {plan['name']}")
            st.write(f"**Description:** {plan['description']}")
            st.write(f"**Products:** {', '.join(plan['products'])}")
            st.write(f"**Frequency:** {plan['frequency']}")
            st.write(f"**Price:** ₹{plan['price']}")
            if plan['benefits']:
                st.write(f"**Benefits:** {', '.join(plan['benefits'])}")
