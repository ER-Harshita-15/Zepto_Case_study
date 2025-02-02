import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

class DeliveryInsights:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        # self.df['Delivery_Time_mins'] = pd.to_datetime(self.df['Delivery_Time_mins'])
        self.plots_dir = 'plots'
        os.makedirs(self.plots_dir, exist_ok=True)

    def calculate_average_delivery_time(self):
        self.grouped_data = self.df.groupby(['City', 'Product_Category']).agg({
            'Delivery_Time_mins': 'mean'
        }).reset_index()
        self.grouped_data.rename(columns={'Delivery_Time_mins': 'average_delivery_time'}, inplace=True)

    def plot_average_delivery_time(self):
        plt.figure(figsize=(14, 7))
        sns.barplot(data=self.grouped_data, x='City', y='average_delivery_time', hue='Product_Category')
        plt.title('Average Delivery Time by City and Product Category')
        plt.xlabel('City')
        plt.ylabel('Average Delivery Time (minutes)')
        plt.legend(title='Product Category')
        plt.savefig(os.path.join(self.plots_dir, 'average_delivery_time.png'))
        plt.close()

if __name__ == "__main__":
    insights = DeliveryInsights('..\\Data\\updated_dataset.csv')
    insights.calculate_average_delivery_time()
    insights.plot_average_delivery_time()