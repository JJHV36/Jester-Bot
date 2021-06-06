import discord
from discord.ext import commands

from jokeapi import Jokes       #Creating from the JokeAPI Python Wrapper
response = Jokes()
blacklisted = ['sexist', 'racist']
filter = {      #dictionary made up of the filters to see which are on and off
            'nsfw': True,
            'religious': True,
            'political': True,
            'racist': False,
            'sexist': False
        }
joke = response.get_joke(blacklist=blacklisted, response_format="txt")

class Joke(commands.Cog):      #Cog for the bot to make its jokes!

    def __init__(self, client):
        self.client = client
        global blacklisted
        global joke

    #Commands
    @commands.command()
    async def joke(self, ctx):  #The joke function, used to determine a joke with the current filters and if detected, any phrase after command
        search = ctx.message.content.lower()
        if len(search) > 5:
            specificJoke = search[6:]
            joke = response.get_joke(blacklist=blacklisted, search_string=specificJoke, response_format="txt")
        else:
            joke = response.get_joke(blacklist=blacklisted, response_format="txt")
        await ctx.send(joke)

    @commands.command()
    async def filter(self, ctx):  #Command that focuses on handling the filtering of the jokes, requires input after command
        command = ctx.message.content.lower()
        global filter
        try:
            keyword = command[8:]       #Checking to see if keyword after filter is in the filter dictionary. If not, it will prompt with better instructions
            if keyword in filter:
                filter[keyword] = not filter[keyword]
                await ctx.send("Alright, I'm updating my jokebook! So, my jokes can now be:")       #Making updates to its filters and letting you know which are on and off
                if(filter['nsfw']):
                    await ctx.send('Not safe for work ( ͡° ͜ʖ ͡°)')
                    if 'nsfw' in blacklisted:
                        blacklisted.remove('nsfw')
                else:
                    await ctx.send('Safe for work. I will keep it PG!')
                    if 'nsfw' not in blacklisted:
                        blacklisted.insert(0, 'nsfw')
                if(filter['religious']):
                    await ctx.send("Religious. I'm keeping the holy jokes in!")
                    if 'religious' in blacklisted:
                        blacklisted.remove('religious')
                else:
                    await ctx.send('Non-religious. To each their own, am I right?')
                    if 'religious' not in blacklisted:
                        blacklisted.insert(1, 'religious')
                if(filter['political']):
                    await ctx.send("Politicial. It doesn't matter who or what you follow! You WILL be joked about")
                    if 'political' in blacklisted:
                        blacklisted.remove('political')
                else:
                    await ctx.send('Non-political. Typical politician...')
                    if 'political' not in blacklisted:
                        blacklisted.insert(2, 'political')
                if(filter['racist']):
                    await ctx.send("Racist. I'm not racist... BUT!")
                    if 'racist' in blacklisted:
                        blacklisted.remove('racist')
                else:
                    await ctx.send("Non-racist. I'm trying to avoid getting my creator canceled!")
                    if 'racist' not in blacklisted:
                        blacklisted.insert(3, 'racist')
                if(filter['sexist']):
                    await ctx.send("Sexist. Thankfully, I'm safe because I have no gender!")
                    if 'sexist' in blacklisted:
                        blacklisted.remove('sexist')
                else:
                    await ctx.send('Non-sexist. Alright, fine, Karen! I will comply!')
                    if 'sexist' not in blacklisted:
                        blacklisted.insert(4, 'sexist')
        except:
            await ctx.send('Something is wrong, I can feel it! Did you try only putting in one filter at a time? My current filters are: nsfw, religious, political, racist, and sexist!')
            await ctx.send('I know, I know. My creator is very efficient!')

def setup(client):
    client.add_cog(Joke(client))