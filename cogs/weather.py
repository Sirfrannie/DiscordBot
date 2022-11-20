
from geopy import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import getenv 
import discord
from discord.ext import commands
import json
import asyncio


key = getenv.get('OPW_KEY')
geolocator = Nominatim(user_agent='geoapiExercise')

temp = []
weather = []
weatherdescription  = []
pressure = []
wind = []
humidity = []
time = []

lstoflst = [temp, weather, weatherdescription, pressure, wind, humidity, time]


# get default location from json file
def getlocation() :
    with open('jsonFile\data.json', "r+") as f :
        data = json.load(f)
    
    return data['default_location']


# create link
def api () :
    geolocator = Nominatim(user_agent='geoapiExercise')
    location = geolocator.geocode(getlocation())
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    api = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&units=metric&appid={key}"
    
    return api
    


# find index of tomorrow in json_data
def tomorrow_index() :
    json_data  = requests.get(api()).json()
    date = json_data['list'][0]['dt_txt']
    today = int(date[8:10])
    tomorrow = today + 1

    tmrIndex = 0
    while 1 :
        if int(json_data['list'][tmrIndex]['dt_txt'][8:10]) == tomorrow :
            break
        else : tmrIndex += 1
    
    return tmrIndex

# change thumpnail image 
def switch(swicth, emBed):
    if swicth == 'clear sky' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/01d@2x.png')

    elif swicth == 'few clouds' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/02d@2x.png')

    elif swicth == 'scattered clouds' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/03d@2x.png')

    elif swicth == 'broken clouds' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/04d@2x.png')

    elif swicth == 'shower rain' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/09d@2x.png')

    elif swicth == 'rain' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/10d@2x.png')

    elif swicth == 'thunderstorm' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/11d@2x.png')

    elif swicth == 'snow' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/13d@2x.png')

    elif swicth == 'mist' :
        emBed.set_thumbnail(url='http://openweathermap.org/img/wn/50d@2x.png')

    else : emBed.set_thumbnail(url='http://openweathermap.org/img/wn/03d@2x.png')

        


# main class
class Weather(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    # send today's weather 
    @commands.command()
    async def weather(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        json_data = requests.get(api()).json()

        for i in range (0,3):
            temp.append(json_data['list'][i]['main']['temp'])
            weather.append(json_data['list'][i]['weather'][0]['main'])
            weatherdescription.append(json_data['list'][i]['weather'][0]['description'])
            pressure.append(json_data['list'][i]['main']['pressure'])
            wind.append(json_data['list'][i]['wind']['speed'])
            humidity.append(json_data['list'][i]['main']['humidity'])
            time.append(json_data['list'][i]['dt_txt'])



        emBed = discord.Embed(title=f"Today's Weather at {getlocation()}", description=f"Date : {time[0][0:10]}", color=0x1F51FF)

        switch(weatherdescription[0], emBed)

        # 1st 
        emBed.add_field(name=f"at {time[0][10::]}", value=\
            f"weather : {weather[0]} ({weatherdescription[0]})\
                \nTemperature : {temp[0]}\
                \nHumidity : {humidity[0]}\
                \nWind Speed : {wind[0]}\
                \nPressure : {pressure[0]} ", inline=False)

        for i in range (1,3) :
            emBed.add_field(name=f"at {time[i][10::]}", value=\
                f"weather : {weather[i]} ({weatherdescription[i]})\
                    \nTemperature : {temp[i]}\
                    \nHumidity : {humidity[i]}\
                    \nWind Speed : {wind[i]}\
                    \nPressure : {pressure[i]} ", inline=True)


        for lst in lstoflst :
            lst.clear()
        
        await ctx.channel.send(embed= emBed)
        return

    
    # forecast tomorrow's weather
    @commands.command()
    async def wforecast(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        json_data = requests.get(api()).json()
        tomorrow = tomorrow_index()

        for i in range (tomorrow,tomorrow+9,3):
            temp.append(json_data['list'][i]['main']['temp'])
            weather.append(json_data['list'][i]['weather'][0]['main'])
            weatherdescription.append(json_data['list'][i]['weather'][0]['description'])
            pressure.append(json_data['list'][i]['main']['pressure'])
            wind.append(json_data['list'][i]['wind']['speed'])
            humidity.append(json_data['list'][i]['main']['humidity'])
            time.append(json_data['list'][i]['dt_txt'])

        emBed = discord.Embed(title=f"Weather forecast for Tomorrow at {getlocation()}", description=f"Date : {time[0][0:10]}", color=0x1F51FF)

        switch(weatherdescription[0], emBed)
        
        # 1st 
        emBed.add_field(name=f"at {time[0][10::]}", value=\
            f"weather : {weather[0]} ({weatherdescription[0]})\
                \nTemperature : {temp[0]}\
                \nHumidity : {humidity[0]}\
                \nWind Speed : {wind[0]}\
                \nPressure : {pressure[0]} ", inline=False)
        
        for i in range (1,3) :
            emBed.add_field(name=f"at {time[i][10::]}", value=\
                f"weather : {weather[i]} ({weatherdescription[i]})\
                    \nTemperature : {temp[i]}\
                    \nHumidity : {humidity[i]}\
                    \nWind Speed : {wind[i]}\
                    \nPressure : {pressure[i]} ", inline=True)


        for lst in lstoflst :
            lst.clear()
        
        await ctx.channel.send(embed= emBed)
        return


    # change default location
    @commands.command()
    async def setlocation(self, ctx,*,Inplocation) :
        async with ctx.typing():
            await asyncio.sleep(0)
        location = geolocator.geocode(Inplocation)

        if location == None :
            await ctx.channel.send("Sorry, I can not find your loacation please try another location's name")
            return 0
        else :
            with open('jsonFile\data.json', 'r+') as f :
                data = json.load(f)
                f.close()
                
            data['default_location'] = Inplocation

            jsonFile = open("jsonFile\data.json", "w+")
            jsonFile.write(json.dumps(data))
            jsonFile.close()
            await ctx.channel.send(f"Location set to {location}")
            return 0


    # show cuurent weather location
    @commands.command()
    async def location(self, ctx) :
        async with ctx.typing():
            await asyncio.sleep(0)
        await ctx.channel.send(f"Current Weather locations : {geolocator.geocode(getlocation())}")


async def setup(bot) :
    await bot.add_cog(Weather(bot))