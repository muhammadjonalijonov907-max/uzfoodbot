from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,CallbackQueryHandler,filters

from handlers.start import start
from handlers.message import message_handler
from handlers.admin_buttons import button_handler

from database import init_db
from config import BOT_TOKEN


app=ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start",start))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,message_handler))

app.add_handler(CallbackQueryHandler(button_handler))

init_db()

print("Bot ishlayapti...")

app.run_polling()