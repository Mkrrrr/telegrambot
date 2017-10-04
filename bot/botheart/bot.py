import telebot
from telebot import types

token = '389449348:AAGt1xgwvGsnijAQU3VuhqATTO7drZLHjt8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Сделать заказ']])
    msg = bot.send_message(m.chat.id, 'БЛА-БЛА-БЛА',
                     reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)
def name(m):
    if m.text == 'Сделать заказ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['UAH', 'USD','EUR']])
        msg = bot.send_message(m.chat.id, 'Что вы хотите купить?',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, name1)
def name1(m):
    if m.text == 'UAH':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['USD','EUR']])
        msg = bot.send_message(m.chat.id, 'Вы продаёте:',
                                reply_markup=keyboard)
    elif m.text == 'USD':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['UAH','EUR']])
        msg = bot.send_message(m.chat.id, 'Вы продаёте:',
                                 reply_markup=keyboard)
    elif m.text == 'EUR':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['UAH','USD']])
        msg = bot.send_message(m.chat.id, 'Вы продаёте:',
                                 reply_markup=keyboard)
    bot.register_next_step_handler(msg, name2)
def name2(m):
    if m.text == 'UAN':
        bot.send_message(m.chat.id, 'Введите сумму, которую хотите купить')
    elif m.text == 'USD':
        bot.send_message(m.chat.id, 'Введите сумму, которую хотите купить')
    elif m.text == 'EUR':
        bot.send_message(m.chat.id, 'Введите сумму, которую хотите купить')

bot.polling()