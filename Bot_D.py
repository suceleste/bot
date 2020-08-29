import requests
import json
import discord
from discord.ext import commands
import asyncio



client = commands.Bot(command_prefix= '!')

@client.command()
async def ip(ctx, ip_Adress):

    API = f"https://ipapi.co/{ip_Adress}/json/"
    result = requests.get(API)
    data = result.json()

    city = data["city"]
    country_name = data["country_name"]
    region = data["region"]
    org  = data["org"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    position = f"https://www.google.com/maps/search/?api=1&query={latitude}%2C{longitude}&hl=fr"

    print (API)
    await ctx.send(f"Cette adresse ip est localisé à {city} en {region} en {country_name} par l'opérateur {org}.")
    await ctx.send(f"{position}")

@client.command()
async def connected(ctx):

    await ctx.send("Bonjour, je suis actuellement connecter")

@client.command()
async def rame(ctx, Episode):

    api = f"https://rickandmortyapi.com/api/episode/{Episode}"
    api = requests.get(api)
    data_RAME = api.json()

    name = data_RAME["name"]
    air_date = data_RAME["air_date"]
    episode = data_RAME["episode"]

    await ctx.send(f"Nom de l'Episode : {name}")
    print (Episode)
    await ctx.send(f"Date de Sortie : {air_date}")
    await ctx.send(f"Episode Numéro : {episode}")


@client.command()
async def covid(ctx) :

    api_C = "https://api.covid19api.com/world/total"
    api_C = requests.get(api_C)
    data_C = api_C.json()

    total = data_C["TotalConfirmed"]
    total_death = data_C["TotalDeaths"]
    total_recovered = data_C["TotalRecovered"]

    print (total)
    await ctx.send(f"Total d'infectés : {total}")
    await ctx.send(f"Total de mort : {total_death}")
    await ctx.send(f"Total de survivants : {total_recovered}")

@client.command()
async def delete(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


client.run("NzQ3MDg3NDUxMDkyMjg3NTIx.X0JxaA.CkfjL1WMODNfJiEcMWCj3hs518M")

