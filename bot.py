import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

CHANNEL_URL = "https://t.me/dailysignalsbonanza"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # First message (no button)
    await update.message.reply_text(
        "👋 Welcome to James Cash Market Education Bot\n\n"
        "This bot provides FREE educational content about global financial markets.\n\n"
        "📘 Topics covered:\n"
        "• Financial market basics\n"
        "• Economic terminology\n"
        "• How global markets work\n"
        "• Risk awareness & education\n\n"
        "⚠️ Disclaimer:\n"
        "This bot is for EDUCATIONAL PURPOSES ONLY.\n"
        "It does NOT provide:\n"
        "❌ Trading signals\n"
        "❌ Investment advice\n"
        "❌ Financial recommendations\n\n"
        "⏳ Please wait..."
    )

    # Wait 5 seconds
    await asyncio.sleep(5)

    # Second message with button
    keyboard = [
        [InlineKeyboardButton("🚀 Join Channel", url=CHANNEL_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👇 To continue, join the channel below:",
        reply_markup=reply_markup
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()



