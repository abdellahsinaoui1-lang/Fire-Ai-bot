import discord


async def purge_messages(guild, message, data):

    amount = int(data.get("Amount", 10))

    if amount < 1:
        amount = 1

    if amount > 100:
        amount = 100

    deleted = await message.channel.purge(limit=amount + 1)

    await message.channel.send(
        f"🧹 تم حذف {len(deleted)-1} رسالة.",
        delete_after=5
    )
