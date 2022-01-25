import telebot
import secrets
from telebot import types

bot = telebot.TeleBot('5091567583:AAGZ--Xp80P9OctOr-GGOC8PPZuIvltymFI')

def rand_num():
    while True:
        num = input('Для рассчета введите букву n ')
        if num == "n":
            numbers = []
            while (len(numbers)) < 7:
                number = secrets.randbelow(50)
                if number not in numbers and number > 0:
                    numbers.append(number)
            print(sorted(numbers))



def rn():
    numbers = []
    while (len(numbers)) < 7:
        number = secrets.randbelow(50)
        if number not in numbers and number > 0:
            numbers.append(number)
    print(sorted(numbers))






markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('Получить 7 чисел')
markup.add(btn1)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('1')
btn2 = types.KeyboardButton('2')
markup2.add(btn1, btn2)

@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    #bot.send_message(message.chat.id,  "Let`s start!", reply_markup=markup)
    send_mess = f"Привет, {username}! Нажми на кнопку, чтоб получить 7 чисел)"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup)



def mess(message):
    send_mess = "Выбери подходящий вариант"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text =='начать тест заново')
def foo(message):
    final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text =="Получить 7 чисел")
def foo(message):
    numbers = []
    while (len(numbers)) < 7:
        number = secrets.randbelow(50)
        if number not in numbers and number > 0:
            numbers.append(number)

    num = str(sorted(numbers))
    bot.send_message(message.chat.id, num, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
