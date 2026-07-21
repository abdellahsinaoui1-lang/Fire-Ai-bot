import discord


async def slowmode(guild, message, data):

    channel_name = data["Name"]
    seconds = int(data["Seconds"])

    channel = discord.utils.get(
        guild.text_channels,
        name=channel_name
    )

    if channel is None:

        await message.reply(
            f"❌ لم أجد الروم **{channel_name}**."
        )

        return

    await channel.edit(
        slowmode_delay=seconds
    )

    if seconds == 0:

        await message.reply(
            f"✅ تم إزالة السلو مود من **{channel.name}**."
        )

    else:

        await message.reply(
            f"🐌 تم ضبط السلو مود في **{channel.name}** إلى **{seconds}** ثانية."
        )
