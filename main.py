import asyncio
import os
import random

import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    client.loop.create_task(background_task())


@client.event
async def on_message(message):
    if message.content == "!playsound":
        await checkVoiceChannels(1)


async def checkVoiceChannels(randomness):
    for guild in client.guilds:
        for channel in guild.voice_channels:
            
            if channel.members:
                num = random.randrange(0, randomness)
                print(num)
                if num == 0:
                    await playSound(channel)


async def playSound(channel):
    path = os.path.join('Sounds', random.choice(os.listdir('Sounds')))
    sound = discord.FFmpegPCMAudio(path)
    voice_client = await channel.connect()

    async def play():
        voice_client.play(sound,
                          after=lambda err: client.loop.create_task(
                              voice_client.disconnect()))

    await play()


async def background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        await checkVoiceChannels(15)
        await asyncio.sleep(20)


client.run(os.environ['TOKEN'])
