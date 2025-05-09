# Learn : Discord Quote Bot

This document explains the purpose of the bot, how to set it up, and how to use it.

---

## 1. Overview
The Discord Quote Bot is a simple Python script that fetches today's quote from the ZenQuotes API and sends it to a Discord webhook. It uses the requests library to get quotes and to post it to the Discord channel.
It's best to set up a cron job to run the script at regular intervals.

---

## 2. Key Components

### a. ZenQuotes API
- The bot fetches today's quote from the ZenQuotes API using the requests library.
- The API returns a JSON response containing the quote.

### b. Discord Webhook
- The bot sends the fetched quote to a Discord channel using a webhook URL.
- Webhooks can be set up in Discord to allow external applications to send messages to a channel.
- This script uses the requests library to send a POST request to the Discord webhook URL with the quote as the message content.

### c. Environment Variables
- The webhook URL is stored in an environment variable for security reasons. It's accessed using the dotenv library.

---

## 3. How It Works

1. The script imports the necessary libraries: requests, os, and dotenv.
2. It loads the environment variables from a `.env` file using the dotenv library.
3. It fetches the webhook URL from the environment variables.
4. It makes a GET request to the ZenQuotes API to fetch today's quote.
5. It checks if the response is successful (status code 200).
6. If successful, it extracts the quote and author from the JSON response.
7. It constructs a message string with the quote and author.
8. It sends a POST request to the Discord webhook URL with the message as the content.
9. It checks if the response from the webhook is successful.
10. If successful, it prints a success message; otherwise, it prints an error message.

---

## 4. Resources
- [ZenQuotes API Documentation](https://docs.zenquotes.io/zenquotes-documentation/)
- [Discord Webhooks Documentation](https://discord.com/developers/docs/resources/webhook)
- [Python Requests Library Documentation](https://docs.python-requests.org/en/latest/)
- [Python Dotenv Library Documentation](https://pypi.org/project/python-dotenv/)