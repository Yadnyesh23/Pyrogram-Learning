from pyrogram import Client, filters
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

load_dotenv()

app = Client(
    "day02_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@app.on_message(filters.command('start'))
async def start_handler(client, message):
    keyboard=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("About", callback_data='about')],
            [InlineKeyboardButton("Settings", callback_data='settings')],
        ]
    )
    await message.reply_text(
        'This is Day 02 Bot.\n Choose an option :',
        reply_markup=keyboard
    )

@app.on_callback_query()
async def callbackHandler(client, callback):
    if callback.data == 'about':
        await callback.message.edit_text(
            'This is about page. Coming soon.',
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data='back')]])
        )
    elif callback.data == 'settings':
        await callback.message.edit_text(
            'This is settings page. Coming soon.',
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data='back')]])
        )
    elif callback.data == 'back':
        await callback.message.edit_text(
            'This is Day 02 Bot.\n Choose an option :',
            reply_markup=InlineKeyboardMarkup(
                [
            [InlineKeyboardButton("About", callback_data='about')],
            [InlineKeyboardButton("Settings", callback_data='settings')],
        ]
            )
        )

if __name__ =='__main__':
    print('Bot started...')
    app.run()