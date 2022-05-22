# Written by @HeisenbergTheDanger (Keep credits else gay)

import asyncio
import os
from telethon.tl.types import InputMediaUploadedPhoto
from Lucifer.utils import admin_cmd

from Lucifer import CMD_HELP


logs_id = os.environ.get("PRIVATE_GROUP_ID", None)

# Keep all credits pls, made with great effort by @HeisenbergTheDanger


async def pinit(chat, msgid):
    try:
        ent = await borg.get_entity(chat)
        if ent and ent.admin_rights:
            await borg.pin_message(chat, msgid)
            return True
        else:
            return False
    except:
        return False


@Lucifer.on(admin_cmd(pattern="forward ?(.*)"))
@Lucifer.on(sudo_cmd(pattern="forward ?(.*)", allow_sudo=True))
async def forw(event):
    if event.fwd_from:
        return
    mssg = await eor(event, "`...'")
    if not event.is_reply:
        await mssg.edit("Reply to a message to broadcast.")
        return
    channels = get_all_channels()
    await mssg.edit("Sending...")
    error_count = 0
    pin_count = 0
    sent_count = 0
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        previous_message.message
        previous_message.raw_text
    error_count = 0
    for channel in channels:
        try:
            fwd_msg = await borg.forward_messages(int(channel.chat_id), previous_message)
            sent_count += 1
            pin_s = await pinit(int(channel.chat_id), fwd_msg.id)
            pin_count = pin_count + 1 if pin_s else pin_count
            await mssg.edit(
                f"Sent : {sent_count}\nError : {error_count}\nTotal : {len(channels)}"
            )
        except Exception as error:
            try:
                await borg.send_message(
                    logs_id, f"Error in sending at {channel.chat_id}."
                )
                await borg.send_message(logs_id, "Error! " + str(error))
                if error == "The message cannot be empty unless a file is provided":
                    mssg.edit(
                        "For sending files, upload in Saved Messages and reply .forward to in."
                    )
                    return
            except BaseException:
                pass
            error_count += 1
            await mssg.edit(
                f"Sent : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
            )
    await mssg.edit(f"{sent_count} messages sent with {error_count} errors.\nAlso Pinned this Message in {pin_count} Chats.")
    if error_count > 0:
        try:
            await borg.send_message(logs_id, f"{error_count} Errors")
        except BaseException:
            await mssg.edit("Set up log channel for checking errors.")



CMD_HELP.update(
    {
        "giveawayhelper": ".add\nUse - Add the channel/group to your database.\
        \n\n.rm (all)<channel/group id>\nUse - Remove the channel/group from database. Use rm all to remove all groups.\
        \n\n.broadcast <reply to message>\nUse - Send the message to all channels/groups in the db.\
        \n\n.forward <reply to polls/stickers>\nUse - Forwards the poll/sticker to all channels/groups in db.\
        \n\n.listchannels\nUse - List all added channels.\
        \n\n.search <channel id>\nUse - Search for the channel name from id."
    }
)
