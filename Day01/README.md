# Day 01 – Pyrogram Basics 🚀

## 🎯 Objective
Learn the fundamentals of **Pyrogram** and build a basic Telegram bot while following proper project structure and security practices.

---

## 🤖 What is Pyrogram?
Pyrogram is a modern **Python framework based on Telegram’s MTProto API**.  
It allows developers to build:

- Telegram **Bots**
- Telegram **Userbots**

using clean, asynchronous Python code.

---

## 🧠 Key Concepts Learned
- `api_id` & `api_hash` → Telegram application credentials  
- `bot_token` → Used for Bot API authentication  
- `Client` object → Core of Pyrogram  
- Message handlers  
- `filters.command` for command-based routing  
- Environment variables using `.env`

---

## ⚙️ How the Bot Works
1. The `Client` connects to Telegram servers  
2. The bot listens for incoming updates  
3. When `/start` or `/help` is received, the corresponding handler is triggered  
4. The bot replies with a predefined message  

---

## 📁 Files Explained
- `bot.py` → Main bot logic  
- `.env` → Stores sensitive credentials  
- `.gitignore` → Prevents `.env` from being pushed to GitHub  
- `README.md` → Documentation and daily learning notes  

---

## ❌ Common Mistakes
- Forgetting to convert `API_ID` to `int`
- Accidentally uploading `.env` to GitHub
- Using the wrong bot token
- Hardcoding credentials in the source code

---

## 💼 Freelancing Tip
Almost every real-world client project starts with:
- Clean project setup  
- Secure environment variables  
- A working `/start` command  

Mastering these basics saves **time and effort** in paid projects.

---

# 📘 Code Explanation
## Pyrogram Telegram Bot – Basic Command Handler

This project demonstrates how to:
- Securely configure a Telegram bot
- Use Pyrogram command handlers
- Write asynchronous, production-ready code

---

## ✨ Features
- `/start` → Sends a welcome message  
- `/help` → Sends a help message  
- Secure credential handling using `.env`  
- Asynchronous message processing with `async/await`

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

## 🔐 Environment Variables
Create a `.env` file in the root directory and add:

```
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```


⚠️ **Important:**  
Never push the `.env` file to GitHub.  
Always add it to `.gitignore`.

---

## 📜 Code Walkthrough

### 1️⃣ Importing Required Modules
```
from pyrogram import Client, filters
from dotenv import load_dotenv
import os
```

Client → Connects the bot to Telegram
filters → Filters incoming messages
load_dotenv() → Loads environment variables
os.getenv() → Reads credentials securely

```
load_dotenv()
```
Loads all credentials from the .env file.


```
app = Client(
    "day01_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)
```
"day01_bot" → Session name

API_ID must be an integer

Credentials are kept secure and not hardcoded

## /start Command Handler
```
@app.on_message(filters.command('start'))
async def start_handler(client, message):
    await message.reply_text(
        "Hello!\nThis bot is developed using Pyrogram."
    )
```

Triggered when /start is sent
Sends a welcome message
Uses async for non-blocking execution

## /help Command Handler
```
@app.on_message(filters.command('help'))
async def help_handler(client, message):
    await message.reply_text("This is help message.")
```

Triggered when /help is sent
Responds with a help message

## Running the Bot
```
if __name__ == '__main__':
    print("Bot started...")
    app.run()
```
Ensures the script runs only when executed directly

app.run() connects the bot and starts listening for updates