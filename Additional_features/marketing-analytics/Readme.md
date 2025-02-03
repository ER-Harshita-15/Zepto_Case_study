# Marketing Analytics and Customer Acquisition

This repository contains two Python scripts, `AUDIENCE_TARGETING.PY` and `CUSTOMER_ACQUISITION.PY`, which perform marketing analytics and customer insights analysis respectively. Both scripts utilize Streamlit for creating interactive dashboards.

## Files

### 1. AUDIENCE_TARGETING.PY

This script performs marketing analytics on a dataset to provide insights for budget allocation and customer targeting.

#### Features:
- **Customer Acquisition Cost (CAC)**: Calculates the cost of acquiring a new customer.
- **Conversion Rate**: Determines the conversion rate based on the dataset.
- **Top-Selling Product Categories**: Identifies the top-selling product categories.
- **High-Performing Channels**: Analyzes the performance of different channels based on payment methods.
- **Age Distribution**: Provides insights into the age distribution of customers.
- **Suggested Budget Allocation**: Suggests budget allocation based on revenue share.

#### Usage:
1. Ensure the dataset file `..\\Data\\ZEPTO_ANALYTICS_DATASET.CSV` is in the same directory.
2. Run the script using Streamlit:
    ```bash
    streamlit run AUDIENCE_TARGETING.PY
    ```
3. Input the total marketing spend in the sidebar.
4. Select high-performing channels to filter the data.
5. View the results in the interactive dashboard.

### 2. CUSTOMER_ACQUISITION.PY

This script performs customer insights analysis based on channel-dependent data.

#### Features:
- **Customer Acquisition Cost (CAC)**: Calculates the cost of acquiring a new customer in both USD and INR.
- **Conversion Rate**: Determines the conversion rate based on unique visitors.
- **High-Performing Channels**: Identifies high-performing channels for customer acquisition.
- **Audience Targeting by Age Group**: Provides insights into the age distribution of customers.
- **Budget Allocation**: Suggests budget allocation to maximize ROI based on selected channels.

#### Usage:
1. Ensure the dataset file `ZEPTO_ANALYTICS_DATASET.CSV` is in the same directory.
2. Run the script using Streamlit:
    ```bash
    streamlit run CUSTOMER_ACQUISITION.PY
    ```
3. Input the total marketing spend in USD and the number of unique visitors in the sidebar.
4. Select high-performing channels to filter the data.
5. View the results in the interactive dashboard.

## Dataset

Both scripts use the `ZEPTO_ANALYTICS_DATASET.CSV` file, which should contain the following columns:
- `Customer_ID`
- `Product_Category`
- `Price`
- `Payment_Method`
- `Age`

## Requirements

- Python 3.12.6
- Streamlit
- Pandas

Install the required packages using:
```bash
pip install streamlit pandas
```

## Running the Scripts

To run the scripts, use the following commands in your terminal:
```bash
streamlit run AUDIENCE_TARGETING.PY
streamlit run CUSTOMER_ACQUISITION.PY
```

## Conclusion

These scripts provide valuable insights into marketing analytics and customer acquisition, helping businesses make informed decisions about budget allocation and customer targeting. The interactive dashboards created using Streamlit make it easy to visualize and analyze the data.
