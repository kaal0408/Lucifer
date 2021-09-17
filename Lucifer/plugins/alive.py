# LuciferX
# © Alone_Loverboy
# For LuciferX
# ®

import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Lucifer import ALIVE_NAME, CMD_HELP, luciferver
from Lucifer import StartTime
from Lucifer.LuciferConfig import Var

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "**Your LuciferX in working.**"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

start = datetime.now()
myid = bot.uid
end = datetime.now()
(end - start).microseconds / 1000
uptime = get_readable_time((time.time() - StartTime))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LuciferX User❤️"

yes = "[•LuciferX•](https://t.me/LuciferXUpdates)"

edits = f"""
    \n•L U C I F E R X•\n
       \n    {CUSTOM_ALIVE}\
    ╔━━━━━━━━━━━━━━━━━━╕
    ┣ Owner: {DEFAULTUSER}
    ┣ Vision- {luciferver}
    ┣ UpTime - {uptime}
    ┣ Python - 3.9.7
    ┣ Telethon - 1.23.0
    ┣ Updates: {yes}
    ╚━━━━━━━━━━━━━━━━━━╛
    """
@bot.on(admin_cmd(outgoing=True, pattern="alive"))
@bot.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
        if ALV_PIC: 
            await bot.send_file(alive.chat_id, ALV_PIC, caption=edits, link_preview=False)
        else:
            await bot.send_message(alive.chat_id, edits, link_preview=False)
        await alive.delete()

CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})
