from pyrogram import filters
from app import app
from database import files_col

@app.on_callback_query(filters.regex("^get_"))
async def send_file(client, callback):
    try:
        user_id = callback.from_user.id
        key = callback.data.split("_", 1)[1]

        file_data = files_col.find_one({"key": key})

        if not file_data:
            return await callback.answer("❌ File not found", show_alert=True)

        # Access control
        if file_data["owner_id"] != user_id:
            return await callback.answer("❌ Access denied", show_alert=True)

        file_type = file_data["file_type"]
        file_id = file_data["file_id"]

        if file_type == "document":
            await client.send_document(callback.message.chat.id, file_id)
        elif file_type == "photo":
            await client.send_photo(callback.message.chat.id, file_id)
        elif file_type == "video":
            await client.send_video(callback.message.chat.id, file_id)
        else:
            await callback.answer("❌ Unsupported file", show_alert=True)

        await callback.answer()

    except Exception:
        await callback.answer("⚠️ Error occurred", show_alert=True)
