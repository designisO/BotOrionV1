import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to "DEVS ON BLOCKS" server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # adding DEVS ON BLOCKS QUOTES.
    dobq = [
        'DEVS ON BLOCKS is created for the passionate Web3 developers!',
        'Patience, Practice and Persistence are the keys to win',
        (
            'You are not going to win if you quit!'
        ),
    ]

    # if users type DOBQ then a quote will appear in the discord channel.
    if message.content == 'dobq':
        response = random.choice(dobq)
        await message.channel.send(response)

client.run(TOKEN)