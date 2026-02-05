from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# ⚠️ TEST TOKEN — TEMPORARY
# Paste THE SAME token you see in Railway Variables here
BOT_TOKEN = "8159744777:AAHoHByEugT7aaO3RDhNEerN3VFr88JdAwo"

CHANNEL_URL = "https://t.me/dailysignalsbonanza"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 JOIN CHANNEL", url=CHANNEL_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 NEW CODE CONFIRMED 🔥\n\n"
        "If you see THIS message and the JOIN button below,\n"
        "then Railway is running the correct code and bot.",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()



