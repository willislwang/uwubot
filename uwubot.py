import discord
from uwulater import uwulate

#REPLACE WITH OWN TOKEN
TOKEN = 'NjE2MDQwOTcxODYzNDU3ODEz.XXVk7A.38ytlfbZ7byZE1hG7pasfWflMVY'

client = discord.Client()

#Storage optmized for multiple servers
is_uwu = {} #stores uwufy mode by server
prev_msg = {} #stores previous message

help_message = "```----------help uwu----------```\nUwufy pwevious messages with\n```!uwu```\nUwufy aww messages with\n```!uwufy```\nand tuwn off with\n```!nouwu```"


@client.event
async def on_message(message):
    global prev_msg
    global is_uwu
    if message.author == client.user:
        return
    ##Help
    if message.content.startswith('!help'):
        await message.channel.send(help_message) 
    #Well discord doesn't support this okay
    #Disable uwufy mode
    elif message.content.startswith('!nouwu'):
        is_uwu[hash(message.guild)] = False
        await message.channel.send('.｡･ﾟﾟ･(＞_＜)･ﾟﾟ･｡.')
    if message.content.startswith('!uwufy'):
        is_uwu[hash(message.guild)] = True
        await message.channel.send('Uwufying all messages! Use !nouwu to disable pls dont ( ; ω ; )')
    #Check uwu mode
    elif hash(message.guild) in is_uwu and is_uwu[hash(message.guild)]:
        #await message.edit(content = uwulate(message.content))
        await message.delete()
        await message.channel.send(message.author.name + ':\n```' + uwulate(message.content) + '```')
    #Uwufy previous message
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
