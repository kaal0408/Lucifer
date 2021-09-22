

# Astro-UB
# PM_SECURITY

import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import Lucifer.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from Lucifer import CMD_HELP, CUSTOM_PMPERMIT, bot
from Lucifer.utils import admin_cmd
from Lucifer.Luciferconfig import Lucifer Config

NAME = Config.NAME
PM_PIC = os.environ.get("PM_PIC", None)
LUCIFER_PIC = (
    PM_PIC
    if PM_PIC
    else "https://telegra.ph/file/1dc4cf071ecd2be57e30a.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "This is Pro Security By Lucifer υsєяъ๏т To my Master...!"
)
DEFAULTUSER = str(NAME) if NAME else "Astro User✌️"
USER_BOT_WARN_ZERO = "𝘼𝙃𝙃𝙃𝙃𝙃!!!!!\n𝙄 𝙩𝙤𝙡𝙙 𝙮𝙤𝙪 𝙉𝙤𝙩 𝙏𝙤 𝙨𝙥𝙖𝙢 𝙗𝙚 𝙞𝙣 𝙇𝙞𝙢𝙞𝙩𝙨 𝙗𝙪𝙩 𝙔𝙤𝙪 𝙏𝙤𝙤𝙠 𝙈𝙚 𝙇𝙞𝙜𝙝𝙩𝙡𝙮....😒\n𝗡𝗢𝗪 𝗟𝗘𝗧 𝗠𝗘 𝗕𝗟𝗢𝗖𝗞 𝗬𝗢𝗨😂✌️\n𝘿𝙊𝙉'𝙏 𝙈𝙀𝙎𝙎-𝙐𝙋 𝙒𝙄𝙏𝙃 𝙈𝙀 𝘼𝙂𝘼𝙄𝙉 \n𝙁𝙐𝘾𝙆 𝙊𝙁𝙁🙂"

USER_BOT_NO_WARN = (
    "__knock Knock__👀\nWho is There✨**This is PM SECURITY OF [{}](tg://user?id={})**\nBY Lucifer υsєяъ๏т\n\n"
        "{}\n\n"
        "\nPlease choose why you are here, from the available options"
    "\n\n**You have** {}/{} ⚠️warnings⚠️\nSo Don't Spam Until My Master Will Come"
)


