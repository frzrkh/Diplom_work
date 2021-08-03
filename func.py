from cons import *
from menu import *
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from sql_req import *
import sqlite3
from Users import User
from Users import users

contact_button = [KeyboardButton('Отправить свой контакт ☎', request_contact=True)]
location_button = [KeyboardButton('Отправить свою локацию 🗺️', request_location=True)]



def start(update, context):
    user_id = update.message.chat_id

    user = User()
    user.set_id(user_id)
    users.append(user)


    name = update.message.from_user.first_name

    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    id_in = cur.execute(id_in_table.format(user_id)).fetchall()

    try:
        id_in = id_in[0][0]
    except IndexError:
        cur.execute(first_insert.format(user_id, name))
        conn.commit()
    buttons = [InlineKeyboardButton(text='Русский', callback_data='rus'),
          InlineKeyboardButton(text='Узбекча', callback_data='uzb')]
    context.bot.send_message(text=MSG_Start, chat_id=user_id, reply_markup=InlineKeyboardMarkup([buttons]))

def rus(update,context):
    global contact_button
    user_id = update.callback_query.from_user.id

    for us in users:
        if user_id == us.id:
            us.set_lang('ru')

    name = update.callback_query.from_user.first_name
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute(update_app_lang.format('ru', user_id))
    conn.commit()
    x = cur.execute(app_lang_in_table.format(user_id)).fetchall()
    x = x[0][0]
    context.bot.send_message(chat_id=user_id, text=MSG_P[x][0].format(name), reply_markup=ReplyKeyboardMarkup([contact_button], resize_keyboard=True, one_time_keyboard=True))




def uzb(update, context):
    global contact_button
    user_id = update.callback_query.from_user.id

    for us in users:
        if user_id == us.id:
            us.set_lang('uz')

    name = update.callback_query.from_user.first_name
    cur.execute(update_app_lang.format('uzb', user_id))
    conn.commit()
    x = cur.execute(app_lang_in_table.format(user_id)).fetchall()
    x = x[0][0]

    context.bot.send_message(chat_id=user_id, text=MSG_P[x][0].format(name),
                         reply_markup=ReplyKeyboardMarkup([contact_button], resize_keyboard=True,
                                                          one_time_keyboard=True))

def get_contact( update, context):
    user_id = update.message.chat_id
    contact = update.message.contact
    for us in users:
        if user_id == us.id:
            us.set_contact(contact)

    context.bot.send_message(chat_id=user_id,text='Спасибо, мы получили Ваш номер телефона! А теперь отправьте Вашу геолокацию', reply_markup=ReplyKeyboardMarkup([location_button],resize_keyboard=True, one_time_keyboard=True) )

def get_location(update, context):
        user_id = update.message.chat_id
        location = update.message.location
        print(location)
        for us in users:
            if user_id == us.id:
                us.set_location(location)

        context.bot.send_message(chat_id=user_id, text='Спасибо, мы получили Ваши данные.', reply_markup=ReplyKeyboardMarkup([menu_button]))



