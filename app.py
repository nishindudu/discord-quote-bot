import requests
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/discord-quote-bot')
load_dotenv(os.path.join(project_folder, '.env'))

url = os.getenv("DISCORD_WEBHOOK_URL")
quote_url = "https://zenquotes.io/api/today" #URL to get quote from

# Test data. Not used as the quote is fetched from zenquotes.io
hello_world_data = {
    "content": "Hello, World!",
    "username": "Hello Bot"
}

quote = requests.get(quote_url) #get quote from zenquotes.io

if quote.status_code == 200:
    quote_data = quote.json()
    quote_content = quote_data[0]["q"]
    
    quote_data = {
        "content": quote_content,
        "username": "Quote Bot"
    }


result = requests.post(url, json=quote_data) #send quote to discord webhook

# Check if the request was successful
try:
    result.raise_for_status()
    print("Message sent successfully")
except requests.exceptions.HTTPError as err:
    print(f"An error occurred: {err}")
