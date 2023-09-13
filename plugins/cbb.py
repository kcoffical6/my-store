#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f╭─《 🔰𝔸𝔹𝕆𝕌𝕋 𝕄𝔼🔰 》\n├  CREATOR: <a href='tg://settings'>Hacker💻</a>\n├  CHANNEL: <a href='https://t.me/+kQS5TtxyNBVjNjg1'>Sb Kan-Serial</a>, <a href='https://t.me/+kQS5TtxyNBVjNjg1'>𝙺𝙰𝙽𝙽𝙰𝙳𝙰 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂 𝙻𝙸𝙽𝙺</a>\n├ LANGUAGE USED: Python\n╰  𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔❤️</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass