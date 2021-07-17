from pyrogram import Client , filters
from pyrogram.type import InlineKeyboardButton , InlineKeyboardMarkup
from pyrogram.errors import floodwait
from info import OWNER_ID , BUTTON_URL , CAPTION , OWNER_USERNAME , BUTTON_NAME 

ns_keyboard = [
        [
            InlineKeyboardButton('My Owner', url=f"https://t.me/{OWNER_USERNAME}"),
            InlineKeyboardButton('About', callback_data="about")
        ]
    ]

@Client.on_message(filters.command("start") & filters.private)
async def start(Client , message):
  await message.reply_text(f"Hello there \ni am channel caption editor bot \n\n👲 Maintained By:** {owner.mention(style='md')}**" , reply_markup=InlineKeyboardMarkup(ns_keyboard))

CAPTION_BUTTON = [[
             InlineKeyboardButton(f'{BUTTON_NAME}', url=f"BUTTON_URL")
        ]]
@Client.on_message(filters.document & filters.channel)
async def cpation_text(Client , message):
  await message.edit(CAPTION , reply_markup=InlineKeyboardMarkup(CAPTION_BUTTON))
