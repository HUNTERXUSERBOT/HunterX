from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, hunterxversion
from pathlib import Path
import asyncio
import telethon.utils

HUNTERX_PIC = Config.ALIVE_PIC or "https://te.legra.ph/file/d3ba982dab7415cfe951c.jpg"

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting HunterX")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("HunterX Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""HUNTERX IS ON!!! HUNTERX VERSION :- {hunterxversion} YOUR HUNTERX IS READY TO USE! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @HunTerXsuPPorT .""")
async def mafia_is_on():
    try:
        if Config.HUNTERX_LOGGER != 0:
            await bot.send_file(
                Config.HUNTERX_LOGGER,
                MAFIA_PIC,
                caption=f"𝙱𝙰𝙰𝙿 𝙱𝙾𝙻𝚃𝙴 𝙷𝚄𝙽𝚃𝙴𝚁 𝚇\n\n**𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ➪ {hunterxversion}**\n\n𝐓𝐲𝐩𝐞 `.ping` or `.alive` 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤! \n\n𝙹𝙾𝙸𝙽 [𝙷𝚄𝙽𝚃𝙴𝚁 𝚇 𝙲𝙷𝙰𝚃](t.me/HunTerXsuPPorT) 𝚃𝙾 𝚀𝚄𝙴𝚁𝚈 & 𝙹𝙾𝙸𝙽 [ 𝙷𝚄𝙽𝚃𝙴𝚁 𝚇 𝚄𝙿𝙳𝙰𝚃𝙴𝚂](t.me/HunTerXoFFiCiAl) 𝚃𝙾 𝙺𝙽𝙾𝚆 𝚁𝙴𝙶𝚁𝙰𝙳𝙸𝙽𝙶 𝚄𝙿𝙳𝙰𝚃𝙴 𝙰𝙽𝙳 𝙽𝙴𝚆𝚂 𝙰𝙱𝙾𝚄𝚃 𝙷𝚄𝙽𝚃𝙴𝚁 𝚇",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(mafia_is_on())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
