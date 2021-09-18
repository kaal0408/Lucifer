"""Emoji
Available Commands:
.np
"""


import asyncio

from Lucifer.utils import admin_cmd


@Lucifer.on(admin_cmd(pattern="np"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "np":
    await event.edit("np")
    animation_chars = [
        "No",
        "Problem",
        "Sar 😇",
        "No Problem Sar 😇",
        "No Problem Sar 😇. Jao",
        "No Problem Sar 😇. Jao na",
        "No Problem Sar 😇. Jaoo jata kyu nhi",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
