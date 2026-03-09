from telegram import Update
from telegram.ext import ContextTypes

from keyboards import time_keyboard
from database import get_user


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    data = query.data

    await query.answer()

    # BOR
    if data.startswith("yes_"):

        order_id = data.split("_")[1]

        # eski tugmalarni o'chirish
        await query.edit_message_reply_markup(reply_markup=None)

        # vaqt tanlashni chiqarish
        await query.message.reply_text(
            "⏳ Qancha vaqtda tayyor?",
            reply_markup=time_keyboard(order_id)
        )


    # YO'Q
    elif data.startswith("no_"):

        order_id = data.split("_")[1]

        user_id = get_user(order_id)

        await query.edit_message_reply_markup(reply_markup=None)

        await context.bot.send_message(
            user_id,
            "❌ Afsuski mahsulot hozir mavjud emas\n\n"
            "Boshqa buyurtma uchun /start ni bosing"
        )

        await query.message.reply_text("Mijozga mahsulot yo'q deb yuborildi")


    # VAQT TANLASH
    elif data.startswith("time_"):

        parts = data.split("_")

        order_id = parts[1]
        time = parts[2]

        user_id = get_user(order_id)

        # tugmalarni o'chirish
        await query.edit_message_reply_markup(reply_markup=None)

        # admin chatida yozuv qoladi
        await query.message.reply_text(
            f"Mijozga yetkazildi✅"
        )

        # mijozga yuboriladi
        await context.bot.send_message(
            user_id,
            f"✅ Buyurtmangiz qabul qilindi\n\n"
            f"⏳ Tayyor bo'lish vaqti: {time} minut\n\n"
            f"Yana buyurtma uchun /start ni bosing"
        )