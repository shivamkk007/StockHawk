from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os

# Function to check if file exists
def file_exists(file_path):
    return os.path.isfile(file_path)

# Today's date formatted as dd/mm/yyyy
today = datetime.today().date()
formatted_date = today.strftime('%d/%m/%Y')

stocks = []
news = []

page = requests.get("https://groww.in/insights/stocks-in-news")
soup = BeautifulSoup(page.content, 'html.parser')

# Scraping stocks
a_tags = soup.find_all('a', class_='contentAccent headingLarge')
for tag in a_tags:
    stocks.append(tag.text.strip())

# Scraping news
news_texts = soup.find_all('div', class_='sinc22Description bodyLarge')
for text in news_texts:
    news.append(text.text.strip())

# Creating DataFrame
news_df = pd.DataFrame({
    'Stock': stocks,
    'News': news,
    'Date': formatted_date
})

# CSV file path
csv_file = '/Users/shivamkumarkaushik/Desktop/StockHawk/Scrapper/News.csv'

# Check if file exists to decide whether to add headers or not
write_headers = not file_exists(csv_file)

# Append data to CSV file
news_df.to_csv(csv_file, mode='a', index=False, header=write_headers)

print("Data saved to 'News.csv'")


from twilio.rest import Client
import datetime

# Twilio Account SID and Auth Token
account_sid = '*******'
auth_token = '*******'

# Twilio WhatsApp number and recipient WhatsApp number
twilio_number = 'whatsapp:+********'  # Use your Twilio WhatsApp number
your_number = 'whatsapp:+*********'  # Use your verified WhatsApp number

# Current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Message content
message = f"Your Scraping Script Ran Successfully at {current_time}."

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# Send WhatsApp message
message = client.messages.create(body=message, from_=twilio_number, to=your_number)

# print(f"WhatsApp notification sent to {your_number}. Message SID: {message.sid}")

