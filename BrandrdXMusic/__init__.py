from kaalXMusic.core.bot import Hotty
from kaalXMusic.core.dir import dirr
from kaalXMusic.core.git import git
from kaalXMusic.core.userbot import Userbot
from kaalXMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "@KAAL_MUSIC_35_BOT"  # connect music api key "Dont change it"
