import discord
import requests
from discord.ext import commands

Token = 'enter token for discord server here ' # for the discord server
bot = commands.Bot(command_prefix = '.')

api_url = "http://api.weatherstack.com/current?access_key=96b61cb41acaad6fe3b5d8b31465a586&query=vancouver"
json_data = requests.get(api_url).json() # this is to retrieve the data from the JSON file

@bot.event
async def on_ready():
    print("Bot is ready.") # letting me know that the bot is ready to be used

@bot.command('weather')
async def weather_output(context):
    city_name = json_data["location"]["name"] # retrieving name of the city
    temperature = json_data["current"]["temperature"] # retrieving the temperature
    weather_description = json_data["current"]["weather_descriptions"][0] # retrieving the weather description
    await context.send(f'\nCity: {city_name} \nTemperature is {temperature} degrees celcius. \n{weather_description}') # this will be sent after the command is used

bot.run(Token)
