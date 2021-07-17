# NS Bots

import os
import logging
import pyrogram
from config import Config  


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    NSBOTS = pyrogram.Client(
        "Caption_Editor",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    NSBOTS.run()
