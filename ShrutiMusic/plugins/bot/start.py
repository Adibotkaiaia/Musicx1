from pyrogram import filters
from pyrogram.types import Message
from ShrutiMusic import app


@app.on_message(filters.command("start") & filters.private, group=1)
async def force_start(client, message: Message):
    await message.reply_text(
        "✅ /start WORKING NOW\n\nBot fully alive 🚀"
    )
