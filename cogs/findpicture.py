import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


class PictureFinding(commands.Cog) :
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def pic(self, ctx,*,keyword) :
        
        # set up embed
        emBed = discord.Embed(title=f"", description=f"", color=0x1F51FF)
        
        url = f"https://www.google.com/search?q={keyword}+icon&source=lnms&tbm=isch"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img') 

        # set picture to embed and then send to text channel
        for i in range (1,4) :
            if i >= len(images)- 2 : break # stop the loop if picture index out of list
            emBed.set_image(url=images[i]['src'])
            await ctx.channel.send(embed= emBed)
    

async def setup(bot):
    await bot.add_cog(PictureFinding(bot))