## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "MMilebot")
API_ID = int(getenv("API_ID", "15770953"))
API_HASH = getenv("API_HASH", "3a26ba5d4f7a43dc34bc7e94b1e1b780")
OWNER_NAME = getenv("OWNER_NAME", "✘ِ𝘼َِ𝙇َِ𝘼َِ𝙒َِ𝙀 َِ𝘼َِ𝙇𝙌َِ𝙐َِ𝙍َِ𝘼َِ𝙎َِ𝙃َِ𝙀")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ALAWE1")
ALIVE_NAME = getenv("ALIVE_NAME", "⎙𝐀𝐖 𝐂𝐎𝐃𝐄⬥⎙")
BOT_USERNAME = getenv("BOT_USERNAME", "MMilebot")
OWNER_ID = getenv("OWNER_ID", "5719613462")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "amer")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "tx_it")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FTTIT")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5719613462").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://graph.org/file/d1d31a56f7833013cf42b.jpg")
START_PIC = getenv("START_PIC", "https://graph.org/file/76028c417e910d6932d11.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AlawiAlQurashi/Music-MELA")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
