from pyrogram import filters
from app import app
from database import file_cols
import uuid

@app.on_message(filters.document | filters.photo | filters.video)
async def upload_file(client, message):
    try:
        user_id = message.from_user.id

        # Detect file type & file_id
        if message.document:
            file_id = message.document.file_id
            file_type = "document"

        elif message.photo:
            file_id = message.photo.file_id
            file_type = "photo"

        elif message.video:
            file_id = message.video.file_id
            file_type = "video"

        else:
            return await message.reply("❌ Unsupported file")

        # Generate unique key
        key = uuid.uuid4().hex[:10]

        # Save to DB
        file_cols.insert_one({
            "key": key,
            "file_id": file_id,
            "file_type": file_type,
            "owner_id": user_id,
            "is_public": False
        })

        await message.reply(
            f"✅ File saved successfully\n\n"
            f"🔑 File Key: `{key}`\n"
            f"🔗 Access Link:\n"
            f"https://t.me/{(await client.get_me()).username}?start=file_{key}"
        )

    except Exception as e:
        await message.reply("⚠️ Failed to save file")
