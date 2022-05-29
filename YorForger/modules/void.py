from pyrogram import filters
from YorForger import pbot
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from telegram import ParseMode

PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"

@pbot.on_message(filters.command(['void']))
async def void(message):
    caption = f"**Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork)** \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"
    buttons = [
        [
            InlineKeyboardButton(
                " 【Usertag】", url="https://t.me/VoidxNetwork/3"),
            InlineKeyboardButton(
                "【Owner Sama】", url="https://t.me/voidaryan")
            ]
    ]   

    await message.effective_message.send_file(photo=PHOTO, caption=caption, reply_markup=InlineKeyboardMarkup(buttons),
    parse_mode=ParseMode.MARKDOWN,)


__help__ = """
 ──「Void Network」──                         
 
❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "【ᴠᴏɪᴅ】"
