from .create_channel import create_channel
from .create_category import create_category
from .create_role import create_role

from .delete_channel import delete_channel
from .delete_category import delete_category
from .delete_role import delete_role

from .grant_role import grant_role
from .remove_role import remove_role

from .ban import ban_member
from .kick import kick_member
from .timeout import timeout_member

from .purge import purge_messages
from .send_message import send_message


async def execute_command(bot, message, command):

    for key, data in command.items():

        # ===========================
        # Create
        # ===========================

        if key.startswith("CreateChannel"):

            await create_channel(
                message.guild,
                message,
                data
            )

        elif key.startswith("CreateCategory"):

            await create_category(
                message.guild,
                message,
                data
            )

        elif key.startswith("CreateRole"):

            await create_role(
                message.guild,
                message,
                data
            )

        # ===========================
        # Delete
        # ===========================

        elif key.startswith("DeleteChannel"):

            await delete_channel(
                message.guild,
                message,
                data
            )

        elif key.startswith("DeleteCategory"):

            await delete_category(
                message.guild,
                message,
                data
            )

        elif key.startswith("DeleteRole"):

            await delete_role(
                message.guild,
                message,
                data
            )

        # ===========================
        # Roles
        # ===========================

        elif key.startswith("GrantRole"):

            await grant_role(
                message.guild,
                message,
                data
            )

        elif key.startswith("RemoveRole"):

            await remove_role(
                message.guild,
                message,
                data
            )

        # ===========================
        # Members
        # ===========================

        elif key.startswith("BanMember"):

            await ban_member(
                message.guild,
                message,
                data
            )

        elif key.startswith("KickMember"):

            await kick_member(
                message.guild,
                message,
                data
            )

        elif key.startswith("TimeoutMember"):

            await timeout_member(
                message.guild,
                message,
                data
            )

        # ===========================
        # Messages
        # ===========================

        elif key.startswith("PurgeMessages"):

            await purge_messages(
                message.guild,
                message,
                data
            )

        elif key.startswith("SendMessage"):

            await send_message(
                message.guild,
                message,
                data
            )

        # ===========================
        # No Skill
        # ===========================

        elif key.startswith("NoSkill"):

            await message.reply(
                data["Reply"]
            )

        # ===========================
        # Unknown
        # ===========================

        else:

            await message.reply(
                f"❌ الأمر **{key}** غير مدعوم حالياً."
            )
