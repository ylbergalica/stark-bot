import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

king_triggers = ["king", "mbret", "mret", "kral"]

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	# check for king words
	if any(word in message.content.lower() for word in king_triggers):
		await message.reply('KING IN THE NORTH!!')

	await bot.process_commands(message)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
