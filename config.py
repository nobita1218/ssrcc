# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "37138438"))
API_HASH = getenv("API_HASH", "d1b5f3a54b0c8130747432aaca542b77")
BOT_TOKEN = getenv("BOT_TOKEN", "8673437112:AAGR81x_Srv_GQNPUuAbI0X4w__Xhfr4hYM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8109612125").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003843035636")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003843035636"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
