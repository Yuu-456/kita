from pyrogram import filters
from YorForger import pbot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"

@pbot.on_message(filters.command(['void']))
async def void(_, message):
    caption = f"**Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork)** \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"
    buttons = [
        [
            InlineKeyboardButton(
                text=" 【Usertag】", url="https://t.me/VoidxNetwork/3"),
            InlineKeyboardButton(
                text="【Owner Sama】", url="https://t.me/voidaryan")
            ]
    ]   

    await message.send_file(photo=PHOTO, caption=caption, reply_markup=InlineKeyboardMarkup(buttons))


__help__ = """
 ──「Void Network」──                         
 
❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "【ᴠᴏɪᴅ】"