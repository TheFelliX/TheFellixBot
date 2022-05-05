import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from ShuKurenaiXRoBot.events import register
from ShuKurenaiXRoBot import telethn as tbot


PHOTO = "https://telegra.ph/file/404fcd39fb74f79e5c9e7.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm The FelliX Bot.** \n\n"
    TEXT += "⚪ **I'm Working Properly** \n\n"
    TEXT += f"⚪ **Managed By : [Nikhil](https://t.me/XeD_Nikhil)** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/FelliXRobot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/AquaBotsChat"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
