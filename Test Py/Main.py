import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

extentions = ['Test_COGS', 'Destiny_COGS']

@client.event
async def on_ready():
    print('Bot is ready')


@client.command(pass_context=True, aliases=['simonsays', 'simon says'])
async def SimonSays(ctx):
    phrase = ctx.message.content
    printsentence= phrase.partition(' ')[2]
    await client.say(printsentence)

if __name__ == '__main__':
    for extention in extentions:
        try:
            client.load_extension(extention)
        except Exception as error:
            print('{} cannont be loaded. {}'.format(extention, error))

    client.run("{}".format(os.environ.get('CHAT')))
