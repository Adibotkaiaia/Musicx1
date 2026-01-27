import time
import random
from typing import Final

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ShrutiMusic import app
from ShrutiMusic.misc import _boot_
from ShrutiMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from ShrutiMusic.utils import bot_sys_stats
from ShrutiMusic.utils.formatters import get_readable_time
from ShrutiMusic.utils.inline import help_pannel_page1, private_panel, start_panel
from strings import get_string


RANDOM_STICKERS = [
    "CAACAgUAAxkBAAEEnzFor872a_gYPHu-FxIwv-nxmZ5U8QACyBUAAt5hEFVBanMxRZCc7h4E",
    "CAACAgUAAxkBAAEEnzJor88q_xRO1ljlwh_I6fRF7lDR-AACnBsAAlckCFWNCpez-HzWHB4E",
    "CAACAgUAAxkBAAEEnzNor88uPuVTSyRImyVXsu1pqrpRLgACKRMAAvOEEFUpvggmgDu6bx4E",
    "CAACAgUAAxkBAAEEnzRor880z_spEYEnEfyFXN55tNwydQACIxUAAosKEVUB8iqZMVYroR4E"
]


def random_sticker():
    return random.choice(RANDOM_STICKERS)


# ================= PRIVATE START ================= #

@app.on_message(filters.command("start") & filters.private)
async def start_private(client, message: Message):

    # Banned user check
    if await is_banned_user(message.from_user.id):
        return

    await add_served_user(message.from_user.id)

    language = await get_lang(message.chat.id)
    _ = get_string(language)

    if getattr(config, "START_STICKER_ENABLED", True):
        await message.reply_sticker(random_sticker())

    UP, CPU, RAM, DISK = await bot_sys_stats()

    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_2"].format(
            message.from_user.mention,
            app.mention,
            UP,
            DISK,
            CPU,
            RAM
        ),
        reply_markup=InlineKeyboardMarkup(private_panel(_)),
    )

    if await is_on_off(2):
        await app.send_message(
            chat_id=config.LOG_GROUP_ID,
            text=(
                f"{message.from_user.mention} started the bot.\n\n"
                f"User ID: <code>{message.from_user.id}</code>\n"
                f"Username: @{message.from_user.username}"
            ),
        )


# ================= GROUP START ================= #

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message: Message):

    if await is_banned_user(message.from_user.id):
        return

    language = await get_lang(message.chat.id)
    _ = get_string(language)

    if getattr(config, "START_STICKER_ENABLED", True):
        await message.reply_sticker(random_sticker())

    uptime = int(time.time() - _boot_)

    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(
            app.mention,
            get_readable_time(uptime)
        ),
        reply_markup=InlineKeyboardMarkup(start_panel(_)),
    )

    await add_served_chat(message.chat.id)


# ================= BOT ADDED TO GROUP ================= #

@app.on_message(filters.new_chat_members)
async def welcome(client, message: Message):

    for member in message.new_chat_members:

        language = await get_lang(message.chat.id)
        _ = get_string(language)

        if member.id == app.id:

            if message.chat.type != ChatType.SUPERGROUP:
                await message.reply_text(_["start_4"])
                return await app.leave_chat(message.chat.id)

            if message.chat.id in await blacklisted_chats():
                await message.reply_text(
                    _["start_5"].format(
                        app.mention,
                        f"https://t.me/{app.username}?start=sudolist",
                        config.SUPPORT_GROUP,
                    ),
                    disable_web_page_preview=True,
                )
                return await app.leave_chat(message.chat.id)

            if getattr(config, "START_STICKER_ENABLED", True):
                await message.reply_sticker(random_sticker())

            await message.reply_photo(
                photo=config.START_IMG_URL,
                caption=_["start_3"].format(
                    message.from_user.first_name,
                    app.mention,
                    message.chat.title,
                    app.mention,
                ),
                reply_markup=InlineKeyboardMarkup(start_panel(_)),
            )

            await add_served_chat(message.chat.id)
            await message.stop_propagation()
