from os import getenv


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_IDS = list(map(int, getenv("OWNER_IDS", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
CHANNEL_IDS = list(map(int, getenv("CHANNEL_IDS", "").split()))

