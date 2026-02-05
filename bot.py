import os
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

# ================= CONFIG =================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_URL = "https://t.me/dailysignalsbonanza"
JOIN_DELAY_SECONDS = 30  # delay before join button
# =========================================

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing")

# ---------- DELAYED JOB ----------
async def send_join_button(context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Join the Channel", url=CHANNEL_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text="If you’d like to explore more content, you can join the channel below:",
        reply_markup=reply_markup
    )

# ---------- START COMMAND ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 1️⃣ Ads-safe educational message (IMMEDIATE)
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
        "You can explore educational content directly in this bot."
    )

    # 2️⃣ Schedule delayed Join button (RELIABLE)
    context.job_queue.run_once(
        send_join_button,
        when=JOIN_DELAY_SECONDS,
        chat_id=update.effective_chat.id
    )

# ---------- MAIN ----------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started and polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
