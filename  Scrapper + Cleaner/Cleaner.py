import pandas as pd

def remove_duplicates(input_csv, Cleaned_News):
    df = pd.read_csv(input_csv)
    df_cleaned = df.drop_duplicates()
    df_cleaned.to_csv(Cleaned_News, index=False)
    print(f"Removed duplicates. Cleaned file saved as {Cleaned_News}")

input_csv = '/Users/shivamkumarkaushik/Desktop/StockHawk/Scrapper/News.csv'  
Cleaned_News = '/Users/shivamkumarkaushik/Desktop/StockHawk/Scrapper/News(Cleaned).csv'  # Replace with your desired output CSV file path

remove_duplicates(input_csv, Cleaned_News)
