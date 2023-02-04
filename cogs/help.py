import discord
from datetime import datetime
from discord.ext import commands
import asyncio
import json

with open('jsonFile\commands.json', "r+") as f :
        data = json.load(f)

class Botinfo(commands.Cog):  
    def __init__(self, bot) -> None:
        self.bot =bot
    
    @commands.command()
    async def help(self, ctx, channel = None) :
        async with ctx.typing():
            await asyncio.sleep(0)
        # set title and description
        emBed = discord.Embed(title="Bot Information", description="All available bot commands (prefix: '!') ", color=0x1F51FF)

        # set thumbnail and footer image
        emBed.set_thumbnail(url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        emBed.set_footer(text=f'{self.bot.user.name}',icon_url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        emBed.add_field(name=f"--------------------", value = "",inline=False)

        # add command infomation here
        for commands in data['main'] :
            emBed.add_field(name=commands['command'], value=commands['info'], inline=False)

        # send command info
        if channel == None :
            await ctx.channel.send(embed=emBed)
            return

        # send in specific channels
        channel = discord.utils.get(ctx.guild.channels, name=channel)
        channel_id = channel.id
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed=emBed)

    # more commands of music player
    @commands.command()
    async def musichelp(self, ctx, channel = None) :
        async with ctx.typing():
            await asyncio.sleep(0)

        emBed = discord.Embed(title="music player commands", color=0x1F51FF)

        emBed.set_thumbnail(url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        emBed.set_footer(text=f'{self.bot.user.name}',icon_url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        emBed.add_field(name=f"--------------------", value = "",inline=False)

        for commands in data['music'] :
            emBed.add_field(name=commands['command'], value=commands['info'], inline=False)

        if channel == None :
            await ctx.channel.send(embed=emBed)
            return

        channel = discord.utils.get(ctx.guild.channels, name=channel)
        channel_id = channel.id
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed=emBed)

    # more commands of weather report function
    @commands.command()
    async def whelp(self, ctx, channel = None) :
        async with ctx.typing():
            await asyncio.sleep(0)

        emBed = discord.Embed(title="commands for weather function", color=0x1F51FF)

        emBed.set_thumbnail(url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        emBed.set_footer(text=f'{self.bot.user.name}',icon_url='https://img-9gag-fun.9cache.com/photo/aKx3dL6_460s.jpg')
        emBed.add_field(name=f"--------------------", value = "",inline=False)

        for commands in data['weather'] :
            emBed.add_field(name=commands['command'], value=commands['info'], inline=False)

        if channel == None :
            await ctx.channel.send(embed=emBed)
            return

        channel = discord.utils.get(ctx.guild.channels, name=channel)
        channel_id = channel.id
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed=emBed)

        



async def setup(bot) :
    await bot.add_cog(Botinfo(bot))