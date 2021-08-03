
import Users as u
from telegram import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from cons import  *


menu_button = [['Каталог', 'Корзина'], ['Связаться с нами']]

kat_button =[['Для роддома', 'Личная гигиена', 'Товары для дома'], ['Главное меню']]

dom_button = [['Бытовая химия'], ['Главное меню']]

add_chistin_but = [InlineKeyboardButton('Добавить в корзину('+str(u.chistin.cost)+' сум)', callback_data='chistin')]

roddom_button = [['Сумка в роддом'], ['Главное меню']]

sumka_button = [InlineKeyboardButton('Добавить в корзину('+str(u.sumka.cost)+' сум)', callback_data='bag')]

shamp_button = [['Шампуни'], ['Каталог', 'Главное меню']]

add_shamp_but = [InlineKeyboardButton('Добавить в корзину('+str(u.shamp.cost)+' сум) ', callback_data='shamp')]

order_but = [InlineKeyboardButton('Оформить заказ', callback_data='order'), InlineKeyboardButton('Очистить корзину', callback_data='clear_cart')]

def get_menu(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id,text='Выберете нужный вам раздел.',reply_markup=ReplyKeyboardMarkup(menu_button, resize_keyboard=True))

def get_kat(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id,text='Выберете нужный вам раздел.',reply_markup=ReplyKeyboardMarkup(kat_button, resize_keyboard=True))

def feedback(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id, text = 'United Distribution\n+998 90 117 08 37')

def roddom(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(user_id, 'Выберите продукцию', reply_markup = ReplyKeyboardMarkup(roddom_button,  resize_keyboard=True))

def sumka(update, context):
    user_id = update.message.chat_id

    #context.bot.send_photo(user_id, 'Photo/photo_2021-08-02_20-38-59.jpg',caption=SUMKA, reply_markup = InlineKeyboardMarkup([sumka_button]))
    with open('Photo\sumka.jpg', 'rb') as ph:
        photo = ph.read()
    context.bot.send_photo(user_id, photo, caption=SUMKA, reply_markup = InlineKeyboardMarkup([sumka_button]))
    #context.bot.send_message(user_id, SUMKA,reply_markup = InlineKeyboardMarkup([sumka_button]))

def add_sumka(update, context):
    user_id = update.callback_query.from_user.id

    for us in u.users:
        if user_id == us.id:
            us.basket.append(u.sumka)
    context.bot.send_message(user_id, 'Сумка добавлена в корзину', reply_markup=ReplyKeyboardMarkup(menu_button, resize_keyboard=True))

def gig(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(user_id, 'Выберите товар', reply_markup=ReplyKeyboardMarkup(shamp_button,resize_keyboard=True))

def shamp(update, context):
    user_id = update.message.chat_id
    #context.bot.send_message(user_id, SHAMP, reply_markup=InlineKeyboardMarkup([add_shamp_but]))
    with open('Photo\shampun.jpg', 'rb') as ph:
        photo = ph.read()
    context.bot.send_photo(user_id, photo, caption=SHAMP, reply_markup = InlineKeyboardMarkup([add_shamp_but]))

def add_shamp(update, context):
    user_id = update.callback_query.from_user.id

    for us in u.users:
        if user_id == us.id:
            us.basket.append(u.shamp)
    context.bot.send_message(user_id, 'Шампунь добавлен в корзину', reply_markup=ReplyKeyboardMarkup(menu_button, resize_keyboard=True))

def dom(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(user_id, 'Выберите товар', reply_markup=ReplyKeyboardMarkup(dom_button, resize_keyboard=True))

def chistin(update, context):
    user_id = update.message.chat_id
    #context.bot.send_message(user_id, CHISTIN, reply_markup=InlineKeyboardMarkup([add_chistin_but]))
    with open('Photo\chistin.jpg', 'rb') as ph:
        photo = ph.read()
    context.bot.send_photo(user_id, photo, caption=CHISTIN, reply_markup = InlineKeyboardMarkup([add_chistin_but]))

def add_chistin(update, context):
    user_id = update.callback_query.from_user.id

    for us in u.users:
        if user_id == us.id:
            us.basket.append(u.chistin)
    context.bot.send_message(user_id, 'Чистин добавлен в корзину', reply_markup=ReplyKeyboardMarkup(menu_button, resize_keyboard=True))

def cart(update, context):
    user_id = update.message.chat_id
    total_cost = 0
    for us in u.users:
        if user_id == us.id:
            if len(us.basket) != 0:
                for tov in us.basket:
                    total_cost += tov.cost
                context.bot.send_message(user_id, 'Корзина:\n'+'\n'.join(map(str, us.basket))+'\nОбщая стоимость: '+str(total_cost),
                                         reply_markup=InlineKeyboardMarkup([order_but]))
            else:
                context.bot.send_message(user_id, 'Корзина пуста')



def order(update, context):
    user_id = update.callback_query.from_user.id
    for us in u.users:
        if user_id == us.id:
            context.bot.send_message(ADMIN_ID, 'Новый заказ. Заказ:\n'+
                                     '\n'+str(us.contact)+'\n'+'Язык: '+us.lang+'\n'+
                                     '\n'.join(map(str, us.basket)))
            context.bot.send_location(ADMIN_ID, latitude=us.location['latitude'],
                                      longitude=us.location['longitude'])
            context.bot.send_message(user_id, 'Спасибо, Ваш заказ оформлен\nЖдите звонка нашего'+
                                     ' оператора', reply_markup=ReplyKeyboardMarkup(menu_button,resize_keyboard=True))

def clear_cart(update, context):
    user_id = update.callback_query.from_user.id
    for us in u.users:
        if user_id == us.id:
            us.basket.clear()
            context.bot.send_message(user_id, 'Корзина очищена', reply_markup = ReplyKeyboardMarkup(menu_button, resize_keyboard=True))
