async def create_category(guild, message, data):

    name = data["Name"]

    await guild.create_category(name=name)

    await message.reply(
        f"✅ تم إنشاء الكاتيجوري **{name}**."
    )
