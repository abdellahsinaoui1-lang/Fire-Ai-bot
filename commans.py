import discord
from discord import app_commands
from discord.ext import commands

from config import ALLOWED_ROLE_ID

# حالة البوت
bot_enabled = True


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def has_role(self, interaction: discord.Interaction):
        return any(role.id == ALLOWED_ROLE_ID for role in interaction.user.roles)

    @app_commands.command(
        name="enable",
        description="تشغيل البوت"
    )
    async def enable(self, interaction: discord.Interaction):

        global bot_enabled

        if not self.has_role(interaction):
            await interaction.response.send_message(
                "❌ ليس لديك صلاحية.",
                ephemeral=True
            )
            return

        bot_enabled = True

        await interaction.response.send_message(
            "✅ تم تشغيل البوت.",
            ephemeral=True
        )

    @app_commands.command(
        name="disable",
        description="إيقاف البوت"
    )
    async def disable(self, interaction: discord.Interaction):

        global bot_enabled

        if not self.has_role(interaction):
            await interaction.response.send_message(
                "❌ ليس لديك صلاحية.",
                ephemeral=True
            )
            return

        bot_enabled = False

        await interaction.response.send_message(
            "⛔ تم إيقاف البوت.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
