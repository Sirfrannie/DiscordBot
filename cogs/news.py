from GoogleNews import GoogleNews
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import asyncio

gnew = GoogleNews()
gnew.set_lang('US')


class news(commands.Cog) :

    def __init__(self, bot) :
        self.bot = bot
        self.image_links = []
        self.tmbn_links = []

    @commands.command()
    async def news(self, ctx, *, keyword) :
        
        async with ctx.typing():
            await asyncio.sleep(0)
        
        gnew.search(keyword)
        res = gnew.results()

        # get image topic
        for i in range (5) :
            url = f"https://www.google.com/search?q={res[i]['title']}&source=lnms&tbm=isch"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            images = soup.find_all('img')
            self.image_links.append(images[1]['src'])

        # get link of news for use to search
        for i in range (5) :
            url = f"https://www.google.com/search?q={res[i]['media']}+icon&source=lnms&tbm=isch"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            images = soup.find_all('img')
            self.tmbn_links.append(images[1]['src'])

        # set up embed and then send to discord channel
        for i in range (5) :
            emBed = discord.Embed(title=f"{res[i]['title']}", description=f"{res[i]['desc']}", color=0x1F51FF)
            emBed.set_image(url=self.image_links[i])
            emBed.set_thumbnail(url=self.tmbn_links[i])
            emBed.add_field(name=f"media : {res[i]['media']}",value=f"source : {res[i]['link']}", inline=False)
            emBed.set_footer(text=f"date: {str(res[i]['datetime'])[:19]}  ( {res[i]['date']} )")
            
            msg = await ctx.channel.send(embed= emBed)

            if i == 4 :
                await msg.add_reaction("👍")

        # clear all data in each List
        gnew.clear()
        self.image_links.clear()
        self.tmbn_links.clear()


async def setup(bot):
    await bot.add_cog(news(bot))
