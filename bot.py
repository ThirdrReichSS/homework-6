from pathlib import Path
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
# from db.databbase import database, Database

load_dotenv()
token = getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()


# database = Database(
#     Path(__file__).parent / "db.sqlite"
# )
