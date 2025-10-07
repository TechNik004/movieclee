import re
from os import getenv
from dotenv import load_dotenv

load_dotenv()

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    API_ID = int(getenv("API_ID", "10671416"))
    API_HASH = getenv("API_HASH", "d32e7a9253928d78d7888c0b9998939d")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    BOT_WORKERS = int(getenv("BOT_WORKERS", "4"))
    
    # Webhook settings
    WEB_MODE = getenv("WEB_MODE", "False").lower() in ("true", "1", "yes")
    PORT = int(getenv("PORT", "8080"))  # default port for web services
    
    CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002882008991"))
    OWNER_ID = int(getenv("OWNER_ID", "6667067260"))

    # Database
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://technik659:8pZAv0q1E4TpzBfW@cluster0.scjdsho.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = getenv("DATABASE_NAME", "Cluster0")

    # Force subscription
    #FORCE_SUB_CHANNEL = int(getenv("FORCE_SUB_CHANNEL", "0"))   
    FORCE_SUB_CHANNEL = list(set(int(ch) for ch in getenv("FORCE_SUB_CHANNEL", "-1002378694223").split() if id_pattern.fullmatch(ch)))
    JOIN_REQUEST_ENABLE = getenv("JOIN_REQUEST_ENABLED", None)

    # Messages
    START_PIC = getenv("START_PIC", "")
    START_MSG = getenv("START_MESSAGE", "👋 Hello {mention},\n\nThis bot helps you store private files in a secure channel and generate special access links for sharing. 🔐📁\n\nOnly admins can upload files and generate links. Just send the file here to get started.")
    FORCE_MSG = getenv("FORCE_SUB_MESSAGE", "👋 Hello {mention},\n\n<b>You need to join our updates channel before using this bot.</b>\n\n📢 Please join the required channel, then try again.")
    CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", None)

    # ✅ Secure ADMINS (only numeric IDs)
    admins = getenv("ADMINS", "6667067260 5225541255").split()
    ADMINS = list(set(
        [int(x) for x in admins if x.isdigit()] + [OWNER_ID]
    ))

    # Other configs
    PROTECT_CONTENT = getenv("PROTECT_CONTENT", "False") == "True"
    DISABLE_CHANNEL_BUTTON = getenv("DISABLE_CHANNEL_BUTTON", "False") == "True"

    AUTO_DELETE_TIME = int(getenv("AUTO_DELETE_TIME", "0"))
    AUTO_DELETE_MSG = getenv("AUTO_DELETE_MSG", "This file will be automatically deleted in {time}.")
    AUTO_DEL_SUCCESS_MSG = getenv("AUTO_DEL_SUCCESS_MSG", "✅ File deleted successfully.")

    # Token Verification (Shortlink)
    VERIFY_MODE = getenv("VERIFY_MODE", "True").lower() in ("true", "1", "yes")
    SHORTLINK_API = getenv("SHORTLINK_API", "181feb5a18a1e702e5ccf4caf1cac37ebb607822")
    SHORTLINK_URL = getenv("SHORTLINK_URL", "linkshortify.com")
    TOKEN_EXPIRE = int(getenv("TOKEN_EXPIRE", "43200"))  # default: 6 hours
    TUTORIAL = getenv("TUTORIAL", "https://t.me/+-E1ScRZLkQ05Y2Y1")

    BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
    USER_REPLY_TEXT = "❌ I'm a bot — please don't DM me!"
