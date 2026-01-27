# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from ShrutiMusic import app
from ShrutiMusic.core.call import Nand
from ShrutiMusic.utils import bot_sys_stats
from ShrutiMusic.utils.decorators.language import language
from ShrutiMusic.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()

    # 🔹 TEXT ONLY (NO IMAGE)
    response = await message.reply_text(
        _["ping_1"].format(app.mention),
        disable_web_page_preview=True
    )

    pytgping = await Nand.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    await response.edit_text(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping
        ),
        reply_markup=supp_markup(_),
        disable_web_page_preview=True
    )
