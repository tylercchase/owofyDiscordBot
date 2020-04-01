# Work with Python 3.6
import discord
from filter import process_image
TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
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