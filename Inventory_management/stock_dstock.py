import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import pandas as pd

# Load dataset automatically
DATA_PATH = "..\\Data\\updated_dataset.csv"
df = pd.read_csv(DATA_PATH)

# Streamlit title and instructions
st.title('Product Category Demand by City and Quarter')
st.markdown("""
This app displays the demand for product categories in a selected city and quarter,
along with the stock percentage for each category.
""")

# Check if necessary columns exist in the dataset
required_columns = ['Order_Time', 'City', 'Product_Category', 'Quantity']
if all(col in df.columns for col in required_columns):
    
    # Convert 'Order_Time' to datetime format
    df['Order_Time'] = pd.to_datetime(df['Order_Time'])

    # Extract month and map to quarters
    df['Month'] = df['Order_Time'].dt.month
    df['Quarter'] = df['Month'].apply(lambda x: f'Q{((x - 1) // 3) + 1}')

    # Group by City, Product_Category, and Quarter, then sum the Quantity
    quarterly_demand_by_city = df.groupby(['City', 'Product_Category', 'Quarter'])['Quantity'].sum().reset_index()

    # Display quarter and city selection
    st.sidebar.subheader("Select Filters")
    selected_city = st.sidebar.selectbox("Select City", df['City'].unique())
    selected_quarter = st.sidebar.selectbox("Select Quarter", ['Q1', 'Q2', 'Q3', 'Q4'])

    # Filter the data based on user selection
    filtered_data = quarterly_demand_by_city[
        (quarterly_demand_by_city['City'] == selected_city) & 
        (quarterly_demand_by_city['Quarter'] == selected_quarter)
    ]

    if not filtered_data.empty:
        # Calculate total demand for the selected city and quarter
        total_demand = filtered_data['Quantity'].sum()

        # Calculate the percentage of demand for each product category
        filtered_data['Stock_Percentage'] = ((filtered_data['Quantity'] / total_demand) * 100).round(2)

        # Display the filtered result with the stock percentage
        st.subheader(f"Demand for {selected_city} in {selected_quarter}")
        st.dataframe(filtered_data)

        # Optional: Allow downloading the filtered result as CSV
        st.download_button(
            label="Download Data as CSV",
            data=filtered_data.to_csv(index=False),
            file_name=f"demand_{selected_city}_{selected_quarter}_with_stock_percentage.csv",
            mime="text/csv"
        )
    else:
        st.warning(f"No data found for {selected_city} in {selected_quarter}")
else:
    st.error(f"Dataset must contain the following columns: {', '.join(required_columns)}")
