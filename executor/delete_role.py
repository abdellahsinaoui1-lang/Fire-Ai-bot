import discord


async def delete_role(guild, message, data):

    name = data["Name"]

    role = discord.utils.get(
        guild.roles,
        name=name
    )

    if role is None:

        await message.reply(
            f"❌ لم أجد رتبة باسم **{name}**."
        )

        return

    await role.delete()

    await message.reply(
        f"🗑️ تم حذف الرتبة **{name}**."
    )
