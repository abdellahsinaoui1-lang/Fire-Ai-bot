import discord
from datetime import timedelta


async def timeout_member(guild, message, data):

    member_name = data["Member"]

    member = discord.utils.get(
        guild.members,
        display_name=member_name
    )

    if member is None:
        member = discord.utils.get(
            guild.members,
            name=member_name
        )

    if member is None:

        await message.reply(
            f"❌ لم أجد العضو **{member_name}**."
        )

        return

    minutes = int(data.get("Minutes", 10))

    await member.timeout(
        timedelta(minutes=minutes)
    )

    await message.reply(
        f"⏳ تم كتم **{member.display_name}** لمدة {minutes} دقيقة."
    )
