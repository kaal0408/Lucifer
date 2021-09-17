import asyncio
from collections import deque

from Lucifer import CMD_HELP
from Lucifer.utils import admin_cmd


@Lucifer.on(admin_cmd(pattern=r"earth", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update({"earth": ".earth\nUse - useless."})
