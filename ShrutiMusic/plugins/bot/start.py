from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ShrutiMusic import app
import config


@app.on_message(filters.command("start") & filters.private)
async def start_private(client, message: Message):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕ Add me to Group", url=f"https://t.me/{app.username}?startgroup=true")
            ],
            [
                InlineKeyboardButton("💬 Support", url=config.SUPPORT_GROUP)
            ]
        ]
    )

    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=(
            "👋 **Welcome!**\n\n"
            "🎶 I am a Music Bot\n"
            "⚡ Fast & Stable\n\n"
            "Use buttons below 👇"
        ),
        reply_markup=buttons
    )
