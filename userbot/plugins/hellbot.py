

"""Plugin for HellBot Repo

\nCode by @UNK_HUNTER

type '.hellbot' to get HellBot repo
"""

import random, re
from hunterx.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="hellbot ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Click [here](https://github.com/The-HellBot/HellBot) to open this 🔥**Lit AF!!**🔥 **Hêllẞø†** Repo.. Join channel :- @Its_HellBot Repo Uploaded By @MafiaBot_Support")
    
  
