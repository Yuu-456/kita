from pyrogram import filters
from YorForger import pbot

PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"

@pbot.on_message(filters.command(['alive']))
async def void(_, message):
    caption = f"**I Am Kita Shinsuke!**\n\n**I Work Under - [Void X Network](t.me/voidxnetwork)** \n\n◈ I will love to be in your groupchat ◈"
    

    await message.reply_photo(photo=PHOTO, caption=caption)


    # # BUTTON = [
    # #     [
    # #         Button.url("【Support】", "https://t.me/kitaxsupport"),
    # #         Button.url("【Updates】", "https://t.me/kitaxupdates"),
    # #     ]
    # # ]
    # await pbot.reply_photo(event.chat_id, PHOTO, caption=caption,
    # # buttons=BUTTON
    # )


__help__ = """ 
❂ /alive: To check if bot is alive or not."""
   
__mod_name__ = "Alive"