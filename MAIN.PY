import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get(8876606341:AAFovrrAP7wYtpFtaKo6QYwQlQBK4Cu7EA4")
GROQ_KEY = os.environ.get("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")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        r = requests.post("https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_KEY}"},
            json={"model": "llama3-8b-8192", "messages": [{"role": "user", "content": user_text}]},
            timeout=30)
        answer = r.json()['choices'][0]['message']['content']
    except Exception as e:
        answer = f"Error: {e}"
    await update.message.reply_text(answer)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
print("Bot LIVE on Render")
app.run_polling()
