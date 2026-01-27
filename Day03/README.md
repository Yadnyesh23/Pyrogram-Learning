# Day 04 – MongoDB Integration (Persistent File Store)

## Objective
Upgrade the file store bot to store files permanently using MongoDB.

## Key Concepts Learned
- MongoDB basics
- Async database access using motor
- Persistent file storage
- Retrieving data from database

## How the Bot Works
1. User sends a file
2. Bot extracts file_id and metadata
3. Bot stores data in MongoDB
4. Bot sends a retrieval button
5. On click, bot fetches file_id from DB and resends file

## Why Database Is Mandatory
- Prevents data loss on restart
- Supports multi-user bots
- Required for production systems

## Technologies Used
- Pyrogram
- MongoDB
- motor
- dotenv

## Freelancing Tip
Any serious client project requires:
- Database integration
- Persistent data
- Clean environment handling
