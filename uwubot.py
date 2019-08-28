import discord
from uwulater import uwulate

TOKEN = 'NjE2MDQwOTcxODYzNDU3ODEz.XWXJ6w.BprUgtO_EL_K0oR2sDYcHD9JtHE'  #REPLACE WITH OWN TOKEN

client = discord.Client()

prev_msg = ''

@client.event
async def on_message(message):
    global prev_msg
    if message.author == client.user:
        return
    elif message.content.startswith('!uwu'):
        await message.channel.send(uwulate(prev_msg))
    else:
        prev_msg = message.content
        print('recorded ' + prev_msg)


@client.event
async def on_ready():
    print('uwu')

client.run(TOKEN)
