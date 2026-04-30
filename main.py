from telethon import TelegramClient, events
import os
os.system('python app.py')

# Ambil dari Environment Variables di Railway
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = TelegramClient('nimescans_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("Halo! Buka Mini App melalui tombol di bawah.")

print("Bot sedang berjalan...")
bot.run_until_disconnected()
