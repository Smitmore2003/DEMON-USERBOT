# Copyright (C) 2021 The Mahadev Company LLC.
#
# Licensed under the MahaDev Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

from userbot import CMD_HELP DEFAULTUSER
from userbot.events import register


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def help(event):
    """For .help command."""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Error!**`{args}` **not a valid module name**")
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("⚡")
        await asyncio.sleep(2.5)
        await event.edit(f"**[⚡Demon-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡](t.me/LynxUserbot)**\n\n"
                         f"**◑» Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◑» Pʟᴜɢɪɴ : {len(modules)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"╰►| {string} ◄─\n\n"
                         f"**License : [Raphielscape Public License 1.d](https://github.com/SRIDHAR2021SIDDHARTH/DEMON-USERBOT/blob/DEMON-USERBOT/LICENSE)**\n"
                         f"**Copyright © 2021 [Demon-Userbot LLC Company](https://github.com/SRIDHAR2021SIDDHARTH/DEMON-USERBOT/)**")
        await event.reply(f"\n**Example** : Type » `.help admin` For Admin Plugin Usage Information.")
        await asyncio.sleep(1000)
        await event.delete()
