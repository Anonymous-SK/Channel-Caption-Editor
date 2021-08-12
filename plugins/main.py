from pyrogram import Client , filters
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup

@Client.on_message(filters.document  & filters.channel)
async def cation_text(Client , message):
  await message.edit(CAPTION , reply_markup = InlineKeyboardMarkup(

         [

[
        InlineKeyboardButton(f"{BUTTON_NAME}", url=f"{BUTTON_URL}")]
            ]
            
                       )
)
