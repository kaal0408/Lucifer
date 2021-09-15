# For @Lucifer_support_group
"""Check if your userbot is working."""
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Lucifer import ALIVE_NAME, CMD_HELP, luciferver
from Lucifer.__init__ import StartTime
from Lucifer.LuciferConfig import Config, Var

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None
lucifermoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✵**"
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


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Lucifer_support_group"


@Lucifer.on(admin_cmd(outgoing=True, pattern="alive"))
@Lucifer.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        lucifer = f"**Welcome To LuciferBot **\n\n"
        lucifer += f"`{CUSTOM_ALIVE}`\n\n"
        lucifer += (
            f"{luciferemoji} **Telethon version**: `1.17`\n{lucifermoji} **Python**: `3.8.3`\n"
        )
        lucifer += f"{luciferemoji} **LuciferBot Version**: `{luciferver}`\n"
        tele += f"{luciferemoji} **More Info**: @Lucifer_support_group\n"
        lucifer += f"{luciferemoji} **Sudo** : `{sudo}`\n"
        lucifer += f"{luciferemoji} **LuciferBot Uptime**: `{uptime}`\n"
        lucifer += f"{luciferemoji} **Database Status**: `All OK 👌!`\n"
        lucifer += (
            f"{luciferemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
        )
        lucifer += "    [✨ GitHub Repository ✨](https://github.com/kaal0408/Lucifer"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=lucifer, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/0670190de8e3bddea6d95.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**Welcome To LuciferBot **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{luciferemoji} **Telethon version**: `1.17`\n{lucifermoji} **Python**: `3.8.3`\n"
            f"{luciferemoji} **LuciferBot Version**: `{telever}`\n"
            f"{luciferemoji} **More Info**: @Lucifer_support_group\n"
            f"{luciferemoji} **Sudo** : `{sudo}`\n"
            f"{luciferemoji} **TeleBot Uptime**: `{uptime}`\n"
            f"{luciferemoji} **Database Status**: `All OK 👌!`\n"
            f"{luciferemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/kaal0408/Lucifer)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()


CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})
