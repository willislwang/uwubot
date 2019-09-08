import discord
from uwulater import uwulate

#REPLACE WITH OWN TOKEN
TOKEN = 'NjE2MDQwOTcxODYzNDU3ODEz.XXNXzg.48iLBwLx5NeBjhvLAkZ0WHCPyBw'

client = discord.Client()

#Storage optmized for multiple servers
is_uwu = {}
prev_msg = {}


@client.event
async def on_message(message):
    global prev_msg
    global is_uwu
    if message.author == client.user:
        return
    #Check uwu mode
    if hash(message.guild) in is_uwu and is_uwu[hash(message.guild)]:
        await message.edit(content = uwulate(message.content))
    '''
    Well discord doesn't support this okay
    elif message.content.startswith('!uwufy'):
        is_uwu[hash(message.guild)] = True
        await message.channel.send('Uwufying all messages! Use !nouwu to disable pls dont ; - ;')
    '''
    #Uwufy previous message
    elif message.content.startswith('!uwu'):
        if hash(message.guild) not in prev_msg:
            await message.channel.send('nyothing to uwufy uwu')
        else:
            uwu_message = uwulate(prev_msg[hash(message.guild)])
            await message.channel.send(uwu_message)
    '''
    elif message.content.startswith('!nouwu'):
        is_uwu[hash(message.guild)] = False
    '''
    else:
        prev_msg[hash(message.guild)] = message.content


@client.event
async def on_ready():
    print('uwu')

client.run(TOKEN)
