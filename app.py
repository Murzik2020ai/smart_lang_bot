# t.me/smart_lang_bot
  
#pip install pytelegrambotapi
import telebot
import pandas as pd
import numpy as np
import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

import config

bot = telebot.TeleBot(config.token)
#switch to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
#load language model
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru").to(device)

@bot.message_handler(commands=['start','help'])
def start(message):
    start_message='''✌️✌️✌️✌️✌️Это бот-переводчик\n\
                 Выможете отправить мне фразу на английском языке и я ее переведу на русский.\n\
                 Это и много другое я уже умею!✌️\n'''
    bot.send_message(message.chat.id,start_message)
    

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    '''
    fucn handes messages from user in text format
    '''
    str = message.text+'.'


    translation_tokenized = model.generate(**tokenizer(str.split('.')[0], return_tensors="pt", padding=True))
    result = [tokenizer.decode(t, skip_special_tokens=True) for t in translation_tokenized]
    answer = '>eng_rus> '+result[0]

    bot.send_message(message.chat.id, answer)
if __name__ == '__main__':
    print('bot started.')
    bot.polling(none_stop=True)
