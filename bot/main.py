import telebot

import time

bot = telebot.TeleBot('token')

list=['hello', 'HELLO', 'Hello', 'good morning']

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello,if you first here use /help <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['destroy'])
def destroy(message):
    y = 0
    for x in range(5, 8):
        y = y + 2
        b = x - y
        bot.send_message(message.chat.id, "Destoy in %s" % b, parse_mode='html')
        time.sleep(1)

    bot.send_message(message.chat.id, 'BOOM')

    image = open('Boom.png', 'rb')
    bot.send_photo(message.chat.id, image)

@bot.message_handler(commands=['help'])
def help(message):
    mass = 'you can use this command( /start, /help, /destroy)'
    bot.send_message(message.chat.id, mass, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text in list:
        bot.send_message(message.chat.id, "what are you want?", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "I don`t understant", parse_mode='html')


bot.polling(none_stop=True)