import telebot 
from pygame import mixer
#6192276630:AAEsrsSS0gkcfekkDBr_wW7Z2q1yM2KtCkI
bot = telebot.TeleBot('6192276630:AAEsrsSS0gkcfekkDBr_wW7Z2q1yM2KtCkI')

keyword = 'play'

@bot.message_handler(commands=['start']) 
def start_message(message): 
    bot.send_message(message.chat.id, "To play music reply with the keyword 'play'")

@bot.message_handler(content_types=['text']) 
def send_text(message): 
    if message.text.lower() == keyword: mixer.init() 
    # mixer.music.load('song.mp3') 
    # mixer.music.play()
    print ("hello")

bot.polling()




from telebot import TeleBot

bot = telebot.TeleBot('6192276630:AAEsrsSS0gkcfekkDBr_wW7Z2q1yM2KtCkI')

#Handle /start 
@bot.message_handler(commands=['start']) 
def send_welcome(message): 
    bot.reply_to(message, 'Welcome!')

bot.polling()