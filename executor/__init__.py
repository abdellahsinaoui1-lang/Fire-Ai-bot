from .create_channel import create_channel
from .create_category import create_category
from .create_role import create_role


async def execute_command(bot, message, command):

    for key, data in command.items():

        if key.startswith("CreateChannel"):
            await create_channel(message.guild, message, data)

        elif key.startswith("CreateCategory"):
            await create_category(message.guild, message, data)

        elif key.startswith("CreateRole"):
            await create_role(message.guild, message, data)

        else:
            await message.reply(
                f"❌ الأمر **{key}** غير مدعوم حالياً."
            )
