import discord
from datetime import datetime
from discord.ext import commands
import asyncio

class Botinfo(commands.Cog):  
    def __init__(self, bot) -> None:
        self.bot =bot
    
    @commands.command()
    async def help(self, ctx, channel = None) :
        async with ctx.typing():
            await asyncio.sleep(0)
        # set title and description
        emBed = discord.Embed(title="Bot Information", description="All available bot commands(prefix: '!'>)", color=0x1F51FF)

        # set thumbnail and footer image
        emBed.set_thumbnail(url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        emBed.set_footer(text=f'{self.bot.user.name}',icon_url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        
        # add command infomation here
        emBed.add_field(name="help <channel's name or None>", value="Get help command", inline=False)
        emBed.add_field(name="say", value="Greeting to user", inline=False)
        emBed.add_field(name="weather", value="Send  today's weather infomations", inline=False)
        emBed.add_field(name="wforecast", value="Send weather forecast for tomorrow", inline=False)
        emBed.add_field(name="setlocation <location's name>", value="Set default location for weather report", inline=False)
        emBed.add_field(name="location", value="Send the default location", inline=False)
        emBed.add_field(name="toptrends", value="show most tweets topic in Twitter", inline=False)
        emBed.add_field(name="trending", value="show Twitter's trending topic", inline=False)
        emBed.add_field(name="news <topic>", value="search news", inline=False)
        
        # send command info
        if channel == None :
            await ctx.channel.send(embed=emBed)
            return

        # send in specific channels
        channel = discord.utils.get(ctx.guild.channels, name=channel)
        channel_id = channel.id
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed=emBed)



async def setup(bot) :
    await bot.add_cog(Botinfo(bot))