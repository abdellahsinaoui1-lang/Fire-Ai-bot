import discord
from discord.ext import commands

from config import TOKEN
from events import setup_events
from commands import setup_commands

# ===========================
# Intents
# ===========================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

# ===========================
# Bot
# ===========================

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# ===========================
# Ready Event
# ===========================

@bot.event
async def on_ready():
    print("=" * 40)
    print(f"✅ Logged in as {bot.user}")
    print(f"🆔 ID: {bot.user.id}")
    print("🚀 F7 Bot Started")
    print("=" * 40)

    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} Slash Commands")
    except Exception as e:
        print("❌ Slash Sync Error")
        print(e)

# ===========================
# Load Files
# ===========================

setup_events(bot)
setup_commands(bot)

# ===========================
# Start
# ===========================

bot.run(TOKEN)
