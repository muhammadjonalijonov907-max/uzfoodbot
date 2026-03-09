from telegram import Update
from telegram.ext import ContextTypes
from keyboards import restaurant_keyboard

user_state={}
user_data={}

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user_id=update.message.from_user.id

    user_state[user_id]="restaurant"

    await update.message.reply_text(
        "Assalomu alaykum\n\nOshxonani tanlang:",
        reply_markup=restaurant_keyboard()
    )