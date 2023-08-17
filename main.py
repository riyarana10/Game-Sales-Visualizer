import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class GameSalesVisualizer:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = pd.read_csv(self.data_file)

    def clean_data(self):
        self.df_cleaned = self.df.dropna()
        cleaned_file = 'cleaned_' + self.data_file
        self.df_cleaned.to_csv(cleaned_file, index=False)
        self.new_df = pd.read_csv(cleaned_file)

    def plot_number_of_games_released_by_year(self):
        temp = sns.countplot(x='Year', data=self.new_df)
        for bars in temp.containers:
            temp.bar_label(bars)
        plt.show()

    def plot_genre_sales_in_na(self):
        ax = sns.barplot(x='Genre', y='NA_Sales', data=self.new_df)
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.show()
        
    # comparing total global sales for diffrent genres
    def plot_genre_sales_globally(self):
        genre_sales = self.new_df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 6))
        genre_sales.plot(kind='bar', color='skyblue')
        plt.xlabel('Genre')
        plt.ylabel('Global Sales (millions)')
        plt.title('Total Global Sales by Genre')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.show()
        
    # 
    def plot_region_sales(self):
        region_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
        region_names = ['North America', 'Europe', 'Japan', 'Other', 'Global']

        region_sales = self.new_df[region_columns].sum()

        plt.figure(figsize=(10, 6))
        plt.bar(region_names, region_sales, color=['skyblue', 'lightgreen','pink', 'purple', 'orange'])
        plt.xlabel('Region')
        plt.ylabel('Sales (millions)')
        plt.title('Sales by Region')
        plt.tight_layout()
        plt.show()
        
    def plot_publisher_sales(self):
        top_publishers = self.new_df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(12, 6))
        top_publishers.plot(kind='bar', color='orange')
        plt.xlabel('Publisher')
        plt.ylabel('Global Sales (millions)')
        plt.title('Top 10 Publishers by Global Sales')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    data_file = 'vgsales.csv'
    visualizer = GameSalesVisualizer(data_file)

    visualizer.clean_data()
    visualizer.plot_number_of_games_released_by_year()
    visualizer.plot_genre_sales_in_na()
    visualizer.plot_genre_sales_globally()
    visualizer.plot_region_sales()
    visualizer.plot_publisher_sales()


