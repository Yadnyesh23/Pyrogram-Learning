from pyrogram import filters
from bot import app
from database import user_cols, file_cols
from utils.roles import admin_only, owner_only

@app.on_message(filters.command("add_admin"))
@owner_only
async def add_admin(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user")

    uid = message.reply_to_message.from_user.id
    await user_cols.update_one(
        {"user_id": uid},
        {"$set": {"role": "admin"}},
        upsert=True
    )
    await message.reply("✅ Admin added")


@app.on_message(filters.command("remove_admin"))
@owner_only
async def remove_admin(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to admin")

    uid = message.reply_to_message.from_user.id
    await user_cols.update_one(
        {"user_id": uid},
        {"$set": {"role": "user"}}
    )
    await message.reply("❌ Admin removed")


@app.on_message(filters.command("stats"))
@admin_only
async def stats(client, message):
    users = await user_cols.count_documents({})
    files = await file_cols.count_documents({})

    await message.reply(
        f"📊 Bot Stats\n\n"
        f"👤 Users: {users}\n"
        f"📁 Files: {files}"
    )
