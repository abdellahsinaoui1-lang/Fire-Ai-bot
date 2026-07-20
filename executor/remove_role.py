import discord


async def remove_role(guild, message, data):

    member_name = data["Member"]
    role_name = data["Role"]

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

    role = discord.utils.get(
        guild.roles,
        name=role_name
    )

    if role is None:

        await message.reply(
            f"❌ لم أجد الرتبة **{role_name}**."
        )

        return

    await member.remove_roles(role)

    await message.reply(
        f"✅ تمت إزالة رتبة **{role_name}** من **{member.display_name}**."
    )
