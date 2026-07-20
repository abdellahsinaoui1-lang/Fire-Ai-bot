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

        if channel_type.lower() == "text":

            await guild.create_text_channel(
                name=name,
                category=category
            )

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
    # Create Category
    # ===========================

    if "CreateCategory0" in command:

        data = command["CreateCategory0"]

        name = data["Name"]

        await guild.create_category(name=name)

        await message.reply(
            f"✅ تم إنشاء الكاتيجوري **{name}**."
        )
        return

    # ===========================
    # Create Role
    # ===========================

    if "CreateRole0" in command:

        data = command["CreateRole0"]

        name = data["Name"]

        color_name = data.get("Color", "").lower()

        colors = {
            "red": discord.Color.red(),
            "blue": discord.Color.blue(),
            "green": discord.Color.green(),
            "yellow": discord.Color.yellow(),
            "orange": discord.Color.orange(),
            "purple": discord.Color.purple(),
            "pink": discord.Color.magenta(),
            "black": discord.Color.dark_gray(),
            "white": discord.Color.light_gray(),

            "احمر": discord.Color.red(),
            "ازرق": discord.Color.blue(),
            "أزرق": discord.Color.blue(),
            "اخضر": discord.Color.green(),
            "أخضر": discord.Color.green(),
            "اصفر": discord.Color.gold(),
            "أصفر": discord.Color.gold(),
            "برتقالي": discord.Color.orange(),
            "بنفسجي": discord.Color.purple(),
            "وردي": discord.Color.magenta(),
            "ابيض": discord.Color.light_gray(),
            "أبيض": discord.Color.light_gray(),
            "اسود": discord.Color.dark_gray(),
            "أسود": discord.Color.dark_gray(),
        }

        color = colors.get(color_name, discord.Color.default())

        await guild.create_role(
            name=name,
            color=color
        )

        await message.reply(
            f"✅ تم إنشاء الرتبة **{name}**."
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
    # Unknown
    # ===========================

    await message.reply(
        "❌ لا أعرف كيف أنفذ هذا الأمر حتى الآن."
    )
