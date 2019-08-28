import discord
from uwulater import uwulate

#REPLACE WITH OWN TOKEN
TOKEN = 'NjE2MDQwOTcxODYzNDU3ODEz.XWYi8Q.n5Tie3TlLMtmdWcMjb5wXV6XEKM'

client = discord.Client()

prev_msg = {}

@client.event
async def on_message(message):
    global prev_msg
    if message.author == client.user:
        return
    elif message.content.startswith('!uwu'):
        if hash(message.guild) not in prev_msg:
            await message.channel.send('nyothing to uwufy uwu')
        else:
            uwu_message = uwulate(prev_msg[hash(message.guild)])
            await message.channel.send(uwu_message)
    else:
        prev_msg[hash(message.guild)] = message.content


@client.event
async def on_ready():
    print('uwu')

client.run(TOKEN)
