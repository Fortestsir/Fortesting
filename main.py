from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = "8183222059:AAF7Q0_fdAlfmy6QV0lwdA-Tcia9YSO-13c"

# Function to handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    chat_id = update.effective_chat.id

    # Keyword-based responses
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

# Bot setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
