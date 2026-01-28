from functools import wraps
from config import OWNER_ID
from database import user_cols

def owner_only(func):
    @wraps(func)
    async def wrapper(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply("❌ Owner only command")
        return await func(client, message)
    return wrapper


def admin_only(func):
    @wraps(func)
    async def wrapper(client, message):
        user = user_cols.find_one({"user_id": message.from_user.id})
        if not user or user["role"] not in ["admin", "owner"]:
            return await message.reply("❌ Admin only command")
        return await func(client, message)
    return wrapper
