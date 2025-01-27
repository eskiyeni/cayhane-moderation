import discord
from discord.ext import commands
import json
import time
import os

start_time = time.time()

def json_load(file) -> dict:
    try:
        with open(file, "r") as f:
            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Json yüklenirken hata oluştu: {e}")
        exit()

def return_uptime() -> str:
    uptime_seconds = int(time.time() - start_time)
    days = uptime_seconds // (24 * 3600)
    hours = (uptime_seconds % (24 * 3600)) // 3600
    minutes = (uptime_seconds % 3600) // 60

    return f"{days} gün, {hours} saat, {minutes} dakika"

config = json_load("config.json")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents, help_command=None)
bot.return_uptime = return_uptime
bot.config = config

async def load_extensions():
    for file in os.listdir(
        os.path.join(
            os.getcwd(), "commands"
        )
    ):
        if file.endswith(".py"):
            await bot.load_extension(f"commands.{file[:-3]}")

@bot.event
async def on_ready():
    await load_extensions()
    await bot.tree.sync()
    print(f"{bot.user.name} aktif!")

bot.run(config["token"])