# ZeldrisRobot
# Copyright (C) 2017-2019, Paul Larsen
# Copyright (c) 2021, IDNCoderX Team, <https://github.com/IDN-C-X/ZeldrisRobot>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import json

if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    sys.exit(1)

def get_user_list(config, key):
    with open("{}/zeldris/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = "5364041591:AAEPo9zccIjLMRBhIUNHhIckseQXvxTeFXM"  # Take from @BotFather
    OWNER_ID = (
         1938491135 # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "Husbandoo"
    API_HASH = "6b19682d1aeeda50a4aa8b6eb61f3a4e"  # for purge stuffs
    API_ID = 7761098

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://xlzbhnyp:FVQzpp344W5yDcXc_cupZHy5qZoehDbN@castor.db.elephantsql.com/xlzbhnyp"  # needed for any database modules
    MESSAGE_DUMP = -1001607789423  # needed to make sure 'save from' messages persist
    REDIS_URL = "redis://:LBVYsRjHCjJWb5xbyJXZdoHChpKVUJGr@redis-16484.c15.us-east-1-4.ec2.cloud.redislabs.com:16484"  # needed for afk module, get from redislab
    LOAD = []
    SUPPORT_CHAT = "ShinomiyaSupport"  # Your own group for support, do not add the @
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    DEV_USERS = get_user_list("elevated_users.json", "devs") # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = get_user_list("elevated_users.json", "sudos") # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelist")  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DEMONS = get_user_list("elevated_users.json", "demon")
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = True # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = ""  # OpenWeather API
    SPAMWATCH_API = ""  # Your SpamWatch token
    WALL_API = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
