from pyrogram import filters
from app import app
from database import user_cols, file_cols
from config import OWNER_ID

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    user = user_cols.find_one({"user_id": user_id})
    if not user:
        role = "owner" if user_id == OWNER_ID else "user"
        user_cols.insert_one({
            "user_id": user_id,
            "role": role
        })

    args = message.text.split(maxsplit=1)
    if len(args) > 1 and args[1].startswith("file_"):
        key = args[1].replace("file_", "")
        file_data = file_cols.find_one({"key": key})

        if not file_data:
            return await message.reply("❌ File not found")

        if file_data["owner_id"] != user_id:
            return await message.reply("❌ You are not allowed to access this file")

        file_type = file_data["file_type"]
        file_id = file_data["file_id"]

        if file_type == "document":
            await client.send_document(message.chat.id, file_id)
        elif file_type == "photo":
            await client.send_photo(message.chat.id, file_id)
        elif file_type == "video":
            await client.send_video(message.chat.id, file_id)
        else:
            await message.reply("❌ Unsupported file type")

        return

    await message.reply("✅ Bot is live and role system is active")
