from Lucifer import CMD_HELP
from Lucifer.utils import admin_cmd


@Lucifer.on(admin_cmd(outgoing=True, pattern="group"))
@Lucifer.on(sudo_cmd(allow_sudo=True, pattern="group"))
async def join(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await eor(
            e,
            "This is my community.\n\n[Channel](http://t.me/skyverse01)\n\n[Chat Group](https://t.me/BESTIE30)\n\n[UserBot Tutorial - LuciferBot](https://t.me/Lucifer_support_group)\n\n[LuciferBot Chat](https://t.me/Lucifer_support_group)\n\n[Github](https://github.com/kaal0408)",
        )


CMD_HELP.update({"group": ".group\nUse - None."})
