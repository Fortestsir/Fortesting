from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import os

BOT_TOKEN = os.getenv("7609219087:AAGT1NMeizZcSQgNGyjDLUisYNAbI75ql10")  # Set this on Render.com

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    chat_id = update.effective_chat.id

    # Keyword-based responses (Hindi + English)
    if any(word in user_message for word in ["hello", "hi", "namaste", "नमस्ते"]):
        reply = "Hello! नमस्ते! कैसे मदद कर सकता हूँ?"
    elif any(word in user_message for word in ["price", "कीमत", "rate"]):
        reply = "Price ₹499 है। For details, visit our website."
    elif any(word in user_message for word in ["help", "मदद", "support"]):
        reply = "Support के लिए @admin को message करें।"
    elif any(word in user_message for word in ["bye", "अलविदा", "goodbye"]):
        reply = "Goodbye! फिर मिलेंगे।"
    else:
        reply = "माफ कीजिए, मैं समझ नहीं पाया। कृपया फिर से लिखें।"

    await context.bot.send_message(chat_id=chat_id, text=reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
