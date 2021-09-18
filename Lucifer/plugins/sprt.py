# python 3.7.1

"""Available Commands:
.support"""


import asyncio

from Lucifer.utils import admin_cmd


@Lucifer.on(admin_cmd(pattern="(.*)"))
@Lucifer.on(sudo_cmd(pattern="(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "support":
        await eor(event, input_str)
        animation_chars = [
            "Hello,",
            "Hello, do you need support?",
            "Then join the support group.",
            "[Join Now](t.me/Lucifer_support_group)",
            "[SUPPORT GROUP](t.me/Lucifer_support_group)",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await eor(event, animation_chars[i % 5])
