import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ================= CONFIG =================
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Set it as an environment variable: BOT_TOKEN=...")

# The channel where your message/content is (this does not affect the button destination)
SOURCE_CHANNEL_URL = "https://t.me/dailysignalsbonanza"

# The destination you want the button to open (account/channel)
BUTTON_DESTINATION_URL = "https://t.me/Alexmsignals"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Safety: /start should be used in private chat with the bot
    if update.effective_chat and update.effective_chat.type != "private":
        return

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
        f"📣 Main channel: {SOURCE_CHANNEL_URL}\n\n"
        "⏳ Please wait..."
    )

    # Wait 5 seconds
    await asyncio.sleep(5)

    # Second message with button (goes to the OTHER account)
    keyboard = [[InlineKeyboardButton("🚀 Join Channel", url=BUTTON_DESTINATION_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👇 To continue, click the button below:",
        reply_markup=reply_markup
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()




