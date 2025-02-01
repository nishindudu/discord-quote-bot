import requests
import os


url = os.environ.get("DISCORD_WEBHOOK_URL")
quote_url = "https://zenquotes.io/api/today"

hello_world_data = {
    "content": "Hello, World!",
    "username": "Hello Bot"
}

quote = requests.get(quote_url)

if quote.status_code == 200:
    quote_data = quote.json()
    quote_content = quote_data[0]["q"]
    
    quote_data = {
        "content": quote_content,
        "username": "Quote Bot"
    }


result = requests.post(url, json=quote_data)

try:
    result.raise_for_status()
    print("Message sent successfully")
except requests.exceptions.HTTPError as err:
    print(f"An error occurred: {err}")
