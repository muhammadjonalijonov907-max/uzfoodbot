from telegram import Update
from telegram.ext import ContextTypes

from data import menus,admins
from keyboards import menu_keyboard,quantity_keyboard,type_keyboard,admin_keyboard
from database import add_order

from handlers.start import user_state,user_data


async def message_handler(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user_id=update.message.from_user.id
    text=update.message.text

    state=user_state.get(user_id)

    if state=="restaurant":

        user_data[user_id]={"restaurant":text}
        user_state[user_id]="food"

        await update.message.reply_text(
            "Ovqat tanlang:",
            reply_markup=menu_keyboard(menus[text])
        )


    elif state=="food":

        if text=="⬅ Orqaga":
            user_state[user_id]="restaurant"
            return

        user_data[user_id]["food"]=text
        user_state[user_id]="quantity"

        await update.message.reply_text(
            "Nechta?",
            reply_markup=quantity_keyboard()
        )


    elif state=="quantity":

        if text=="⬅ Orqaga":
            user_state[user_id]="food"
            return

        user_data[user_id]["quantity"]=text
        user_state[user_id]="type"

        await update.message.reply_text(
            "Oshxonada ovqatlanish yoki olib ketish?",
            reply_markup=type_keyboard()
        )


    elif state=="type":

        order_type=text

        data=user_data[user_id]

        order_id=add_order(
            user_id,
            data["restaurant"],
            data["food"],
            data["quantity"],
            order_type
        )

        admin_id=admins[data["restaurant"]]

        await context.bot.send_message(
            admin_id,
            f"Yangi zakaz\n\n{data['restaurant']}\n{data['food']} {data['quantity']} ta\n{order_type}",
            reply_markup=admin_keyboard(order_id)
        )

        await update.message.reply_text(
            "📦 Buyurtmangiz oshxonaga yuborildi.\n\n"
            "Iltimos biroz kuting ⏳"
        )

        user_state[user_id]="done"