from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# HARD-CODE TOKEN FOR PROOF (temporary)
BOT_TOKEN = "8159744777:AAHoHByEugT7aaO3RDhNEerN3VFr88JdAwo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    me = await context.bot.get_me()

    await update.message.reply_text(
        f"🔥 BOT IDENTITY CHECK 🔥\n\n"
        f"ID: {me.id}\n"
        f"Username: @{me.username}\n"
        f"Name: {me.first_name}\n\n"
        f"If this does NOT match the bot you think you are chatting with,\n"
        f"then you are talking to a DIFFERENT bot."
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()




