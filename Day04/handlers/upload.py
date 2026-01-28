from pyrogram import filters
from uuid import uuid4
from bot import app
from database import file_cols

@app.on_message(filters.private & (filters.document | filters.photo | filters.video))
async def upload_file(client, message):
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
        return
    
    count = await file_cols.count_documents({})
    key = str(count+1)

    await file_cols.insert_one({
        "key": key,
        "file_id": file_id,
        "file_type": file_type
    })

    await message.reply_text(
        f"✅ File saved\n\n"
        f"🔑 Key: `{key}`\n"
        f"Use button to retrieve",
        reply_markup={
            "inline_keyboard": [[
                {"text": "📥 Get File", "callback_data": f"get_{key}"}
            ]]
        }
    )
