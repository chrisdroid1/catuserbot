# kangers give credit

import time
from platform import python_version

from telethon import version

from . import StartTime, catversion, get_readable_time, ALIVE_NAME, mention, reply_id

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Creminal"

CAT_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "⚠️ MY CREMINAL BOT IS ALIVE ⚠️"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "⚠️"


@bot.on(admin_cmd(outgoing=True, pattern="salive$"))
@bot.on(sudo_cmd(pattern="salive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"<b>{CUSTOM_ALIVE_TEXT}</b>\n\n"

        cat_caption += f"☞ ** MY SYSTEM STATUS**\n"

        cat_caption += (
            f"<b>{EMOJI}  **Telethon Version:** </b> <code>{version.__version__}</code>\n"
        )

        cat_caption += (
            f"<b>{EMOJI} **Python Version:** </b> <code>{python_version()}</code>\n"
        )

        cat_caption += f"<b>{EMOJI} **Uptime** : `{uptime}` \n"

        cat_caption += f"<b>{EMOJI} **Database :**  </b> <code>{check_sgnirts}</code>\n"

        cat_caption += (
            f"<b>{EMOJI} **Creminal Version** : </b> <code>{catversion}</code>\n"
        )

        cat_caption += (
            f"↼🤠🄱🄾🅂🅂🤠⇀\n**『 [{DEFAULTUSER}] 』**\n\n"
        )

        cat_caption += "    <a href = https://github.com/chrisdroid1/Creminal><b>🎇REPO🎇</b></a> 🔹 <a href = https://t.me/CreminalUBotSupport><b>Group</b></a> 🔹 <a href = https://t.me/CreminalUBot><b>Channel</b></a>"
        await alive.client.send_file(
            alive.chat_id,
            CAT_IMG,
            caption=cat_caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"{CUSTOM_ALIVE_TEXT}\n\n"

            f" __↼🤠🄱🄾🅂🅂🤠⇀__\n『 [{DEFAULTUSER}] 』\n\n"

            f"<b> MY SYSTEM STATUS</b>\n"

            f"<b>{EMOJI}} Uptime :</b> <code>{uptime}</code>\n"

            f"<b>{EMOJI} Telethon version :</b> <code>{version.__version__}</code>\n"

            f"<b>{EMOJI} Creminal Version :</b> <code>{catversion}</code>\n"

            f"<b>{EMOJI} Database :</b> <code>{check_sgnirts}</code>\n"    
    
            f"<b>{EMOJI} Python Version: </b> <code>{python_version()}</code>\n\n"

            "    <a href = https://github.com/chrisdroid1/Creminal><b>🎇REPO🎇</b></a> 🔹 <a href = https://t.me/CreminalUBotSupport><b>Group</b></a> 🔹 <a href = https://t.me/CreminalUBot><b>Channel</b></a>",
            parse_mode="html",
        )
        
@bot.on(admin_cmd(outgoing=True, pattern="sialive$"))
@bot.on(sudo_cmd(pattern="sialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    reply_to_id = await reply_id(alive)
    cat_caption = f"**Creminal is Up and Running**\n"

    cat_caption += f"**  -Boss :** {mention}\n"

    cat_caption += f"**  -Telethon version :** `{version.__version__}\n`"

    cat_caption += f"**  -Creminal Version :** `{catversion}`\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "__**PLUGIN NAME :** Alive__\
      \n\n📌** CMD ➥** `.salive`\
      \n**USAGE   ➥  **To see wether your bot is working or not.\
      \n\n📌** CMD ➥** `.sialive`\
      \n**USAGE   ➥  **__Status of bot will be showed by inline mode with button__."
    }
)
