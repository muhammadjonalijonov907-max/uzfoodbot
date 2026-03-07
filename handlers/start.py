from telegram import Update
from telegram.ext import ContextTypes
from keyboards.menu_keyboard import restaurant_keyboard
from handlers.message import user_state


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id

    user_state[user_id] = "start"

    await update.message.reply_text(
        "Assalomu alaykum 👋\n\nOshxonani tanlang:",
        reply_markup=restaurant_keyboard()
    )