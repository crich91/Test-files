import discord
from discord.ext import commands
import asyncio

class Destiny2:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True,
                      aliases=['xur', 'WheresXur', 'Wheres_Xur', 'wheresxur', 'whereisxur'],
                      description= 'This will eventually tell you where Xur (AKA Destiny Sanata) will be on weekends....maybe')
    async def Xur(self, ctx):
        await self.client.say("Where is Xur Today?")
        await self.client.say("No idea, this module isnt programmed yet....")


def setup(client):
    client.add_cog(Destiny2(client))
