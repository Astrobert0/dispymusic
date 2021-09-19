from pathlib import PurePath
import discord
import os

from discord.channel import VoiceChannel
from discord.ext import commands
from discord.ext.commands import bot


directory = os.path.dirname(__file__)
rel_path = "discord_token.txt"
abs_file_path = PurePath(directory, rel_path)

with open(abs_file_path, 'r') as file:
    token = file.read()
client =discord.Client()

class voice(commands.Cog):

    @commands.command()
    async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    @commands.command()
    async def leave(ctx):
        await ctx.voice_client.disconnect()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith('@hello'):
        await message.channel.send('howdy')

    elif message.content.startswith('@join'):
        await voice.join(client)
    elif message.content.startswith('@stop'):
        await voice.leave(client)
client.run(token)
