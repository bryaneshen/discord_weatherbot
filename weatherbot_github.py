import discord
import requests
from discord.ext import commands

token = 'enter discord token here' # for the discord server
bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("Bot is ready.") # letting me know that the bot is ready to be used

@bot.command('weather')
async def weather_output(context, city):
    api_address = "http://api.weatherstack.com/current?access_key=96b61cb41acaad6fe3b5d8b31465a586&query="
    api_url = api_address + city # finding the weather of the user's desired destination
    json_data = requests.get(api_url).json() # retrieving data from JSON file

    city_name = json_data["location"]["name"] # retrieving name of the city
    temperature = json_data["current"]["temperature"] # retrieving the temperature
    weather_description = json_data["current"]["weather_descriptions"][0] # retrieving the weather description

    await context.send(f'\nCity: {city_name} \nTemperature is {temperature} degrees celcius. \n{weather_description}') # this will be sent after the command is used

bot.run(token)
