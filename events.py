import discord

from config import ALLOWED_ROLE_ID
from ai import ask_ai

# حالة البوت لكل سيرفر
from database import is_enabled


def setup_events(bot):

    @bot.event
    async def on_ready():
        print(f"✅ Events Loaded")

    @bot.event
    async def on_message(message: discord.Message):

        # تجاهل رسائل البوتات
        if message.author.bot:
            return

        # لازم يكون داخل سيرفر
        if message.guild is None:
            return

        # التأكد أن البوت مفعل في هذا السيرفر
        if message.guild.id not in enabled_guilds:
            return

        # لازم يبدأ بـ F7
        if not message.content.lower().startswith("f7"):
            return

        # التأكد من الرتبة
        has_role = any(role.id == ALLOWED_ROLE_ID for role in message.author.roles)

        if not has_role:
            return

        # حذف كلمة F7
        prompt = message.content[2:].strip()

        if prompt == "":
            await message.reply("اكتب طلبك بعد F7.")
            return

        print(f"[{message.guild.name}] {message.author} -> {prompt}")

        async with message.channel.typing():

            try:
                response = ask_ai(prompt, message.guild)

                await message.reply(response)

            except Exception as e:
                print(e)
                await message.reply("حدث خطأ أثناء التواصل مع الذكاء الاصطناعي.")

        await bot.process_commands(message)
