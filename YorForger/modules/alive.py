# import os
# import re
# from platform import python_version as kontol
# from telethon import events, Button
# from telegram import __version__ as telever
# from telethon import __version__ as tlhver
# from pyrogram import __version__ as pyrover
# from YorForger.events import register
# from YorForger import telethn as tbot


# PHOTO = "https://telegra.ph/file/fa2c031ecf5df678280e5.jpg"


# @register(pattern=("/alive"))
# async def awake(event):
#     TEXT = f"**Hey There Team Mates!![{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
#     TEXT += f"**I Am Kita Shinsuke!**\n\n"
#     TEXT += f"**I Work Under - [Void X Network](t.me/voidxnetwork)**** \n\n"
#     TEXT += "◈ I will love to be in your groupchat ◈"
#     BUTTON = [
#         [
#             Button.url("【Support】", "https://t.me/kitaxsupport"),
#             Button.url("【Updates】", "https://t.me/kitaxupdates"),
#         ]
#     ]
#     await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)


from pyrogram import filters
from YorForger import pbot
from telethon import Button

PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"

@pbot.on_message(filters.command(['void']))
async def void(event):
    caption = f"**I Am Kita Shinsuke!**\n\n**I Work Under - [Void X Network](t.me/voidxnetwork)** \n\n◈ I will love to be in your groupchat ◈"

    # BUTTON = [
    #     [
    #         Button.url("【Support】", "https://t.me/kitaxsupport"),
    #         Button.url("【Updates】", "https://t.me/kitaxupdates"),
    #     ]
    # ]
    await pbot.send_file(event.chat_id, PHOTO, caption=caption,
    # buttons=BUTTON
    )


help = """
 ──「Void Network」──                         
 
❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
mod_name = "【ᴠᴏɪᴅ】"