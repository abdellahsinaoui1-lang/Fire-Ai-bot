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

        # تجاهل رسائل البوتات
        if message.author.bot:
            return

        # تجاهل الرسائل الخاصة
        if message.guild is None:
            return

        print(f"✅ Guild ID: {message.guild.id}")

        enabled = is_enabled(message.guild.id)
        print(f"✅ Enabled: {enabled}")

        # إذا كان البوت غير مفعل
       # if not enabled:
           # return

        # يجب أن تبدأ الرسالة بـ F7
        if not message.content.lower().startswith("f7"):
            return

        # التحقق من الرتبة
        has_role = any(
            role.id == ALLOWED_ROLE_ID
            for role in message.author.roles
        )

        print(f"✅ Has Role: {has_role}")

        if not has_role:
            return

        # إزالة F7 من بداية الرسالة
        prompt = message.content[2:].strip()

        if prompt == "":
            await message.reply("اكتب طلبك بعد F7.")
            return

        print(f"🧠 Prompt: {prompt}")

        async with message.channel.typing():

            try:

                # سنستخدمها لاحقًا لإعطاء الـ AI معلومات عن السيرفر
                server_info = ""

                command = parse_command(
                    prompt,
                    server_info
                )

                print("📦 Parsed Command:", command)

                # إذا لم يكن أمر Discord
                if "NoSkill0" in command:

                    response = chat(
                        prompt,
                        message.guild
                    )

                    await message.reply(response)
                    return

                # تنفيذ أوامر Discord
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
