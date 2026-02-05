import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Use environment variable (recommended)
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
