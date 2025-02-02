import pandas as pd

class WorkforceAllocation:
    def __init__(self, file_path):
        # Load the dataset
        self.data = pd.read_csv(file_path)
        
        # Assume the dataset has a column 'Order_Time' in the format 'HH:MM:SS'
        # Explicitly specify the datetime format and handle invalid values
        self.data['Order_Hour'] = pd.to_datetime(self.data['Order_Time'], format='%H:%M:%S', errors='coerce').dt.hour

        # Define peak and off-peak hours
        self.peak_hours = list(range(10, 14)) + list(range(18, 23))  # 11 AM to 3 PM and 6 PM to 10 PM
        self.off_peak_hours = list(set(range(24)) - set(self.peak_hours))  # Remaining hours

        # Categorize orders into peak and off-peak
        self.data['Peak_OffPeak'] = self.data['Order_Hour'].apply(lambda x: 'Peak' if x in self.peak_hours else 'Off-Peak')

    def calculate_orders(self):
        # Calculate the number of orders in peak and off-peak hours
        peak_orders = self.data[self.data['Peak_OffPeak'] == 'Peak'].shape[0]
        off_peak_orders = self.data[self.data['Peak_OffPeak'] == 'Off-Peak'].shape[0]

        return peak_orders, off_peak_orders

    def suggest_workforce(self):
        # Suggest workforce allocation
        peak_orders, off_peak_orders = self.calculate_orders()
        total_orders = self.data.shape[0]

        peak_percentage = peak_orders / total_orders
        off_peak_percentage = off_peak_orders / total_orders

        return peak_percentage, off_peak_percentage

    def display_results(self):
        peak_orders, off_peak_orders = self.calculate_orders()
        peak_percentage, off_peak_percentage = self.suggest_workforce()

        # Print the results
        print(f"Number of orders during peak hours: {peak_orders}")
        print(f"Number of orders during off-peak hours: {off_peak_orders}")

        print(f"Suggested workforce allocation:")
        print(f"Peak hours: {peak_percentage * 100:.2f}% of the workforce")
        print(f"Off-peak hours: {off_peak_percentage * 100:.2f}% of the workforce")

    @staticmethod
    def process_sample_data(sample_data):
        # Process the sample dataframe
        sample_data['Order_Hour'] = pd.to_datetime(sample_data['Order_Time'], format='%H:%M:%S', errors='coerce').dt.hour
        peak_hours = list(range(10, 14)) + list(range(18, 23))  # 11 AM to 3 PM and 6 PM to 10 PM
        sample_data['Peak_OffPeak'] = sample_data['Order_Hour'].apply(lambda x: 'Peak' if x in peak_hours else 'Off-Peak')

        # Calculate the number of orders in peak and off-peak hours for the sample dataframe
        sample_peak_orders = sample_data[sample_data['Peak_OffPeak'] == 'Peak'].shape[0]
        sample_off_peak_orders = sample_data[sample_data['Peak_OffPeak'] == 'Off-Peak'].shape[0]

        # Print the results for the sample dataframe
        print(f"Sample Data - Number of orders during peak hours: {sample_peak_orders}")
        print(f"Sample Data - Number of orders during off-peak hours: {sample_off_peak_orders}")

        # Suggest workforce allocation for the sample dataframe
        sample_total_orders = sample_data.shape[0]
        sample_peak_percentage = sample_peak_orders / sample_total_orders
        sample_off_peak_percentage = sample_off_peak_orders / sample_total_orders

        print(f"Sample Data - Suggested workforce allocation:")
        print(f"Peak hours: {sample_peak_percentage * 100:.2f}% of the workforce")
        print(f"Off-peak hours: {sample_off_peak_percentage * 100:.2f}% of the workforce")


# Example usage
file_path = '..\\Data\\updated_dataset.csv'
allocation = WorkforceAllocation(file_path)
allocation.display_results()

# Process a sample dataframe
sample_data = pd.DataFrame({
    'Order_Time': ['10:00:00', '12:30:00', '14:45:00', '19:00:00', '19:15:00', '21:30:00', '23:00:00']
})
WorkforceAllocation.process_sample_data(sample_data)
