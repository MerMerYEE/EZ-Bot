import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
import re


client = commands.Bot(command_prefix = '.', help_command=None)

status = cycle(['NACL', 'NACL과 함께 개발중'])

@client.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('')
