from dotenv import load_dotenv
from pyrogram import Client, filters
import os

load_dotenv()

app = Client(
    "day01_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@app.on_message(filters.command('start'))
async def start_handler(client, message):
    await message.reply_text("Welcome ! \n This bot is developed using Pyrogram.")

if __name__ == '__main__':
    print('Bot started...')
    app.run()