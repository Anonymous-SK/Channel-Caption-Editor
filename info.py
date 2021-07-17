# Ns Bots

import os

class config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BUTTON_URL = os.environ.get("BUTTON_URL", "")
    CAPTION = os.environ.get("FILES_CAPTION", "")

