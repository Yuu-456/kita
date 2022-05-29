import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YorForger.events import register
from YorForger import telethn as tbot


PHOTO = "https://telegra.ph/file/dbf5b416000d948b0fdca.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hey There Team Mates!![{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
    TEXT += f"**I Am Kita Shinsuke!**\n\n"
    TEXT += f"**I Work Under - [Void X Network](t.me/voidxnetwork)**** \n\n"
    TEXT += "◈ I will love to be in your groupchat ◈"
    BUTTON = [
        [
            Button.url("【Support】", "https://t.me/kitaxsupport"),
            Button.url("【Updates】", "https://t.me/kitaxupdates"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
