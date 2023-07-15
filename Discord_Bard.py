import discord
import os
import re
import sqlite3
from bardapi import Bard
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

# Connect to the SQLite database (or create it)
conn = sqlite3.connect('token.db')
c = conn.cursor()

# Create table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS tokens
             (id INTEGER PRIMARY KEY, bard_token text)''')

# Commit and close the connection
conn.commit()
conn.close()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
slash = SlashCommand(client, sync_commands=True)

target_channel_ids = [1112563855852314674, 1112630941572141077, 12345]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

@slash.slash(
    name="set_token",
    description="Set Bard token.",
    options=[
        create_option(
            name="token",
            description="Your Bard token.",
            option_type=3,
            required=True
        )
    ])
async def _set_token(ctx: SlashContext, token: str):
    try:
        conn = sqlite3.connect('token.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tokens WHERE id = 1")
        if c.fetchone() is not None:
            c.execute("UPDATE tokens SET bard_token = ? WHERE id = 1", (token,))
        else:
            c.execute("INSERT INTO tokens VALUES (1, ?)", (token,))
        conn.commit()
        conn.close()
        await ctx.send("Token successfully updated.", hidden=True)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}", hidden=True)

@client.event
async def on_message(message):
    if message.author.bot:
        return 

    if message.channel.id in target_channel_ids or client.user in message.mentions or isinstance(message.channel, discord.DMChannel):
        try:
            question = re.sub(r'<@!?\d+>', '', message.content).strip()

            conn = sqlite3.connect('token.db')
            c = conn.cursor()
            c.execute("SELECT bard_token FROM tokens WHERE id = 1")
            bard_token = c.fetchone()
            conn.close()

            if not bard_token:
                await message.channel.send("Bard token is not set.")
                return

            bard = Bard(token=bard_token[0])
            question = message.content
            async with message.channel.typing():
                answer = bard.get_answer(question)
            bard_content = answer['content']
            await message.channel.send(bard_content)
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")

client.run("Discord_token")
