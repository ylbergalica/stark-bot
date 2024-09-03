import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

import re
import time

load_dotenv()

king_triggers = ["king", "mbret", "mret", "kral"]

cooldown_seconds = 1  # Set cooldown period in seconds
cooldowns = {}

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
	
	current_time = time.time()
	user_id = message.author.id

	# check if user is on cooldown
	if user_id in cooldowns:
		last_triggered = cooldowns[user_id]
		if current_time - last_triggered < cooldown_seconds:
			return

	# check for king words
	if any(re.search(rf'(^|\W){word}(\W|$)', message.content.lower()) for word in king_triggers):
		await message.reply('KING IN THE NORTH!!')
		cooldowns[user_id] = current_time  # update last use

	await bot.process_commands(message)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
