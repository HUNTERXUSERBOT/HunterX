

import asyncio
import random
from telethon import events, version
from userbot import hunterversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Κα΄Ι΄α΄α΄Κx"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

hunter = bot.uid

HUNTERX_IMG = Config.ALIVE_PIC or " https://te.legra.ph/file/d3ba982dab7415cfe951c.jpg"
pm_caption = "  __**π­πππππππ ππ πΌπππππ­**__\n\n"

pm_caption += f"**ββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 ππππππππ\n  **γπ[{DEFAULTUSER}](tg://user?id={hunter})πγ**\n\n"
)
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += f"β£β’β³β  `Telethon:` `{version.__version__}` \n"
pm_caption += f"β£β’β³β  `Version:` `{hunterversion}`\n"
pm_caption += f"β£β’β³β  `Sudo:` `{sudou}`\n"
pm_caption += f"β£β’β³β  `Channel:` [α΄α΄ΙͺΙ΄](https://t.me/HunTerXsuPPorT)\n"
pm_caption += f"β£β’β³β  `Creator:` [HUNTER](https://t.me/UNK_HUNTER)\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += " [π₯REPOπ₯](https://github.com/Parth651-45/hunterX) πΉ [πLicenseπ](https://github.com/Parth651-45/hunterX/blob/main/LICENSE)"

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
