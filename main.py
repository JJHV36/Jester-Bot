import discord  #imports discord library
import random

from jokeapi import Jokes       #Creating from the JokeAPI Python Wrapper
response = Jokes()
blacklisted = ['sexist', 'racist']
joke = response.get_joke(blacklist=blacklisted, response_format="txt")

def randomIntro(number):        #Function that will go through and return one entry from the dictionary made up of random rude introductions
    case = {
        0: "Hello, monkey!",
        1: "Greetings, fellow clown! I see you forgot your make-up!",
        2: "Ahoy, matey! I see the Scurvy got to you too! Oh wait, that's just your teeth...",
        3: "https://tenor.com/view/howdy-cowboy-tom-and-jerry-old-west-gif-5543643",
        4: "What's cookin', good lookin'? Oh sorry, I was looking at myself!",
        5: "Hydrogen iodide! If you don't understand that, it's fine. I already knew that you couldn't figure it out!",
        6: "Hi, side character! I see you are still trying to be relevant!",
        7: "Well, look what the cat dragged in! A rodent!",
        8: "Saluations! I never expected to meet life outside of Earth. Oh wait, you're human. Darn...",
        9: "WAZZAAAAAAAAAAAP!!!",
        10: "*scans power level* I had to make sure you aint threat! But, based on your appearance, I didn't need to worry!"
    }
    return case.get(number, "... I got nothing! So, hey!")

client = discord.Client()   #Variable to represent connection to discord

@client.event       #Registering an event that will automatically run when it is on
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event       #Registering an event that will have the bot respond to a message
async def on_message(message):
    global blacklisted
    global joke
    if message.author == client.user:
        return

    if message.content.lower().startswith('$introduce'):        #Checks content of the message to see if bot needs to introduce itself
        await message.channel.send("I am Jester! The rude and loveable bot that will try its hardest to at least make you breathe out harder than usual (We all know you didn't really laugh out loud or laugh your ass off!)")
        await message.channel.send("I was created by the programmer with half of a brain cell, Jeffrey J. Hernandez V.! You should check out my sweet GitHub respository at: https://github.com/JJHV36/Jester-Bot")

    if message.content.lower().startswith('$hello') or message.content.lower().startswith('$hi') or message.content.lower().startswith('$howdy') or message.content.lower().startswith('$hey'):        #Checks the content of the message for a specific hello and responds back in its own silly way!
        rand = random.randint(0,10)
        await message.channel.send(randomIntro(rand))

    if message.content.lower().startswith('$joke'):     #Will tell joke either randomly or by whatever is asked after keyword based on filters
        search = message.content.lower()
        if len(search) > 5:
            specificJoke = search[6:]
            joke = response.get_joke(blacklist=blacklisted, search_string=specificJoke, response_format="txt")
        else:
            joke = response.get_joke(blacklist=blacklisted, response_format="txt")
        await message.channel.send(joke)

    if message.content.lower().startswith('$filter'):       #Start of filtering branch
        command = message.content.lower()
        filter = {      #dictionary made up of the filters to see which are on and off
            'nsfw': True,
            'religious': True,
            'political': True,
            'racist': False,
            'sexist': False
        }
        try:
            keyword = command[8:]       #Checking to see if keyword after filter is in the filter dictionary. If not, it will prompt with better instructions
            if keyword in filter:
                filter[keyword] = not filter[keyword]
                await message.channel.send("Alright, I'm updating my jokebook! So, my jokes can now be:")       #Making updates to its filters and letting you know which are on and off
                if(filter['nsfw']):
                    await message.channel.send('Not safe for work ( ͡° ͜ʖ ͡°)')
                    if 'nsfw' in blacklisted:
                        blacklisted.remove('nsfw')
                else:
                    await message.channel.send('Safe for work. I will keep it PG!')
                    if 'nsfw' not in blacklisted:
                        blacklisted.insert(0, 'nsfw')
                if(filter['religious']):
                    await message.channel.send("Religious. I'm keeping the holy jokes in!")
                    if 'religious' in blacklisted:
                        blacklisted.remove('religious')
                else:
                    await message.channel.send('Non-religious. To each their own, am I right?')
                    if 'religious' not in blacklisted:
                        blacklisted.insert(1, 'religious')
                if(filter['political']):
                    await message.channel.send("Politicial. It doesn't matter who or what you follow! You WILL be joked about")
                    if 'political' in blacklisted:
                        blacklisted.remove('political')
                else:
                    await message.channel.send('Non-political. Typical politician...')
                    if 'political' not in blacklisted:
                        blacklisted.insert(2, 'political')
                if(filter['racist']):
                    await message.channel.send("Racist. I'm not racist... BUT!")
                    if 'racist' in blacklisted:
                        blacklisted.remove('racist')
                else:
                    await message.channel.send("Non-racist. I'm trying to avoid getting my creator canceled!")
                    if 'racist' not in blacklisted:
                        blacklisted.insert(3, 'racist')
                if(filter['sexist']):
                    await message.channel.send("Sexist. Thankfully, I'm safe because I have no gender!")
                    if 'sexist' in blacklisted:
                        blacklisted.remove('sexist')
                else:
                    await message.channel.send('Non-sexist. Alright, fine, Karen! I will comply!')
                    if 'sexist' not in blacklisted:
                        blacklisted.insert(4, 'sexist')
        except:
            await message.channel.send('Something is wrong, I can feel it! Did you try only putting in one filter at a time? My current filters are: nsfw, religious, political, racist, and sexist!')
            await message.channel.send('I know, I know. My creator is very efficient!')




client.run('TOKEN!')       #Runs the bot with the specified token