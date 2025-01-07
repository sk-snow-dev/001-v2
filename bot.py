import nextcord
from nextcord.ext import commands
from chat import chatbot

# Configuration
TESTING_GUILD_ID = 1326191744022482954  # Replace with your guild ID

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

@bot.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == bot.user:
        return

    # Get chatbot response and send it
    user_message = message.content
    response = chatbot(user_message)
    await message.channel.send(response)
