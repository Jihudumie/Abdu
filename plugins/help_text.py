#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Khamis Seleleko

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "msaada"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["khamis", "hamis"]))
async def hamis(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/khamis")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HAMIS_MAJIBU,
        parse_mode="html",
        reply_to_message_id=update.message_id,
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["elimu"]))
async def elimu(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/elimu")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ELIMU_TXT,
        parse_mode="html",
disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["history", "sira"]))
async def history_islamic(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/history")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HISTORY_ISLAMIC,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["juzuu"]))
async def juzuuzote(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/juzuu")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.JUZUUZOTE,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["quran", "quranswahili", "tafsir"]))
async def quranswahili(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/quran")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.QURAN_SWAHILI,
        parse_mode="html",
        reply_to_message_id=update.message_id,
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["ramadhan"]))
async def ramadhan(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/ramadhan")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.RAMADHAN,
        parse_mode="html",
        reply_to_message_id=update.message_id,
    )
