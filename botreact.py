import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    global a
    print('Logged in {} as {}'.format(client.user.name, client.user.id))
    print('------')

@client.event
async def on_message(message):
    listemj=[client.get_emoji(722020385402650624),client.get_emoji(722021123759538227),
    client.get_emoji(722020322731098152),u'\U0001F921',u'\U0001F63C',u'\U0001F98A', u'\U0001F43A',
    u'\U0001F981', u'\U0001F42F']

    if message.author.id == 439113276643868682:
        print("Lucas envoi un message")
        i=0
        while i<9:
            emoji=listemj[i]
            await message.add_reaction(emoji)
            i+=1

client.run("client ID")
