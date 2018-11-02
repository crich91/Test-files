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

def setup(client):
    client.add_cog(COGS(client))






'''
@client.command(pass_context=True,
                aliases=["simonsays", "Simon Says"],
                description= "Say what I say.")
async def SimonSays(context):
    await client.say(context.message.author.mention + "," + context.message.content )
'''
