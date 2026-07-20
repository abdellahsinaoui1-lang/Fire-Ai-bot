import discord


async def kick_member(guild, message, data):

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

    reason = data.get("Reason", "No reason")

    await member.kick(reason=reason)

    await message.reply(
        f"👢 تم طرد **{member.display_name}**."
    )
