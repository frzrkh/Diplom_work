from telegram.ext import Updater, Dispatcher, MessageHandler, CommandHandler, CallbackQueryHandler, Filters
from func import *
from menu import *
from cons import TOKEN
import Users as u
updater = Updater(token = TOKEN, workers = 4)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('Start', start, run_async=True))
dispatcher.add_handler(CallbackQueryHandler(pattern='rus', callback=rus))
dispatcher.add_handler(CallbackQueryHandler(pattern='uzb', callback=uzb))
dispatcher.add_handler(MessageHandler(Filters.contact, callback=get_contact))
dispatcher.add_handler(MessageHandler(Filters.location, callback=get_location))
dispatcher.add_handler(MessageHandler(Filters.text('Каталог'), callback=get_kat))
dispatcher.add_handler(MessageHandler(Filters.text('Главное меню'), callback=get_menu))
dispatcher.add_handler(MessageHandler(Filters.text('Связаться с нами'), callback=feedback))
dispatcher.add_handler(MessageHandler(Filters.text('Для роддома'), callback=roddom))
dispatcher.add_handler(MessageHandler(Filters.text('Сумка в роддом'), callback=sumka))
dispatcher.add_handler(CallbackQueryHandler(pattern='bag', callback=add_sumka))
dispatcher.add_handler(MessageHandler(Filters.text('Личная гигиена'), callback=gig))
dispatcher.add_handler(MessageHandler(Filters.text('Шампуни'), callback=shamp))
dispatcher.add_handler(CallbackQueryHandler(pattern='shamp', callback=add_shamp))
dispatcher.add_handler(MessageHandler(Filters.text('Товары для дома'), callback=dom))
dispatcher.add_handler(MessageHandler(Filters.text('Бытовая химия'), callback=chistin))
dispatcher.add_handler(CallbackQueryHandler(pattern='chistin', callback=add_chistin))
dispatcher.add_handler(MessageHandler(Filters.text('Корзина'), callback=cart))
dispatcher.add_handler(CallbackQueryHandler(pattern='order', callback=order))
dispatcher.add_handler(CallbackQueryHandler(pattern='clear_cart', callback=clear_cart))
updater.start_polling(drop_pending_updates=True)