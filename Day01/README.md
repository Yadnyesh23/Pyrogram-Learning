# Day 01 – Pyrogram Basics

## Objective
Learn the fundamentals of Pyrogram and create a basic Telegram bot.

## What is Pyrogram?
Pyrogram is a Python framework based on Telegram’s MTProto API.  
It can be used to build both **bots** and **userbots**.

## Key Concepts Learned
- api_id & api_hash (Telegram application credentials)
- bot_token (used for Bot API access)
- Client object (core of Pyrogram)
- Message handlers
- filters.command

## How the Bot Works
1. The Client connects to Telegram servers
2. The bot listens for incoming messages
3. When `/start` is received, the handler function is triggered
4. The bot replies with a welcome message

## Files Explained
- bot.py → Main bot logic
- .env → Stores sensitive credentials
- README.md → Daily learning notes

## Common Mistakes
- Forgetting to convert API_ID to int
- Uploading .env file to GitHub
- Wrong bot token

## Freelancing Tip
Almost every client project starts with:
- Clean setup
- Environment variables
- `/start` command  
Mastering this saves time in paid projects.
