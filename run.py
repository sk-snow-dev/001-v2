import os
from bot import bot

# Load environment variables (optional, if using .env for token)
from dotenv import load_dotenv
load_dotenv()

# Get the bot token from the environment or replace with a hardcoded token
BOT_TOKEN = os.getenv("BOT_TOKEN")

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN is not set. Add it to your .env file or hardcode it.")
    else:
        bot.run(BOT_TOKEN)
