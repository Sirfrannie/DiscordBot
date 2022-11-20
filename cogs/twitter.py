
import tweepy
import getenv
import json
import discord
from discord.ext import commands
import asyncio

# setup api 
api_key = getenv.get('api_key')
api_key_secret = getenv.get('api_key_secret')
access_token = getenv.get('access_token')
access_token_secret = getenv.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key= api_key,consumer_secret= api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth= auth)



def search_trends(woeid) :
    return api.get_place_trends(woeid)

def get_woeid():
    f = open('jsonFile\data.json',  'r+')
    data = json.load(f)
    f.close()

    return data['woeid']



class Twitter(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def toptrends(self,ctx) :
        async with ctx.typing():
            await asyncio.sleep(0)

        trends = search_trends(get_woeid())
        lstvollum = []
        lsttrends = []
        lstlink = []

        emBed = discord.Embed(title=f"Top Twitter Trends", description=f"", color=0x00acee)
        emBed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/124/124021.png')

        for i in trends[0]['trends'][::1]:
            if i["tweet_volume"] == None :
                continue

            else :
                lsttrends.append(i["name"])
                lstvollum.append(i["tweet_volume"])
                lstlink.append(i["url"])

        for i in range (len(lstvollum)) :
            for j in range (i) :
                if lstvollum[j] < lstvollum[i]:
                    lstvollum[j], lstvollum[i] = lstvollum[i], lstvollum[j]
                    lsttrends[j], lsttrends[i] = lsttrends[i], lsttrends[j]
                    lstlink[j], lstlink[i] = lstlink[i], lstlink[j]

        for i in range (10 if len(lstvollum) > 10 else len(lstvollum)) : 
            emBed.add_field(name=f"{i+1}.) {lsttrends[i]}   : {lstvollum[i]} tweets",value=f"link : {lstlink[i]}", inline=False)


        await ctx.channel.send(embed= emBed)



    @commands.command()
    async def trending(self,ctx) :
        async with ctx.typing():
            await asyncio.sleep(0)

        trends = search_trends(get_woeid())

        emBed = discord.Embed(title=f"Trending now.", description=f"", color=0x00acee)
        emBed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/124/124021.png')

        for i in range (10) : 
            emBed.add_field(name=f"{i+1}.) {trends[0]['trends'][i]['name']}   : {trends[0]['trends'][i]['tweet_volume']} tweets",value=f"link : {trends[0]['trends'][i]['url']}", inline=False)


        await ctx.channel.send(embed= emBed)


async def setup(bot) :
    await bot.add_cog(Twitter(bot))