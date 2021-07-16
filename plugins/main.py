from pyrogram import Client , filters
from pyrogram.type import InlineKeyboardButton , InlineKeyboardMarkup
from pyrogram.errors import floodwait

ns_keyboard = [
        [
            InlineKeyboardButton('My Owner', url=f"https://t.me/{owner_username}"),
            InlineKeyboardButton('About', callback_data="about")
        ]
    ]

@Client.on_message(filters.command("start") & filters.private)
async def start(Client , message):
  await message.reply_text(f"Hello there \ni am channel caption editor bot \n\n👲 Maintained By:** {owner.mention(style='md')}**" , reply_markup=InlineKeyboardMarkup(ns_keyboard))


@Client.on_message(filters.document & filters.channel)
async def cpation_text(Client , message):
  await message.reply_text(channel_caption)
