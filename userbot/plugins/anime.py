import re

from hunterx import bot
from hunterxutils import admin_cmd, sudo_cmd, edit_or_reply
from hunterx.cmdhelp import CmdHelp
from hunterxhelpers.functions import deEmojify
from userbot.Config import Config
from . import *

@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(h1m4n5hu0p):
    hunter = hunterxuserbot.pattern_match.group(1)
    if not hunter:
        if hunterxuserbot.is_reply:
            (await hunterxuserbot.get_reply_message()).message
        else:
            await edit_or_reply(hunterx, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(mafia))}")

    await troll[0].click(
        hunter.chat_id,
        reply_to=hunterxuserbot.reply_to_msg_id,
        silent=True if  hunterxuserbot.is_reply else False,
        hide_via=True,
    )
    await hunterxuserbot.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
