from telethon.tl.types import Channel

from Lucifer import *
from Lucifer import ALIVE_NAME, bot, luciferver
from Lucifer.LuciferConfig import Config, Var

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

LuciferUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lucifer user"

lucifer = f"lucifer𝚅𝙴𝚁𝚂𝙸𝙾𝙽: {luciferver}\n"
lucifer += f"𝙻𝙾𝙶 𝙶𝚁𝙾𝚄𝙿: {log}\n"
lucifer += f"𝙼𝚈 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙾𝚃: {bots}\n"
lucifer += f"𝙻𝚈𝙳𝙸𝙰: {lyd}\n"
lucifer += f"𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁: {sudo}\n"
lucifer += f"𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈: {pm}\n"
lucifer += f"\n𝚅𝙸𝚂𝙸𝚃 @Lucifer 𝙵𝙾𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.\n"
luciferstats = f"{lucifer}:@Lucifer_support_group"

LUCIFER_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def Lucifer_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
