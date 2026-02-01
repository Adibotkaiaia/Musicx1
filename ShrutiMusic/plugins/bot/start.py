from pyrogram import filters
from pyrogram.types import Message
from ShrutiMusic import app


@app.on_message(filters.command("start") & filters.private, group=1)
async def force_start(client, message: Message):
    await message.reply_text(
        "✨ HELLO {}\n\n"
        "🎶 WELCOME TO VIP X MUSIC 🎶\n\n"
        "➤ A SMART & ELEGANT MUSIC BOT\n"
        "➤ SMOOTH PLAYBACK • HD SOUND\n"
        "➤ NO ADS • NO LAG\n\n"
        "📌 SOURCES:\n"
        "YouTube • Spotify • Apple • Saavn\n\n"
        "👉 USE /help TO VIEW ALL COMMANDS",
        format_kwargs={"mention": message.from_user.mention}
    )
