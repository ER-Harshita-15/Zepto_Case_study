import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class RiderIncentiveAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.average_delivery_time = self.data['Delivery_Time_mins'].mean()

    def calculate_incentives(self, row):
        """Calculate incentives based on delivery time."""
        if row['Delivery_Time_mins'] <= self.average_delivery_time:
            incentives = 30  # Base incentive for low delivery time
            if row['Delivery_Time_mins'] < 8:
                incentives += 15  # Additional incentive for delivery time < 8 min
            elif row['Delivery_Time_mins'] < 9:
                incentives += 10  # Additional incentive for delivery time < 9 min
            return incentives
        else:
            return 0  # No incentives for high delivery time

    def apply_incentives(self):
        """Apply incentive calculation to each row in the dataset."""
        self.data['Incentives'] = self.data.apply(self.calculate_incentives, axis=1)

    def show_incentive_summary(self):
        """Display the summary of the incentives."""
        print(f'Average Delivery Time: {self.average_delivery_time:.2f} minutes')
        print(f'Incentive summary for the first few rows:')
        print(self.data[['Customer_ID', 'Delivery_Time_mins', 'Incentives']].head())

# Example usage
file_path = '..\\Data\\updated_dataset.csv'  # Update with the correct file path
analyzer = RiderIncentiveAnalyzer(file_path)

# Apply the incentives calculation
analyzer.apply_incentives()

# Show summary of incentives
analyzer.show_incentive_summary()
