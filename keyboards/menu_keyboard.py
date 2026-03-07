from telegram import ReplyKeyboardMarkup
from data import restaurants, menu


def restaurant_keyboard():

    keyboard = [[r] for r in restaurants]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def menu_keyboard():

    keyboard = [[m] for m in menu.keys()]
    keyboard.append(["⬅ Orqaga"])

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def quantity_keyboard():

    keyboard = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["⬅ Orqaga"]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)