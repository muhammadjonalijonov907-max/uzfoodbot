from telegram import Update
from telegram.ext import ContextTypes
from database import get_orders

ADMIN_ID = 5378140881


async def orders_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text("Siz admin emassiz ❌")
        return

    orders = get_orders()

    if not orders:
        await update.message.reply_text("Buyurtmalar yo'q")
        return

    text = "📦 Buyurtmalar ro'yxati:\n\n"

    for order in orders:

        order_id = order[0]
        restaurant = order[2]
        food = order[3]
        quantity = order[4]
        status = order[5]

        text += (
            f"#{order_id}\n"
            f"{restaurant}\n"
            f"{food} - {quantity} ta\n"
            f"Status: {status}\n\n"
        )

    await update.message.reply_text(text)