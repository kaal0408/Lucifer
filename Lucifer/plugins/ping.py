# special thanks to Sur_vivor
# Re-written for Lucifer by @its_xditya

import time
from datetime import datetime

from Lucifer import CMD_HELP
from Lucifer.__init__ import StartTime
from Lucifer.plugins import ALIVE_NAME, OWNER_ID

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lucifer user"


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


# @command(pattern="^.ping$")


@Lucifer.on(admin_cmd(pattern="ping$"))
@Lucifer.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    x = await eor(event, "⛝ ＰＯＮＧ! ⛝")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    await x.edit(
        f"MY MASTER\nI AM ON\n\n✘ **ριиg** : `{ms}`\n✘ **uptime** : `{uptime}`\n✘ **MY MASTER** : [{DEFAULTUSER}](tg://user?id={OWNER_ID})\n\n© 𝙻ucifer 𝚄𝚂𝙴𝚁𝙱𝙾𝚃"
    )


CMD_HELP.update({"ping": ".ping\nUse - See the ping stats and uptime of userbot."})
