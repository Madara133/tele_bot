import telebot
import random
from my_token import token




bot = telebot.TeleBot(token)
keybord = telebot.types.ReplyKeyboardMarkup()

butn1 = telebot.types.KeyboardButton('Играть')
butn2 = telebot.types.KeyboardButton('Нет')


keybord.add(butn1,butn2)





@bot.message_handler(commands=['start', 'help'])
def start_message(message):
#  bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI2w2S1PC9EtdTL6QQAAUac9jF-f5MYMwACCAADwDZPE29sJgveGptpLwQ')

    msg = bot.send_message(message.chat.id, f'Привет, {message.chat.first_name} , начнем игру', reply_markup=keybord)
    bot.register_next_step_handler(msg, chek_answer)


def chek_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Ок, тогда вот правила: нужно угадать число от 1 до 10 за 3 попытки')
        random_number = random.randint(1,10)
        start_game(message, 3, random_number)
    else:
        bot.send_message(message.chat.id, 'Ну и ладно')

def start_game(message, attempts,random_number):
    msg  = bot.send_message(message.chat.id, 'Введи число')
    bot.register_next_step_handler(msg, check_number, attempts - 1, random_number)

def check_number(message, attempts, random_number):
    if message.text == str(random_number):
        bot.send_message(message.chat.id, 'Вы победили')
        bot.send_photo(message.chat.id, 'https://christianindex.org/stories/your-church-needs-to-reflect-some-measure-of-victory,971')
    elif attempts == 0:
        bot.send_message(message.chat.id, f'Извините но у вас закончились попытки. Число было - {random_number}')
    else:
        bot.send_message(message.chat.id, f'Попробуйте еще раз, у вас осталось {attempts} попыток')
        start_game(message, attempts, random_number)



bot.polling()
















































