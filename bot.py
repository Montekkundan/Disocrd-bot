import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant


chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

# Variables
BOT_NAME = "Bro"
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

minecraft_server_url = "lightmc.fun" # this is just an example, and you should use your own minecraft server

bot_help_message = """
:: Bot Usage ::
`!b help`                   : shows help
"""

# Set the bot command prefix
bot = commands.Bot(command_prefix="!b")

# Executes when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

# Executes whenever there is an incoming message event
@bot.event
async def on_message(message):
    print(f'Guild: {message.guild.name}, User: {message.author}, Message: {message.content}')
    if message.author == bot.user:
        return

    if message.content == '!b help':
        await message.channel.send(bot_help_message)

    if message.content.startswith("!b"):
        response = chatbot.request(message.content[2:])
        await message.channel.send(response)


bot.run(DISCORD_TOKEN)