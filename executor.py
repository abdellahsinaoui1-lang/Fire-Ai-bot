import discord


async def execute_command(bot, message: discord.Message, command: dict):

    guild = message.guild

    # ===========================
    # Create Channel
    # ===========================

    if "CreateChannel0" in command:

        data = command["CreateChannel0"]

        name = data["Name"]
        channel_type = data["Type"]

        category = None

        if data.get("Category"):

            category = discord.utils.get(
                guild.categories,
                name=data["Category"]
            )

        # روم نصي
        if channel_type.lower() == "text":

            await guild.create_text_channel(
                name=name,
                category=category
            )

        # روم صوتي
        elif channel_type.lower() == "voice":

            await guild.create_voice_channel(
                name=name,
                category=category
            )

        await message.reply(
            f"✅ تم إنشاء الروم **{name}**."
        )

        return

    # ===========================
    # No Skill
    # ===========================

    if "NoSkill0" in command:

        await message.reply(
            command["NoSkill0"]["Reply"]
        )

        return

    # ===========================
    # Unknown Command
    # ===========================

    await message.reply(
        "❌ لا أعرف كيف أنفذ هذا الأمر حتى الآن."
    )
