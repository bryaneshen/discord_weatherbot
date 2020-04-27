import discord
import requests
from discord.ext import commands

Token = 'enter token here' # for the discord server
bot = commands.Bot(command_prefix = '.')

api_url = "http://api.weatherstack.com/current?access_key=96b61cb41acaad6fe3b5d8b31465a586&query=vancouver"
json_data = requests.get(api_url).json()

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.command('weather')
async def weather_output(context): # can do more than one parameter: context, *, location
    city_name = json_data["location"]["name"]
    temperature = json_data["current"]["temperature"]
    weather_description = json_data["current"]["weather_descriptions"][0]
    await context.send(f'\nCity: {city_name} \nTemperature is {temperature} degrees celcius. \n{weather_description}') # this will be sent after the command is used

bot.run(Token)
