from app import app

from handlers import start, upload, callback, admin

if __name__ == "__main__":
    print("Bot running...")
    app.run()