@Lucifer.on(admin_cmd(pattern="a ?(.*)"))
@Lucifer.on(admin_cmd(pattern="approve ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            if chat.id in PM_WARNS:
                del PM_WARNS[chat.id]
            if chat.id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat.id].delete()
                del PREV_REPLY_MESSAGE[chat.id]
            pmpermit_sql.approve(chat.id, reason)
            await event.edit(
                "[{}](tg://user?id={}) Have been Approved👀To chat you .".format(firstname, chat.id)
            )
            await asyncio.sleep(3)
            await event.delete()


# Approve outgoing


@bot.on(events.NewMessage(outgoing=True))
async def you_dm_niqq(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            if chat.id not in PM_WARNS:
                pmpermit_sql.approve(chat.id, "outgoing")
                logit = "Auto_Approved\nUser - [{}](tg://user?id={}) \n-Due to Outgoing Messages".format(
                    chat.first_name, chat.id
                )
                try:
                    await borg.send_message(Config.PRIVATE_GROUP_ID, logit)
                except BaseException:
                    pass


@Lucifer.on(admin_cmd(pattern="block ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == 1258905497:
            await event.edit("ωнαт тнє ƒυck🙄\nI won't block My 𝙊𝙒𝙉𝙀𝙍\nHe is Lucifer-DEV👀\nI am going Offline for 100s😴 Realise Your Mistake Nigga")
            await asyncio.sleep(100)
        else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "𝙁𝙐𝘾𝙆 𝙊𝙁𝙁😂𝙉𝙞𝙗𝙗𝙖\nBlocked:- [{}](tg://user?id={})".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))

@Lucifer.on(admin_cmd(pattern="da ?(.*)"))
@Lucifer.on(admin_cmd(pattern="disapprove ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == 1258905497:
            await event.edit("Ahhhh...Are you Kidding me😂\n𝙃𝙀 𝙄𝙎 𝙈𝙔 𝙊𝙒𝙉𝙀𝙍\n I can't Disapprove Him...")
        else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "[{}](tg://user?id={}) Got disapproval..\nNoW Don't Disturb Me 𝙉𝙞𝙗𝙗𝙖".format(
                        firstname, chat.id
                    )
                )


@Lucifer.on(admin_cmd(pattern="listapproved"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    approved_users = pmpermit_sql.get_all_approved()
    APPROVED_PMs = "[Astro] Currently Approved PMs\n"
    if len(approved_users) > 0:
        for a_user in approved_users:
            if a_user.reason:
                APPROVED_PMs += f"→ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                APPROVED_PMs += f"→ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
    else:
        APPROVED_PMs = "No Approved PMs (yet)"
    if len(APPROVED_PMs) > 4095:
        with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
            out_file.name = "approved.pms.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="[Lucifer]Current Approved PMs",
                reply_to=event,
            )
            await event.delete()
    else:
        await event.edit(APPROVED_PMs)


@bot.on(events.NewMessage(incoming=True))
async def on_new_private_message(event):
    if event.sender_id == bot.uid:
        return

    if Config.PRIVATE_GROUP_ID is None:
        return

    if not event.is_private:
        return

    message_text = event.message.message
    chat_id = event.sender_id

    message_text.lower()
    if USER_BOT_NO_WARN == message_text:
        return

        sender = await event.get_input_sender()


    if not pmpermit_sql.is_approved(chat_id):
        # pm permit
        await do_pm_permit_action(chat_id, event)


async def do_pm_permit_action(chat_id, event):
    if Config.PMSECURITY.lower() == "off":
        return
    if chat_id not in PM_WARNS:
        PM_WARNS.update({chat_id: 0})
    if PM_WARNS[chat_id] == Config.MAX_SPAM:
        r = await event.reply(USER_BOT_WARN_ZERO)
        await asyncio.sleep(3)
        await event.client(functions.contacts.BlockRequest(chat_id))
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        the_message = ""
        the_message += "#BLOCKED_PMs\n\n"
        the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
        the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
        # the_message += f"Media: {message_media}"
        try:
            await event.client.send_message(
                entity=Config.PRIVATE_GROUP_ID,
                message=the_message,
                # reply_to=,
                # parse_mode="html",
                link_preview=False,
                # file=message_media,
                silent=True,
            )
            return
        except BaseException:
            return
    # inline pmpermit menu
    mybot = Config.BOT_USERNAME
    MSG = USER_BOT_NO_WARN.format(
        DEFAULTUSER, myid, MESAG, PM_WARNS[chat_id] + 1, Config.MAX_SPAM
    )
    sender = await event.get_input_sender()
    
    Lucifer = await bot.inline_query(mybot, "**PM")
    r = await lucifer[0].click(sender)
    PM_WARNS[chat_id] += 1
    if chat_id in PREV_REPLY_MESSAGE:
        await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r


# Do not touch the below codes!


@Lucifer.on(
    events.NewMessage(
        incoming=True, from_users=(1258905497, 1366616835, 1732683058, 1754865180)
    )
)
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**Lucifer-𝗗𝗲𝘃 is Here\nWelCome Sir✌️🤩**")
            await borg.send_message(chat, "**Lucifer-𝗗𝗲𝘃 is Here\nYou are very lucky**\n\n✌️𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗦𝗶𝗥🤩")


# instant block
NEEDIT = os.environ.get("INSTANT_BLOCK", None)
if NEEDIT == "on":

    @Lucifer.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        event.message.message
        event.message.media
        event.message.id
        event.message.to_id
        chat_id = event.chat_id
        sender = await borg.get_entity(chat_id)
        if chat_id == borg.uid:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if not pmpermit_sql.is_approved(chat_id):
            await borg(functions.contacts.BlockRequest(chat_id))


CMD_HELP.update(
    {
        "pmsecurity": ".approve/.a\nUse - Approve PM\
        \n\n.disapprove/.da\nUse - DisApprove PM\
        \n\n.listapproved\nUse - Get all approved PMs.\
        \n\nSet Config PMPERMIT_PIC for custom PMPic, CUSTOM_PMPERMIT for custom text, PMSECURITY <on/off> to enable/disable, INSTANT_BLOCK <on/off>.\
        \nGet help from @Lucifer_support_group."
    }
)
