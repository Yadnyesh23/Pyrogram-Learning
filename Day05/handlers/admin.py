from pyrogram import filters
from app import app
from utils.roles import owner_only, admin_only
from models.user_model import update_role
from database import user_cols
from utils.logger import logger

@app.on_message(filters.command("addadmin"))
@owner_only
async def add_admin(client, message):
    try:
        user_id = int(message.text.split()[1])
        update_role(user_id, "admin")
        await message.reply("✅ Admin added")
    except:
        await message.reply("Usage: /addadmin user_id")


@app.on_message(filters.command("users"))
@admin_only
async def users(client, message):
    count = user_cols.count_documents({})
    await message.reply(f"👥 Total users: {count}")




@app.on_message(filters.command("stats"))
@admin_only
async def stats(client, message):
    try:
        total_users = user_cols.count_documents({})
        admins = user_cols.count_documents({"role": "admin"})
        await message.reply(
            f"📊 Bot Stats\n\n"
            f"👥 Users: {total_users}\n"
            f"🛠 Admins: {admins}"
        )
    except Exception as e:
        logger.error(e)
        await message.reply("⚠️ Failed to fetch stats")

@app.on_message(filters.command("broadcast"))
@admin_only
async def broadcast(client, message):
    try:
        text = message.text.replace("/broadcast", "").strip()
        if not text:
            return await message.reply("Usage: /broadcast your message")

        users = user_cols.find({})
        sent = 0

        for user in users:
            try:
                await client.send_message(user["user_id"], text)
                sent += 1
            except:
                pass

        await message.reply(f"✅ Broadcast sent to {sent} users")

    except Exception as e:
        logger.error(e)
        await message.reply("❌ Broadcast failed")