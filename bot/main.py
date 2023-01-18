import telebot

from glob import glob

import datetime

import time


bot = telebot.TeleBot('token')

list=['hello', 'HELLO', 'Hello', 'good morning']


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello,if you first here use /help <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['destroy'])
def destroy(message):
    for x in range(3, 0, -1):
        bot.send_message(message.chat.id, "Destoy in %s" % x, parse_mode='html')
        time.sleep(1)

    bot.send_message(message.chat.id, f'<b>Dima</b> have became dictator of <b>KNDR</b> ', parse_mode='html')

    image = open('Boom.png', 'rb')
    bot.send_photo(message.chat.id, image)

@bot.message_handler(commands=['help'])
def help(message):
    mass = 'you can use this command( /start, /help, /destroy, /photo)'
    bot.send_message(message.chat.id, mass, parse_mode='html')


@ bot.message_handler(commands=['photo'])
def photo(message):
    files_found = glob("D:\щош\*Без*")

    for picture in files_found:
        photo = open(picture, 'rb')
        bot.send_photo(message.chat.id, photo)


@bot.message_handler()
def get_user_text(message):
    if message.text in list:
        bot.send_message(message.chat.id, "what are you want?", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "I don`t understant", parse_mode='html')


bot.polling(none_stop=True)