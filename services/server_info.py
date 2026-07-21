import discord


def get_server_info(guild: discord.Guild):

    info = []

    info.append(f"Server Name: {guild.name}")

    # ==========================
    # Members
    # ==========================

    info.append("\nMembers:")

    for member in guild.members:
        if not member.bot:
            info.append(f"- {member.display_name}")

    # ==========================
    # Roles
    # ==========================

    info.append("\nRoles:")

    for role in guild.roles:
        if role.name != "@everyone":
            info.append(f"- {role.name}")

    # ==========================
    # Categories
    # ==========================

    info.append("\nCategories:")

    for category in guild.categories:
        info.append(f"- {category.name}")

    # ==========================
    # Channels
    # ==========================

    info.append("\nChannels:")

    for channel in guild.channels:
        info.append(f"- {channel.name}")

    return "\n".join(info)
