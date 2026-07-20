import discord


async def delete_category(guild, message, data):

    name = data["Name"]

    category = discord.utils.get(
        guild.categories,
        name=name
    )

    if category is None:

        await message.reply(
            f"❌ لم أجد كاتيجوري باسم **{name}**."
        )

        return

    await category.delete()

    await message.reply(
        f"🗑️ تم حذف الكاتيجوري **{name}**."
    )
