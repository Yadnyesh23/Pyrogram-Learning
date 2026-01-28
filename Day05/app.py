from pyrogram import Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Client(
    "role_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)
