from pyrogram import Client , filters
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from info import OWNER_USERNAME , BUTTON_NAME , BUTTON_URL , CAPTION , OWNER_ID 

@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()

about_text = f"""--**My Details:**--

🤖 𝐌𝐲 𝐍𝐚𝐦𝐞: Caption Editor Bot
    
📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: [Python 3](https://www.python.org/)

🧰 𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤: [Pyrogram](https://github.com/pyrogram/pyrogram)

👨‍💻 Developer : [This Person](tg://user?id={OWNER_ID})

📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: [NS BOT UPDATES](https://t.me/Ns_bot_updates)

👥 𝐆𝐫𝐨𝐮𝐩: [Ns BOT SUPPORT](https://t.me/Ns_Bot_supporters)

📎 SOURCE CODE : [Click Here 🥰](https://github.com/Anonymous-SK/Channel-Caption-Editor)
"""

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
keyboard = [[
            InlineKeyboardButton('My Owner', url=f"https://t.me/{OWNER_USERNAME}"),
            InlineKeyboardButton('About', callback_data="about")
        ],[ 
            InlineKeyboardButton('Close 🔐' , callback_data='close')
        ]]

@Client.on_message(filters.command("start") & filters.private)
async def start(Client , message):
  owner = await Client.get_users(int(OWNER_ID))
  await message.reply_text(f"Hello there \n\n **💡 i am channel caption editor bot **\n\n👲 Maintained By: **{owner.mention(style='md')}**" , reply_markup=InlineKeyboardMarkup(keyboard))

@Client.on_message(filters.document & filters.channel)
async def cation_text(Client , message):
  await message.edit(CAPTION , reply_markup = InlineKeyboardMarkup(

         [

[
        InlineKeyboardButton(f"{BUTTON_NAME}", url=f"{BUTTON_URL}")]
            ]
            
                       )
)
