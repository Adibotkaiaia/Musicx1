import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = int(os.getenv("OWNER_ID", "0"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "")

BOT_USERNAME = os.getenv("BOT_USERNAME", "VIP_MUSIC_X1_BOT")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1003550365298"))

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", "")

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/Il_vip_support_lI")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/VIP_SUPPORT_II")
DONATE = os.getenv("DONATE", "https://t.me/VIP_SUPPORT_II")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", "600"))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", "25"))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", "2145386496"))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

STRING1 = os.getenv("STRING_SESSION", "")
STRING2 = os.getenv("STRING_SESSION2", "")
STRING3 = os.getenv("STRING_SESSION3", "")
STRING4 = os.getenv("STRING_SESSION4", "")
STRING5 = os.getenv("STRING_SESSION5", "")

AUTO_LEAVING_ASSISTANT = os.getenv(
    "AUTO_LEAVING_ASSISTANT", "false"
).lower() in ["true", "1", "yes"]

START_STICKER_ENABLED = os.getenv(
    "START_STICKER_ENABLED", "true"
).lower() in ["true", "1", "yes"]

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/u2oc8f.jpg")
PING_IMG_URL = "https://files.catbox.moe/ucyk3n.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/nnqwbf.jpg"
STATS_IMG_URL = "https://files.catbox.moe/1ha8i5.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ucyk3n.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/1ha8i5.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/ucyk3n.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/1ha8i5.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/1ha8i5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/nnqwbf.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/1ha8i5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ucyk3n.jpg"

BANNED_USERS = set()

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

ERROR_FORMAT = int("7574330905")

# URL validation
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with https://")

if SUPPORT_GROUP and not re.match(r"(?:http|https)://", SUPPORT_GROUP):
    raise SystemExit("[ERROR] - SUPPORT_GROUP must start with https://")
