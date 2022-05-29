# from pyrogram import filters
# from YorForger import pbot

# PHOTO = "https://telegra.ph/file/fa2c031ecf5df678280e5.jpg"

# @pbot.on_message(filters.command(['alive']))
# async def void(_, message):
#     caption = f"**I Am Kita Shinsuke!**\n\n**I Work Under - [Void X Network](t.me/voidxnetwork)** \n\n◈ I will love to be in your groupchat ◈"
    

#     await message.reply_photo(photo=PHOTO, caption=caption)


#     # # BUTTON = [
#     # #     [
#     # #         Button.url("【Support】", "https://t.me/kitaxsupport"),
#     # #         Button.url("【Updates】", "https://t.me/kitaxupdates"),
#     # #     ]
#     # # ]
#     # await pbot.reply_photo(event.chat_id, PHOTO, caption=caption,
#     # # buttons=BUTTON
#     # )


# __help__ = """ 
# ❂ /alive: To check if bot is alive or not."""
   
# __mod_name__ = "Alive"





import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YorForger.events import register
from YorForger import telethn as tbot


PHOTO = "https://telegra.ph/file/2b04f7812f22b983f8a10.mp4"

@register(pattern=("/alive"))
async def alive(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Shikomori Robot.** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **My 'Boyfriend' and original 'Creator' : [Yash](https://github.com/SOME-1HING)**\n\n"
  TEXT += f"⚪ **My Owner : [Sneha](https://t.me/Sneha_UwU_OwO)** \n\n"
  TEXT += f"⚪ **My Manager : [【V๏ɪ፝֟𝔡】](https://t.me/VoidAryan)** \n\n"
  TEXT += f"⚪ **I am Powered by : [【V๏ɪ፝֟𝔡】»Network«](https://t.me/VoidxNetwork)** \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Updates", "https://t.me/Shikimori_bot_Updates"), Button.url("Support", "https://t.me/tyranteyeeee")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
