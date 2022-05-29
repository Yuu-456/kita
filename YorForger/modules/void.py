import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YorForger.events import register
from YorForger import telethn as tbot


PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"

@register(pattern=("/void"))
async def awake(event):
    TEXT = f"**Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork)** \n\n"
    TEXT += "◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"
    BUTTON = [
        [
            Button.url("【Usertag】", "https://t.me/VoidxNetwork/3"),
            Button.url("【Owner Sama】", "https://t.me/voidaryan"),
        ]
    ]   
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

__help__ = """
 ──「Void Network」──                         
 
❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "【ᴠᴏɪᴅ】"