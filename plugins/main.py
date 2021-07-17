import os
from pyrogram import Client , filters
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from info import OWNER_USERNAME , BUTTON_NAME , BUTTON_URL , CAPTION , OWNER_ID , about_text , reply_markup

@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()

@Client.on_callback_query(filters.regex('^about'))
async def about_cb(c, m):
    await m.answer()
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton('Close 🔐', callback_data="close")
        ]]),
        disable_web_page_preview=True
    )

keyboard = [
        [
            InlineKeyboardButton('My Owner', url=f"https://t.me/{OWNER_USERNAME}"),
            InlineKeyboardButton('About', callback_data="about")
        ],[ 
            InlineKeyboardButton('Close 🔐' , callback_data='close')
]
    ]

@Client.on_message(filters.command("start") & filters.private)
async def start(Client , message):
  await message.reply_text(f"Hello there \n\n **💡 i am channel caption editor bot **\n\n👲 Maintained By:**[This Person](tg://user?id={OWNER_ID})**" , reply_markup=InlineKeyboardMarkup(keyboard))

@Client.on_message(filters.document & filters.channel)
async def cation_text(Client , message):
  await message.edit(CAPTION , reply_markup=reply_markup)
