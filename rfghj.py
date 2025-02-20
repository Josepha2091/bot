import telebot
from telebot import types

bot = telebot.TeleBot('8195763195:AAGSU0izf3m1KQyLjekBIi4vE5awqs-kfZY')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Кнопка 1", callback_data='1')
    btn2 = types.InlineKeyboardButton("Кнопка 2", callback_data='2')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Пожалуйста, выберите:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == '1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали вариант 1")
        elif call.data == '2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали вариант 2")
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="Неизвестная команда")
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
