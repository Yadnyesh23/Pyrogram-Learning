from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL
import os
from dotenv import load_dotenv

load_dotenv()

mongo = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = mongo.file_store_bot

user_cols = db.users
file_cols = db.files