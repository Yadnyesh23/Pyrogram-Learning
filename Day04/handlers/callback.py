from pyrogram import filters
from bot import app
from database import file_cols

@app.on_callback_query(filters.regex("^get_"))
async def send_file(client, callback):
    key = callback.data.split("_")[1]
    file = await file_cols.find_one({"key": key})

    if not file:
        return await callback.answer("File not found", show_alert=True)

    chat_id = callback.message.chat.id
    file_id = file["file_id"]
    file_type = file["file_type"]

    if file_type == "photo":
        await client.send_photo(chat_id, file_id)
    elif file_type == "document":
        await client.send_document(chat_id, file_id)
    elif file_type == "video":
        await client.send_video(chat_id, file_id)

    await callback.answer("✅ File sent")
