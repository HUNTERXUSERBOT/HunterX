

import asyncio
import random
from telethon import events, version
from userbot import hunterversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ʜᴜɴᴛᴇʀx"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

hunter = bot.uid

HUNTERX_IMG = Config.ALIVE_PIC or " https://te.legra.ph/file/d3ba982dab7415cfe951c.jpg"
pm_caption = "  __**🎭𝙃𝙐𝙉𝙏𝙀𝙍𝙓 𝙄𝙎 𝘼𝙇𝙄𝙑𝙀🎭**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 👑𝐌𝐀𝐒𝐓𝐄𝐑👑\n  **『😈[{DEFAULTUSER}](tg://user?id={hunter})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `Version:` `{hunterversion}`\n"
pm_caption += f"┣•➳➠ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `Channel:` [ᴊᴏɪɴ](https://t.me/HunTerXsuPPorT)\n"
pm_caption += f"┣•➳➠ `Creator:` [HUNTER](https://t.me/UNK_HUNTER)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥REPO🔥](https://github.com/Parth651-45/hunterX) 🔹 [📜License📜](https://github.com/Parth651-45/hunterX/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, HUNTERX_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
