import discord
from discord.ext import commands
import asyncio
import requests, os, sys, time, json, urllib
from datetime import datetime

BungieURL = 'https://www.bungie.net'
URL_BASE = 'https://www.bungie.net/Platform'
pathXur = '/Advisors/Xur/'



class Destiny2:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True,
                      aliases=['xur', 'WheresXur', 'Wheres_Xur', 'wheresxur', 'whereisxur'],
                      description= 'This will eventually tell you where Xur (AKA Destiny Sanata) will be on weekends....maybe')
    async def Xur(self, ctx):
        url = url = URL_BASE + pathXur
        API_KEY =  os.environ.get('D2')
        headers = {'X-API-Key': API_KEY}
        session = requests.Session()
        print("Header: {}\n URL: {}\n API: {}\n".format(headers, url, API_KEY ))

        res = requests.get(url, headers=headers)

        print("Error Status: {}".format(response.json()['ErrorStatus']))

        await self.client.say("What does Xur Have Today?")
        await self.client.say("No idea, this module isnt programmed yet....")

        for saleItems in res.json()['Response']['data']['saleItemCategories']:
            mysaleItems= saleItem['saleItems']
            for myItem in mysaleItems:
                hashId = str(myItem['item']['itemHash'])



    @commands.command(pass_context=True,
                      aliases=['GTLU', 'gtlu'])
    async def GamerTagLookUp(self, ctx):
        await self.client.say("Starting Look Up")
        gamertagraw = str(ctx.message.content)
        gamertag = gamertagraw.partition(' ')[2]
        await self.client.say("Gamer Tag: {}".format(gamertag))

        url = "https://bungie.net/Platform/Destiny2/SearchDestinyPlayer/2/{}".format(gamertag)

        API_KEY =  os.environ.get('D2')
        headers = {'X-API-Key': API_KEY}
        session = requests.Session()

        await self.client.say("Pulling: {}".format(url))
        response = requests.get(url, headers=headers)


        await self.client.say("Error Status: {}".format(response.json()['ErrorStatus']))

        info = response.json()['Response']
        if info:
            for i in info:
                    await self.client.say("{}'s Membership ID is: {}".format(gamertag, i['membershipId']))
                    memberidraw = i['membershipId']
                    memberid = memberidraw
                    staturl = "https://bungie.net/Platform/Destiny2/2/Account/{}/Character/0/Stats".format(memberid)
                    await self.client.say("Pulling: {}".format(staturl))

                    statresponse = requests.get(staturl, headers=headers)
                    await self.client.say("Error Status: {}".format(statresponse.json()['ErrorStatus']))
                    stats = statresponse.json()['Response']
                    print(stats)




                    #await self.client.say(stats)
        else:
            await self.client.say("User Not Found.")





'''
        info = request.json()['Response']

        for member in info:
            if member[displaName] == gamertag:
                print (member['membershipId'])
'''
def setup(client):
    client.add_cog(Destiny2(client))
