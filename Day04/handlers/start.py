print("start.py loaded")

from pyrogram import filters
from app import app
from database import user_cols
from config import OWNER_ID

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    user = await user_cols.find_one({"user_id": user_id})

    if not user:
        role = "owner" if user_id == OWNER_ID else "user"
        await user_cols.insert_one({
            "user_id": user_id,
            "role": role
        })

    await message.reply("✅ File Store Bot ready")
