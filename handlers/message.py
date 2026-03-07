from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data import restaurants, menu
from keyboards.menu_keyboard import menu_keyboard, quantity_keyboard, restaurant_keyboard
from database import add_order, update_status


orders = {}
user_state = {}
order_counter = 1000



async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.message.from_user.id

    state = user_state.get(user_id)

    # ORQAGA
    if text == "⬅ Orqaga":

        if state == "menu":

            user_state[user_id] = "start"

            await update.message.reply_text(
                "Oshxonani tanlang:",
                reply_markup=restaurant_keyboard()
            )

        elif state == "quantity":

            user_state[user_id] = "menu"

            await update.message.reply_text(
                "Menyudan tanlang:",
                reply_markup=menu_keyboard()
            )

        return


    # RESTAURANT TANLASH
    if text in restaurants:

        orders[user_id] = {"restaurant": text}

        user_state[user_id] = "menu"

        await update.message.reply_text(
            f"{text} menyusi 🍽",
            reply_markup=menu_keyboard()
        )


    # OVQAT TANLASH
    elif text in menu:

        food = menu[text]

        orders[user_id]["food"] = food

        user_state[user_id] = "quantity"

        await update.message.reply_text(
            "Nechta buyurtma qilasiz?",
            reply_markup=quantity_keyboard()
        )


    # SON TANLASH
    elif text.isdigit() and state == "quantity":

        global order_counter

        quantity = int(text)

        order_counter += 1
        order_id = order_counter

        restaurant = orders[user_id]["restaurant"]
        food = orders[user_id]["food"]

        orders[order_id] = {
            "user_id": user_id,
            "restaurant": restaurant,
            "food": food,
            "quantity": quantity
        }
        add_order(order_id, user_id, restaurant, food, quantity)

        admin_id = 5378140881   # admin telegram id

        keyboard = [
            [
                InlineKeyboardButton("Bor ✅", callback_data=f"yes_{order_id}"),
                InlineKeyboardButton("Yo'q ❌", callback_data=f"no_{order_id}")
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            admin_id,
            f"🍽 Yangi buyurtma #{order_id}\n\n"
            f"Oshxona: {restaurant}\n"
            f"Ovqat: {food}\n"
            f"Soni: {quantity}",
            reply_markup=reply_markup
        )

        await update.message.reply_text(
            "Buyurtmangiz oshxonaga yuborildi ⏳"
        )
async def button_handler(update, context):

    query = update.callback_query
    await query.answer()

    data = query.data

    action, order_id = data.split("_")
    order_id = int(order_id)

    order = orders.get(order_id)

    if not order:
        await query.edit_message_text("Buyurtma topilmadi")
        return

    user_id = order["user_id"]

    if action == "yes":
        update_status(order_id, "accepted")

        await context.bot.send_message(
            user_id,
            f"✅ Buyurtmangiz #{order_id} qabul qilindi"
        )

        await query.edit_message_text(
            f"✅ Buyurtma #{order_id} tasdiqlandi"
        )

    elif action == "no":
        update_status(order_id, "rejected")

        await context.bot.send_message(
            user_id,
            f"❌ Buyurtma #{order_id} rad etildi"
        )

        await query.edit_message_text(
            f"❌ Buyurtma #{order_id} bekor qilindi"
        )
   
   