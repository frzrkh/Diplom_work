class User(object):
    def __init__(self, id = 0, lang = '', name = '', contact = {}, location = '', basket = []):
        self.id = id
        self.name = name
        self.lang = lang
        self.contact = contact
        self.location = location
        self.basket = basket
    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_lang(self, lang):
        self.lang = lang

    def set_contact(self, contact):
        self.contact = contact

    def set_location(self, location):
        self.location = location

    def set_basket(self, basket):
        self.basket = basket

    def __str__(self):
        return 'id: {}, lang: {}, contact: {}, location: {}'.format(self.id, self.lang, self.contact, self.location)

users = []

class Tovar(object):
    def __init__(self, name, cost, id):
        self.cost = cost
        self.name = name
        self.id = id

    def __str__(self):
        return '{}, {} сум'.format(self.name, self.cost)

sumka = Tovar('Сумка для роддома', 349115, 'sumka_rm')

shamp = Tovar('Шампунь', 16000, 'shamp_rm')

chistin = Tovar('Чистин Универсал', 15000, 'chistin_rm')