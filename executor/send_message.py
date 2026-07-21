import discord


async def send_message(guild, message, data):

    channel_name = data["Channel"]
    content = data["Message"]

    channel = discord.utils.get(
        guild.text_channels,
        name=channel_name
    )

    if channel is None:

        await message.reply(
            f"❌ لم أجد روم باسم **{channel_name}**."
        )

        return

    await channel.send(content)

    await message.reply(
        f"✅ تم إرسال الرسالة في **{channel_name}**."
    )
