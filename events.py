import discord

from config import ALLOWED_ROLE_ID
from database import is_enabled

from ai import chat
from parser import parse_command
from executor import execute_command


def setup_events(bot):

    @bot.event
    async def on_ready():
        print("✅ Events Loaded")

    @bot.event
    async def on_message(message: discord.Message):

        print(f"📩 Received: {message.content}")

        if message.author.bot:
            print("❌ Message from bot")
            return

        if message.guild is None:
            print("❌ Private Message")
            return

        print(f"✅ Guild ID: {message.guild.id}")

        enabled = is_enabled(message.guild.id)
        print(f"✅ Enabled: {enabled}")

       # if not enabled:
          #  print("❌ Bot is disabled in this server")
          #  return

        if not message.content.lower().startswith("f7"):
            print("❌ Message doesn't start with F7")
            return

        has_role = any(
            role.id == ALLOWED_ROLE_ID
            for role in message.author.roles
        )

        print(f"✅ Has Role: {has_role}")

        if not has_role:
            print("❌ User doesn't have the required role")
            return

        prompt = message.content[2:].strip()

        if prompt == "":
            await message.reply("اكتب طلبك بعد F7.")
            return

        print(f"🧠 Prompt: {prompt}")

        async with message.channel.typing():

            try:

                server_info = ""

    command = parse_command(
    prompt,
    server_info
)

print(command)
                print("📦 Parsed Command:", command)

                if "NoSkill0" in command:

                    response = chat(
                        prompt,
                        message.guild
                    )

                    await message.reply(response)
                    return

                await execute_command(
                    bot,
                    message,
                    command
                )

            except Exception as e:
                print("❌ ERROR:", e)
                await message.reply(
                    "حدث خطأ أثناء معالجة الطلب."
                )

        await bot.process_commands(message)
