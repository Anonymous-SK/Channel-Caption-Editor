# NS Bots

import os
import logging
import pyrogram
from info import ns 


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    NSBOTS = pyrogram.Client(
        "Caption_Editor",
        bot_token=ns.BOT_TOKEN,
        api_id=ns.API_ID,
        api_hash=ns.API_HASH,
        plugins=plugins,
        workers=300
    )
    NSBOTS.run()
