from database import user_cols
from config import OWNER_ID

async def get_role(user_id: int):
    user = await user_cols.find_one({"user_id": user_id})
    return user["role"] if user else None


def admin_only(func):
    async def wrapper(client, message):
        role = await get_role(message.from_user.id)
        if role not in ["admin", "owner"]:
            return await message.reply("🚫 Admin only command")
        return await func(client, message)
    return wrapper


def owner_only(func):
    async def wrapper(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply("🚫 Owner only command")
        return await func(client, message)
    return wrapper
