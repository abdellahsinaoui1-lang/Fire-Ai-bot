import discord


async def create_channel(guild, message, data):

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
