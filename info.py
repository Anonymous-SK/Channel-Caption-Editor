# Ns Bots

import os

class ns(object):
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH", "")
  BUTTON_URL = os.environ.get("BUTTON_URL", "")
  BUTTON_NAME = os.environ.get("BUTTON_NAME", "")
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
  CAPTION = os.environ.get("FILES_CAPTION", "")
  OWNER_ID = int(os.environ.get("OWNER_ID", ""))
