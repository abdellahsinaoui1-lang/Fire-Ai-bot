import discord


async def unlock_channel(guild, message, data):

    channel_name = data["Name"]

    channel = discord.utils.get(
        guild.channels,
        name=channel_name
    )

    if channel is None:

        await message.reply(
            f"❌ لم أجد الروم **{channel_name}**."
        )

        return

    overwrite = channel.overwrites_for(
        guild.default_role
    )

    overwrite.send_messages = None

    await channel.set_permissions(
        guild.default_role,
        overwrite=overwrite
    )

    await message.reply(
        f"🔓 تم فتح الروم **{channel.name}**."
    )
