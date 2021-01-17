import json
import discord
from bot import Bot
# all the config are store in config.json
with open('config.json', 'r') as f:
    config = json.load(f)

client = discord.Client()
discord_bot = Bot(client)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# on client message incoming point.
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    data = message.content
    resp = discord_bot.get_response(data)
    await message.channel.send(resp)


client.run(config['discord']['token'])
