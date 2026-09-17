from os import getenv


API_ID = int(getenv("API_ID", "32853799"))
API_HASH = getenv("API_HASH", "7618973ca6fa27183f6df27dfba88f26")
BOT_TOKEN = getenv("BOT_TOKEN", "8803183382:AAFPiHVHEYMZKaa8n6rhhs3RQbGgY9GJ8HM")
OWNER_IDS = list(map(int, getenv("OWNER_IDS", "738363992").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://tanmaysingh87op_db_user:RQKGjrYs5U
NvHvtm@cluster0.7gpqqce.mongodb.net/?appName=Cluster0")
CHANNEL_IDS = list(map(int, getenv("CHANNEL_IDS", "-1004442937928").split()))

