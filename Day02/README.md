# Day 02 – Pyrogram Inline Keyboard Bot 🚀

## 🎯 Objective
Learn how to use **Inline Keyboard buttons** and **Callback Queries** in Pyrogram to create interactive Telegram bots.

---

## 🤖 What This Bot Does
This bot demonstrates:
- Inline keyboard buttons
- Handling button clicks using callback queries
- Editing messages dynamically
- Secure credential management using environment variables

---

## 🧠 Key Concepts Learned
- InlineKeyboardButton
- InlineKeyboardMarkup
- Callback queries
- `on_callback_query` handler
- Message editing with `edit_text`
- Environment variables using `.env`

---

## ⚙️ How the Bot Works
1. The bot starts and listens for commands
2. When `/start` is sent:
   - An inline keyboard with **About** and **Settings** buttons is shown
3. When a button is clicked:
   - A callback query is triggered
   - The message text is edited based on the button pressed
4. A **Back** button allows navigation to the main menu

---

## ✨ Features
- `/start` command with inline keyboard
- About page (via button)
- Settings page (via button)
- Back navigation
- Clean and interactive UI
- Secure credential handling

---

## 🛠️ Technologies Used
- Python  
- Pyrogram  
- python-dotenv  
- Telegram Bot API  

---

## 🗂️ Project Structure
```
├── bot.py
├── .env
├── .gitignore
└── README.md
```


---

## 🔐 Environment Variables
Create a `.env` file in the root directory:
```
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```


⚠️ **Important:**  
Never upload `.env` to GitHub.  
Always add it to `.gitignore`.

---

## 📜 Code Walkthrough

### 1️⃣ Importing Required Modules
```
from pyrogram import Client, filters
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
```

Client → Connects bot to Telegram

filters → Filters messages and commands

InlineKeyboardButton → Creates inline buttons

InlineKeyboardMarkup → Arranges buttons

load_dotenv() → Loads environment variables

```
load_dotenv()
```
Loads credentials from .env into the environment.


## Initializing the Client
```
app = Client(
    "day02_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)
```
"day02_bot" → Session name

API_ID must be an integer

Credentials are kept secure

## /start Command with Inline Keyboard
```
@app.on_message(filters.command('start'))
async def start_handler(client, message):
```

Displays an inline keyboard with:
(1)About
(2)Settings
Sends a message with buttons using reply_markup

## Callback Query Handler
```
@app.on_callback_query()
async def callbackHandler(client, callback):
```
Triggered when a button is clicked
Uses callback.data to identify which button was pressed
Edits the existing message instead of sending a new one

Supported actions:
about → Shows about page
settings → Shows settings page
back → Returns to main menu

## Editing Messages
```
await callback.message.edit_text(...)
```
Updates message text dynamically
Improves user experience
Keeps chat clean

## Running the Bot
```
if __name__ == '__main__':
    print('Bot started...')
    app.run()
```
Ensures the script runs only when executed directly
Starts the bot and listens for updates