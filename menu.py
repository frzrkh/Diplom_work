from cons import *
import Users as u
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

menu_button = [KeyboardButton(text='Каталог'),KeyboardButton(text='Корзина'),KeyboardButton(text='Связаться с нами')]

kat_button = [KeyboardButton(text='Для роддома'), KeyboardButton(text='Личная гигиена'),
                      KeyboardButton(text='Товары для дома'),  KeyboardButton(text='Главное меню')]

roddom_button = [KeyboardButton('Сумка в роддом'), KeyboardButton('Главное меню')]

sumka_button = [InlineKeyboardButton('Добавить в корзину ', callback_data='bag')]

shamp_button = [KeyboardButton('Шампуни'), KeyboardButton('Каталог'), KeyboardButton('Главное меню')]

add_shamp_but = [InlineKeyboardButton('Добавить в корзину ', callback_data='shamp')]

def get_menu(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id,text='Выберете нужный вам раздел.',reply_markup=ReplyKeyboardMarkup([menu_button], resize_keyboard=True))

def get_kat(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id,text='Выберете нужный вам раздел.',reply_markup=ReplyKeyboardMarkup([kat_button], resize_keyboard=True))

def feedback(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id, text = 'United Distribution\n+998 90 117 08 37')

def roddom(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(user_id, 'Выберите продукцию', reply_markup = ReplyKeyboardMarkup([roddom_button]))

def sumka(update, context):
    user_id = update.message.chat_id

    #context.bot.send_photo(user_id, 'Photo/photo_2021-08-02_20-38-59.jpg',caption=SUMKA, reply_markup = InlineKeyboardMarkup([sumka_button]))
    context.bot.send_message(user_id, SUMKA,reply_markup = InlineKeyboardMarkup([sumka_button]))

def add_sumka(update, context):
    user_id = update.callback_query.from_user.id

    for us in u.users:
        if user_id == us.id:
            us.append(u.sumka)
    context.bot.send_message(user_id, 'Сумка добавлена в корзину', reply_markup=ReplyKeyboardMarkup([menu_button]))

def gig(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(user_id, 'Выберите товар', reply_markup=ReplyKeyboardMarkup([shamp_button]))

def shamp(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(user_id, SHAMP, reply_markup=InlineKeyboardMarkup([add_shamp_but]))

def add_shamp(update, context):
    user_id = update.callback_query.from_user.id

    for us in u.users:
        if user_id == us.id:
            us.basket.append(u.shamp)
    context.bot.send_message(user_id, 'Шампунь добавлен в корзину', reply_markup=ReplyKeyboardMarkup([menu_button]))
