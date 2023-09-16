#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5224615589:AAFSp9poqPTnY4tLJS-PalUw9qMZybnQ75g")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "1669750"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0f53ee8c576281995d621194aec588d8")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001738654185"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "831370530"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ramcool:ramcool@cluster0.6hxnajq.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001957015339"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "╔┓┏╦━━╦┓╔┓╔━━-\n║┗┛║┗━╣┃║┃║ ^ ^ ✦\n║┏┓║┏━╣┗╣┗╣╰╯║\n╚┛┗╩━━╩━╩━╩━━╝\n\n\n<b>Hello {first}\nI am a bot which will provide you files instantly which are shared in @Kan_Serial and @SB_SERIALS </b>\n\n⚠Kindly Please join my channel / ದಯವಿಟ್ಟು ನನ್ನನ್ನ ಚಾನಲ್‌ಗೆ ಸೇರಿಕೊಳ್ಳಿ⚠")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "831370530 718979130 967367094 5866151665 928357565").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}<br><a href=https://telegram.me/+kQS5TtxyNBVjNjg1> Kindly Please Join My Channel\n</a><br><a href=https://telegram.me/+kQS5TtxyNBVjNjg1>ದಯವಿಟ್ಟು ನನ್ನನ್ನು ಬಳಸಲು ಚಾನಲ್‌ಗೆ ಸೇರಿಕೊಳ್ಳಿ</a>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
