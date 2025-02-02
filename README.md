# README

**Warning: This README is AI-generated.**

## Discord Quote Bot

This is a simple Discord bot that sends a daily quote to a Discord channel using a webhook.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/discord-quote-bot.git
    cd discord-quote-bot
    ```

2. Create a `.env` file in the project folder with the following content:
    ```
    DISCORD_WEBHOOK_URL=your_discord_webhook_url
    ```

3. Install the required dependencies:
    ```sh
    pip install dot_env
    ```
    Alternatively, you can set the `DISCORD_WEBHOOK_URL` environment variable directly in your shell:
    ```sh
    export DISCORD_WEBHOOK_URL=your_discord_webhook_url
    ```

## Usage

Run the bot:
```sh
python app.py
```