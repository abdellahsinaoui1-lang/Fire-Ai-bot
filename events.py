import discord

from config import ALLOWED_ROLE_ID
from database import is_enabled
from executor import execute_command

from ai import chat
from parser import parse_command


def setup_events(bot):

    @bot.event
    async def on_ready():
        print("✅ Events Loaded")

    @bot.event
    async def on_message(message: discord.Message):

        if message.author.bot:
            return

        if message.guild is None:
            return

        if not is_enabled(message.guild.id):
            return

        if not message.content.lower().startswith("f7"):
            return

        has_role = any(
            role.id == ALLOWED_ROLE_ID
            for role in message.author.roles
        )

        if not has_role:
            return

        prompt = message.content[2:].strip()

        if prompt == "":
            await message.reply("اكتب طلبك بعد F7.")
            return

        print(f"[{message.guild.name}] {message.author} -> {prompt}")

        async with message.channel.typing():

        try:

            server_info = ""

            command = parse_command(
                prompt,
                server_info
            )

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
            print(e)
            await message.reply(
                "حدث خطأ أثناء معالجة الطلب."
            )

        await bot.process_commands(message)
