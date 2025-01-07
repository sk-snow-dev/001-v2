import nextcord
import os
from nextcord.ext import commands
from chat import chatbot
from dotenv import load_dotenv # type: ignore
load_dotenv()

# Get the bot token from the environment or replace with a hardcoded token
TESTING_GUILD_ID = os.getenv("TESTING_GUILD_ID")


# Bot initialization
intents = nextcord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

@bot.slash_command(description="Chat with the bot", guild_ids=[TESTING_GUILD_ID])
async def chat(interaction: nextcord.Interaction, message: str):
    response = chatbot(message)
    await interaction.send(response)

@bot.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == bot.user:
        return

    # Get chatbot response and send it
    user_message = message.content
    response = chatbot(user_message)
    await message.channel.send(response)
