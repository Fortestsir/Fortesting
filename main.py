from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Yahan aapka bot token hai — directly set kiya gaya
BOT_TOKEN = "7609219087:AAGT1NMeizZcSQgNGyjDLUisYNAbI75ql10"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!")

# Bot initialize and start
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
