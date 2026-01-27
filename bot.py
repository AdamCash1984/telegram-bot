from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "8159744777:AAFY3kPi-g_CofmxiX-tmcs3MHHcs26VQ-4"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Join Channel 🚀", url="https://t.me/JamesDailyFXtrader")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "👋 Welcome!\n\n"
        "You’re one step away from real FX & Gold trading signals 📊\n\n"
        "We provide daily entries and market insights from real traders.\n\n"
        "👇 Join our official Telegram channel below",
        reply_markup=reply_markup
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
