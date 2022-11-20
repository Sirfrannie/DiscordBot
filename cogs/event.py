import discord
from discord.ext import commands

class event(commands.Cog) :
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) :
        activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
        await self.bot.change_presence(status=discord.Status.online, activity=activity)
        print (f"bot is running as {self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self, message) :
        greeting = ['Hi', 'hi', 'Hello', 'hello']
        if message.content in greeting  :
            await message.reply(f"Hello {message.author.name} ")


    @commands.command()
    async def say(self,ctx) :
        await ctx.reply(f"Hello {ctx.author.name}")

async def setup(bot) :
    await bot.add_cog(event(bot))