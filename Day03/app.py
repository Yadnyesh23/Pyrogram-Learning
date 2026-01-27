from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Client(
    "day3_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

# MongoDB setup
mongo = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = mongo[os.getenv("DB_NAME")]
files_col = db["files"]

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text(
        "📦 Persistent File Store Bot\n\n"
        "Send me a file and I’ll store it permanently."
    )

@app.on_message(filters.document | filters.photo | filters.video)
async def save_file(client, message):

    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        file_type = "document"

    elif message.photo:
        file_id = message.photo.file_id
        file_name = "photo.jpg"
        file_type = "photo"

    else:
        file_id = message.video.file_id
        file_name = "video.mp4"
        file_type = "video"

    count = await files_col.count_documents({})
    key = str(count + 1)

    await files_col.insert_one({
        "key": key,
        "file_id": file_id,
        "file_name": file_name,
        "file_type": file_type
    })

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("📥 Get File", callback_data=f"get_{key}")]]
    )

    await message.reply_text(
        f"✅ File stored permanently!\n📎 {file_name}",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex("^get_"))
async def send_file(client, callback):
    key = callback.data.split("_")[1]

    file_data = await files_col.find_one({"key": key})
    if not file_data:
        await callback.answer("❌ File not found", show_alert=True)
        return

    file_type = file_data["file_type"]
    file_id = file_data["file_id"]

    if file_type == "photo":
        await client.send_photo(
            chat_id=callback.message.chat.id,
            photo=file_id
        )

    elif file_type == "document":
        await client.send_document(
            chat_id=callback.message.chat.id,
            document=file_id
        )

    elif file_type == "video":
        await client.send_video(
            chat_id=callback.message.chat.id,
            video=file_id
        )

    else:
        await callback.answer("Unsupported file type", show_alert=True)


if __name__ == "__main__":
    print("Day 3 Bot Running...")
    app.run()
