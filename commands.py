import discord
from discord import app_commands

from config import ALLOWED_ROLE_ID
from events import enabled_guilds


def setup_commands(bot):

    @bot.tree.command(
        name="enable",
        description="Enable F7 Bot"
    )
    async def enable(interaction: discord.Interaction):

        # التأكد من الرتبة
        if not any(role.id == ALLOWED_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ ليس لديك صلاحية لاستخدام هذا الأمر.",
                ephemeral=True
            )
            return

        enabled_guilds.add(interaction.guild.id)

        await interaction.response.send_message(
            "✅ تم تفعيل F7 Bot.",
            ephemeral=True
        )


    @bot.tree.command(
        name="disable",
        description="Disable F7 Bot"
    )
    async def disable(interaction: discord.Interaction):

        # التأكد من الرتبة
        if not any(role.id == ALLOWED_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ ليس لديك صلاحية لاستخدام هذا الأمر.",
                ephemeral=True
            )
            return

        enabled_guilds.discard(interaction.guild.id)

        await interaction.response.send_message(
            "🛑 تم إيقاف F7 Bot.",
            ephemeral=True
        )
