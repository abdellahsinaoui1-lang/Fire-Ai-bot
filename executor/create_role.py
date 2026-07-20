import discord


async def create_role(guild, message, data):

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

    color = colors.get(
        color_name,
        discord.Color.default()
    )

    permissions = discord.Permissions.none()

    for perm in data.get("Permissions", []):

        if hasattr(permissions, perm):
            setattr(
                permissions,
                perm,
                True
            )

    await guild.create_role(
        name=name,
        color=color,
        permissions=permissions
    )

    await message.reply(
        f"✅ تم إنشاء الرتبة **{name}**."
    )
