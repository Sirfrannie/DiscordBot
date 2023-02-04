import discord
from discord.ext import commands
import getenv
import asyncio

bot = commands.Bot(command_prefix='!', intents= discord.Intents.all(), help_command= None)

async def load() :
    await bot.load_extension('cogs.event')
    await bot.load_extension('cogs.help')
    await bot.load_extension('cogs.weather')
    await bot.load_extension('cogs.twitter')
    await bot.load_extension('cogs.news')
    await bot.load_extension('cogs.findpicture')
    await bot.load_extension('cogs.music')

async def main():
    await load()
    await bot.start(getenv.get('DISCORD_TOKEN'))

asyncio.run(main())