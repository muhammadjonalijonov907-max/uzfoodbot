from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
from data import restaurants


def restaurant_keyboard():

    keyboard=[[r] for r in restaurants]

    return ReplyKeyboardMarkup(keyboard,resize_keyboard=True)


def menu_keyboard(menu):

    keyboard=[[m] for m in menu]
    keyboard.append(["⬅ Orqaga"])

    return ReplyKeyboardMarkup(keyboard,resize_keyboard=True)


def quantity_keyboard():

    keyboard=[
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"],
        ["⬅ Orqaga"]
    ]

    return ReplyKeyboardMarkup(keyboard,resize_keyboard=True)


def type_keyboard():

    keyboard=[
        ["🍽 Oshxonada ovqatlanish"],
        ["🥡 Olib ketish"],
        ["⬅ Orqaga"]
    ]

    return ReplyKeyboardMarkup(keyboard,resize_keyboard=True)


def admin_keyboard(order_id):

    keyboard=[
        [
            InlineKeyboardButton("✅ Bor",callback_data=f"yes_{order_id}"),
            InlineKeyboardButton("❌ Yo'q",callback_data=f"no_{order_id}")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def time_keyboard(order_id):

    times=[5,10,15,20,30,60]

    keyboard=[]

    for t in times:
        keyboard.append([InlineKeyboardButton(f"{t} min",callback_data=f"time_{order_id}_{t}")])

    return InlineKeyboardMarkup(keyboard)