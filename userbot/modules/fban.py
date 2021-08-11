#PLUGIN BY @RISHISUPERYO
#THANKS TO KEINSHIN TO FIX THE ERROR BRO
#KANG = KEEP CREDITS ELSE GAY DUDE
#KANGERS DON'T SEE THIS FORGET TO KANG ,IF KANG U ARE READY TO GET A GBAN
#THANKS TO READ
from telethon import events
from userbot import ALIVE_NAME
from userbot import CMD_HELP
@borg.on(CMD_HELP(pattern="fban (.*)"))

async def fban(event):
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else lightning_cmd
    FBAN = previous_message.sender_id
    REASON = event.text.split(" ", maxsplit=1)[1]
    if REASON.strip() == "":
         REASON = " #fban"
    chat ="@Miss_RoseBot"    

    await client.send_message(chat,"/fban {FBAN} {REASON}")
    # Dear NIGGA kanger if you remove id or username which is given below so this plugin will not work...
    if int(FBAN) == 1760947083 or int(FBAN) == 1024689872 or int(FBAN) == 1311769691:    
            await event.edit("𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴 𝚄 𝙰𝚁𝙴 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙵𝙱𝙰𝙽 𝚄𝚁 𝙱𝙰𝙰𝙿")      
    elif FBAN == "@Rishisuperyo" or FBAN == "@CYBER_ARJUN_JAISWAL" or FBAN == "@keinshin":
            await event.edit("𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴 𝚄 𝙰𝚁𝙴 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙵𝙱𝙰𝙽 𝚄𝚁 𝙱𝙰𝙰𝙿")
            return
    await event.edit(f"𝙳𝙴𝙼𝙾𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙵𝙱𝙰𝙽𝙽𝙸𝙶 𝚄 𝙺𝙸𝙳 𝙵𝙾𝚁 **{DEFAULTUSER}** .")
