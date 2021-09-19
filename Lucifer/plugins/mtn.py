"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""


import asyncio

from Lucifer.utils import admin_cmd


@Lucifer.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 19)

    input_str = event.pattern_match.group(1)

    if input_str == "air":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting To AIRTEL NG ....`",
            "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
            "*Optimising Network...*",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▇ █`",
            "**AIRTEL Network Boosted....**",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 19])
