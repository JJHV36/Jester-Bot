import discord
from discord.ext import commands

class Intro(commands.Cog):      #Cog for the bot to make an introduction!

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):       #Registering an event that will automatically run when it is on
        print('We have logged in as the funniest bot around, JESTER!')

    #Commands
    @commands.command(aliases=['introduce'])
    async def intro(self, ctx):     #Bot needs to introduce itself
        await ctx.send("I am Jester! The rude and loveable bot that will try its hardest to at least make you breathe out harder than usual (We all know you didn't really laugh out loud or laugh your ass off!)")
        await ctx.send("I was created by the programmer with half of a brain cell, Jeffrey J. Hernandez V.! You should check out my sweet GitHub respository at: https://github.com/JJHV36/Jester-Bot")

def setup(client):
    client.add_cog(Intro(client))