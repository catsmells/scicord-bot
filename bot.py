import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    print(1)
    if message.author.id == bot.user.id:
        print(2)
        return
    print(3)
    if message.content.lower().endswith("er"):
        print(4)
        response = f"{message.content}? I hardly know her!"
        print(5)
        await message.channel.send(response)
        print(6)
    print(7)
    await bot.process_commands(message)
bot.run('token')
