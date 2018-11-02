import discord
from discord.ext import commands

class COGS:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await self.client.say("pong")

    @commands.command(pass_context=True)
    async def pong(self, ctx):
        await self.client.say("ping")

    @client.command(pass_context=True, aliases=['simonsays', 'simon says'])
    async def SimonSays(ctx):
        phrase = ctx.message.content
        printsentence= phrase.partition(' ')[2]
        await client.say(printsentence)

def setup(client):
    client.add_cog(COGS(client))
