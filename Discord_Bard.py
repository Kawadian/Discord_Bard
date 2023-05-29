import discord
from bardapi import Bard
import re

bard_token = 'bard_token'

intents = discord.Intents.all()
client = discord.Client(intents=intents)

target_channel_ids = [12345, 12345, 12345]  # 監視したいチャンネルのIDをリストで保持

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_message(message):
    if message.author.bot:
        return 

    # メンションされた時、またはDMでメッセージが送られた場合のみ応答
    if message.channel.id in target_channel_ids or client.user in message.mentions or isinstance(message.channel, discord.DMChannel):
        # メンションの部分を削除
        question = re.sub(r'<@!?\d+>', '', message.content).strip() 

        bard = Bard(token=bard_token)
        question = message.content
        answer = bard.get_answer(question)
        bard_content = answer['content']
        await message.channel.send(bard_content)

client.run("discord_bot_token")
