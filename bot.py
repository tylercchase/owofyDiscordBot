import discord, os
from filter import process_image, owoify_text
from owotrans import owo
TOKEN = os.getenv(TOKEN)

client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('owo'):
        owoified_name = owoify_text(message.author.nick)
        try: 
            if len(owoified_name) <= 32:
                await message.author.edit(nick=owoified_name, reason="OwO")
        except:
            print("unable to do nick change")
        img = process_image(message.author.avatar_url)
        fileA = discord.File(img,filename="hello.png")
        await message.channel.send(file=fileA)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run(TOKEN)
