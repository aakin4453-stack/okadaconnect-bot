import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

print("🚀 Bot is starting...")
if not TELEGRAM_TOKEN:
    print("❌ TELEGRAM_TOKEN not found!")
else:
    print(f"✅ TELEGRAM_TOKEN loaded: {TELEGRAM_TOKEN[:10]}...")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
print("🤖 Bot is now polling Telegram...")
app.run_polling()

