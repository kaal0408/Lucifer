import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from Lucifer import LOGS, bot, luciferver
from Lucifer.LuciferConfig import Var
from Lucifer.utils import load_module,start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from Lucifer import CMD_HNDLR

LUCIFER = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


# Luciferbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if var.TG_BOT_USER_NAME_BF_HER is not None:
           print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN_BF_HER",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start() 

# imports plugins...
#path = "Lucifer/plugins/*.py"
#files = glob.glob(path)
#for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/kaal0408/Lucifer"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your LuciferBot Is Now Working ⚡")
LOGS.info(
    "Head to @LuciferXupdates for Updates. Also join chat group to get help regarding to LuciferBot."
)

# that's life...
async def lucifer_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                HELL_PIC,
                caption=f"#START \n\nDeployed LuciferBot Successfully\n\n**Lucifer - {luciferver}**\n\nType {hl}ping or {hl}alive to check! \n\nJoin [Lucifer Channel](t.me/LuciferXupdates) for Updates & [Lucifer Chat](t.me/Lucifer_support_group) for any query regarding Luciferẞø†",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join LuciferBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@LuciferXupdates"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@Lucifer_support_group"))
#    except BaseException:
#        pass


bot.loop.create_task(lucifer_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Luciferbot
