import discord
from discord.ext import commands
import random

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

class Hello(commands.Cog):      #Cog for the bot respond back to someone saying hello

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command(aliases=["hey","howdy","hi"])
    async def hello(self, ctx):     #Bot will respond to hello in its own unique way by calling to the randomIntro function
            rand = random.randint(0, 10)
            await ctx.send(randomIntro(rand))

def setup(client):
    client.add_cog(Hello(client))