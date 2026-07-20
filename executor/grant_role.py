import discord


async def grant_role(guild, message, data):

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

    await member.add_roles(role)

    await message.reply(
        f"✅ تم إعطاء رتبة **{role_name}** إلى **{member.display_name}**."
    )
