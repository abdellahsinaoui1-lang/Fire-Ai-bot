import discord


async def execute_command(bot, message: discord.Message, command: dict):

    guild = message.guild

    # ==========================================
    # Create Channel
    # ==========================================

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

    # ==========================================
    # Create Category
    # ==========================================

    if "CreateCategory0" in command:

        data = command["CreateCategory0"]

        name = data["Name"]

        await guild.create_category(name=name)

        await message.reply(
            f"✅ تم إنشاء الكاتيجوري **{name}**."
        )

        return

    # ==========================================
    # Create Role
    # ==========================================

    if "CreateRole0" in command:

        data = command["CreateRole0"]

        name = data["Name"]

        color_name = data.get("Color")

        if color_name:

            color_name = (
                color_name.lower()
                .replace("أ", "ا")
                .replace("إ", "ا")
                .replace("آ", "ا")
                .strip()
            )

        colors = {

            "احمر": discord.Color.red(),
            "ازرق": discord.Color.blue(),
            "اخضر": discord.Color.green(),
            "اصفر": discord.Color.gold(),
            "برتقالي": discord.Color.orange(),
            "بنفسجي": discord.Color.purple(),
            "وردي": discord.Color.magenta(),
            "ابيض": discord.Color.light_grey(),
            "اسود": discord.Color.dark_grey(),

            "red": discord.Color.red(),
            "blue": discord.Color.blue(),
            "green": discord.Color.green(),
            "yellow": discord.Color.gold(),
            "orange": discord.Color.orange(),
            "purple": discord.Color.purple(),
            "pink": discord.Color.magenta(),
            "white": discord.Color.light_grey(),
            "black": discord.Color.dark_grey(),
        }

        color = colors.get(color_name, discord.Color.default())

        permissions = discord.Permissions.none()

        for perm in data.get("Permissions", []):

            if hasattr(permissions, perm):
                setattr(permissions, perm, True)

        await guild.create_role(
            name=name,
            color=color,
            permissions=permissions
        )

        await message.reply(
            f"✅ تم إنشاء الرتبة **{name}**."
        )

        return

    # ==========================================
    # No Skill
    # ==========================================

    if "NoSkill0" in command:

        await message.reply(
            command["NoSkill0"]["Reply"]
        )

        return

    # ==========================================
    # Unknown
    # ==========================================

    await message.reply(
        "❌ لا أعرف كيف أنفذ هذا الأمر حتى الآن."
    )
