import requests
import json 
from lyrics_api import *
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.command()
async def Play(ctx, *, song_Name):
    track_name = song_Name
    artist_name = ""

    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    anwar = data['lyrics']['lyrics_body']
    lyrics = json.dumps(anwar)
    while(lyrics != " "):
        word = lyrics
        inte = word.index(' ')
        word = word[0: inte]
        lyrics = lyrics[inte + 1 : ]
        await ctx.send(word)
    print(data['lyrics']['lyrics_body'])


client.run('Put ur own damn key here')