from pyrogram import Client, filters
from dotenv import load_dotenv
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
   await  message.reply_text('Hello! \n This is bot is developed using pyrogram. \n Use /about to get info about bot.')

@app.on_message(filters.command('help'))
async def help_handler(client, message):
    await message.reply_text('This is help message.\n Use /start to start the bot.')

@app.on_message(filters.command('about'))
async def about_handler(client, message):
    await message.reply_text("This is about messsage.\n Use /help to get help. ")



if __name__ == '__main__':
    print("Bot started...")
    app.run()