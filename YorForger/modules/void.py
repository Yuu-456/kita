from pyrogram import filters
from YorForger import pbot, dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)

PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"

# @pbot.on_message(filters.command(['void']))
# async def void(_, message):
#     caption = f"Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork) \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"

#     await message.reply_photo(photo=PHOTO, caption=caption,)


__help__ = """
 ──「Void Network」──                         
 
❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "【ᴠᴏɪᴅ】"








def void(update: Update, context: CallbackContext):

    update.effective_message.reply_photo(
        PHOTO, caption= "Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork) \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈",
        parse_mode=ParseMode.HTML,

            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="【Usertag】", url="https://t.me/void_network/103"),
                InlineKeyboardButton(text="【Owner Sama】", url="https://t.me/voidxtoxic")
                ],
                [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/voidxnetwork")]
            ]
        ),
    )


void_handler = CommandHandler("void", void)
dispatcher.add_handler(void_handler)