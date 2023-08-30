import os
from os import getenv


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_USERNAME = getenv("BOT_USERNAME", "HirokoRobot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6109551937"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6109551937 5416887843 6236996313 5218610039").split()))
MONGO_URL = getenv("MONGO_URL", "")
