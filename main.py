import discord  #imports discord library
import random

def randomIntro(number):        #Function that will go through and return one entry from the dictionary made up of random rude introductions
    case = {
        0: "Hello, monkey!",
        1: "Greetings, fellow clown! I see you forgot your make-up!",
        2: "Ahoy, matey! I see the Scurvy got to you too! Oh wait, that's just your teeth...",
        3: "https://tenor.com/view/howdy-cowboy-tom-and-jerry-old-west-gif-5543643",
        4: "What's cookin', good lookin'? Oh sorry, I was looking at myself!",
        5: "Hydrogen iodide! If you don't understand that, it's fine. I already knew you couldn't figure it out!"
    }
    return case.get(number, "... I got nothing! So, hey!")

client = discord.Client()   #Variable to represent connection to discord

@client.event       #Registering an event that will automatically run when it is on
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event       #Registering an event that will have the bot respond to a message
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('$introduce'):        #Checks content of the message to see if bot needs to introduce itself
        await message.channel.send("I am Jester! The rude and loveable bot that will try its hardest to at least make you breathe out harder than usual (We all know you didn't really laugh out loud or laugh your ass off!)")
        await message.channel.send("I was created by the programmer with half of a brain cell, Jeffrey J. Hernandez V.! You should check out my sweet GitHub respository at: https://github.com/JJHV36/Jester-Bot")

    if message.content.lower().startswith('$hello') or message.content.lower().startswith('$hi') or message.content.lower().startswith('$howdy') or message.content.lower().startswith('$hey'):        #Checks the content of the message for a specific hello and responds back in its own silly way!
        rand = random.randint(0,5)
        await message.channel.send(randomIntro(rand))

client.run('ODQ0MzA3Mzc1ODU0MDU5NTMw.YKQghA._Jj5J4gPrK-kTHSfHeSd1kNXmqA')       #Runs the bot with the specified token