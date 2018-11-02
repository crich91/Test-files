import discord
from discord.ext import commands
import random

class COGS:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await self.client.say("pong")

    @commands.command(pass_context=True)
    async def pong(self, ctx):
        await self.client.say("ping")

    @commands.command(pass_context=True,
                      aliases=['simonsays', 'simon says'],
                      descrption='What do you think this does?')
    async def SimonSays(self, ctx):
        phrase = ctx.message.content
        printsentence= phrase.partition(' ')[2]
        await self.client.say(printsentence)

    @commands.command(pass_context=True,
                      aliases=['DontDoThisCommand', 'TheCommandOfRegret'],
                      description= 'Only Do This if you want to be annoying')
    async def DontUseThisCommand(self, ctx):
        await self.client.say("Oh no you did it now....")
        for i in range(50):
            await self.client.say(str(50 - i) + " Bottles of Beer on the Wall...Take one down pass it around...")

    @commands.command(pass_context=True,
                      aliases=['iloveyouchatbot', 'LoveYou', 'loveyou', 'iloveyou'],
                      description='so cute')
    async def I_Love_You_ChatBot(self, ctx):
        await self.client.say("{} I love you too".format(":kissing_heart:"))

    @commands.command(pass_context=True,
                      aliases = ['rps'])
    async def RPS(self, ctx):
        RPS = ['Rock',
               'Paper',
               'Scissors']
        await self.client.say(random.choice(RPS))

    @commands.command(pass_context=True,
                      aliases=['flip'])
    async def Flip(self, ctx):
        Coin = ['Heads', 'Tails']
        await self.client.say(random.choice(Coin))




def setup(client):
    client.add_cog(COGS(client))
