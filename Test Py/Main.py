import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix= "!")

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    Auth = message.author
    if message.content == "Hello":
        await client.send_message(Auth, "Hey There!")

@client.command(pass_context=True)
async def HelloWorld(ctx):
    Auth = ctx.message.author
    await client.send_message(Auth, 'You Rang?')

client.run("NTA2NjQ2ODM0MTU3MTkxMjE4.DroDnA.xFwrjkdl9bGBDu1JAhGQOn-IpWw")
