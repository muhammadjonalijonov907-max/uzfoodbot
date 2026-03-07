import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from handlers.start import start
from handlers.message import message_handler, button_handler
from handlers.admin import orders_command
from database import init_db
from config import BOT_TOKEN


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("orders", orders_command))
app.add_handler(MessageHandler(filters.TEXT, message_handler))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot ishlayapti...")

init_db()

app.run_polling()