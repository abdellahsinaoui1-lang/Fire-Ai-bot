import discord


async def delete_channel(guild, message, data):

    name = data["Name"]

    channel = discord.utils.get(
        guild.channels,
        name=name
    )

    if channel is None:

        await message.reply(
            f"❌ لم أجد روم باسم **{name}**."
        )

        return

    await channel.delete()

    await message.reply(
        f"🗑️ تم حذف الروم **{name}**."
    )
