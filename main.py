import telebot

bot = telebot.TeleBot('5751300078:AAExYVTnPW7WsPSzn-iGxAbpIl5aufZ6ztk')


@bot.message_handler(commands=['start'])
def start(message):
    pid = message.from_user.id
    if str(pid) == '1000105342':
        bot.send_message(message.chat.id, 'Привет зайка. Введи сумму оборота твоих продаж: ')
    else:
        bot.send_message(message.chat.id, 'Я чувствую что ты не зая, сука')


# Ввод суммы оборота
@bot.message_handler()
def get_user_text(message):
    if message.text.isdigit():
        sum_oborot = float(message.text)
        itog = sum_oborot * 0.00484 + 25000
        bot.send_message(message.chat.id, 'Твоя примераная зарплата равна: ' + str(itog) + " вечно деревянных")
    else:
        bot.send_message(message.chat.id, 'Зай,ты накосячила с вводом цифры, не вводи символы или этот бот умрет')


bot.polling(none_stop=True)