# Ns Bots

import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "")
BUTTON_URL = os.environ.get("BUTTON_URL", "")
BUTTON_NAME = os.environ.get("BUTTON_NAME", "")
CAPTION = os.environ.get("FILES_CAPTION", "")
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")

about_text = f"""--**My Details:**--

🤖 𝐌𝐲 𝐍𝐚𝐦𝐞: Movies Search NS bot
    
📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: [Python 3](https://www.python.org/)

🧰 𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤: [Pyrogram](https://github.com/pyrogram/pyrogram)

👨‍💻 Creator : [This Person](tg://user?id={OWNER_ID})

📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: [NS BOT UPDATES](https://t.me/Ns_bot_updates)

👥 𝐆𝐫𝐨𝐮𝐩: [Ns BOT SUPPORT](https://t.me/Ns_Bot_supporters)

📎 SOURCE CODE : [Click Here 😍](https://github.com/Anonymous-SK/Channel-Caption-Editor)
"""
