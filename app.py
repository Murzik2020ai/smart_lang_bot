# t.me/smart_lang_bot
  
#pip install pytelegrambotapi
import telebot


import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start','help'])
def start(message):
    start_message='''✌️✌️✌️✌️✌️Это бот-переводчик\n\
                 Выможете выбрать несколько \n\
                 направлений перевода.\n\
                 Например англо-русский\n\
                 (команда /eng_rus)\n\
                 Русско-английский\n\
                 (команда /rus_eng)\n\
                 Это и много другое я уже умею!✌️\n'''
    bot.send_message(message.chat.id,start_message)
    
    
@bot.message_handler(commands=['eng_rus'])
def start(message):
    init_message='''✌️✌️✌️✌️✌️Перевод с английского на русский язык.\n\
                 Функционал в разработке!\n'''
    bot.send_message(message.chat.id,init_message)


@bot.message_handler(commands=['rus_eng'])
def start(message):
    init_message='''✌️✌️✌️✌️✌️Перевод с русского на английский язык.\n\
                 Функционал в разработке!\n'''
    bot.send_message(message.chat.id,init_message)

    
@bot.message_handler(commands=['eng_germ'])
def start(message):
    init_message='''✌️✌️✌️✌️✌️Перевод с английского на немецкий язык.\n\
                 Функционал в разработке!\n'''
    bot.send_message(message.chat.id,init_message)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    answer = f'{message.from_user.first_name} , you send wrong command! Try /eng_rus, /rus_eng'

    bot.send_message(message.chat.id, answer)
if __name__ == '__main__':
    print('bot started.')
    bot.polling(none_stop=True)