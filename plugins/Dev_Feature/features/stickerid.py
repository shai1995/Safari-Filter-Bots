# This code has been modified by @Safaridev
# Please do not remove this credit
from pyrogram import Client, filters

@Client.on_message(filters.command(["sticker_id"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("<b>Oops !! Not a sticker file</b>")
