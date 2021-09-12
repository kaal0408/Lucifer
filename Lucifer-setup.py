#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""𝙿𝙻𝙴𝙰𝚂𝙴 𝙶𝙾 𝚃𝙾 my.telegram.org
𝙻𝙾𝙶𝙸𝙽 𝚄𝚂𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝙲𝙲𝙾𝚄𝙽𝚃
𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 𝙰𝙿𝙸 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙼𝙴𝙽𝚃 𝚃𝙾𝙾𝙻𝚂
𝙲𝚁𝙴𝙰𝚃𝙴 𝙰 𝙽𝙴𝚆 𝙰𝙿𝙿𝙻𝙸𝙲𝙰𝚃𝙸𝙾𝙽, 𝙱𝚈 𝙴𝙽𝚃𝙴𝚁𝙸𝙽𝙶 𝚁𝙴𝚀𝚄𝙸𝚁𝙴𝙳 𝙳𝙴𝚃𝙰𝙸𝙻𝚂
𝚃𝙴𝙰𝙼 𝙻ucifer
 

Running Lucifer Fire on Termux 🔥🔥🔥🔥....
""")
print("")

APP_ID = int(input("𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙰𝙿𝙸 𝙷𝙴𝚁𝙴 ➙ "))
API_HASH = input("𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙰𝙿𝙸 𝙷𝙰𝚂𝙷 𝙷𝙴𝚁𝙴 ➙ ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    tele = client.send_message("me", client.session.save())
    tele.reply(
        "✘ Hᴇʀᴇ ɪs ʏᴏᴜʀ `STRING_SESSION` Oғ Lucifer ᴜsᴇʀʙᴏᴛ ✘.\n@LuciferXsupport")
    print("")
    print("Bᴇʟᴏᴡ ɪs ʏᴏᴜʀ STRING_SESSION. Wᴇ ʜᴀᴠᴇ ᴀʟsᴏ sᴛᴏʀᴇᴅ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ sᴀᴠᴇ ᴍᴇssᴀɢᴇs")
    print("")
    print("")
    print(client.session.save())
