import telebot
import telegram
from telebot import types
from telegram.ext import Updater, CommandHandler


TOKEN = "***"
tb = telebot.TeleBot(TOKEN)
bot = telebot.TeleBot(TOKEN)



def get_pdf(update, context):
    # загрузка файла PDF
    with open('example.pdf', 'rb') as f:
        # отправка файла пользователю
        update.message.reply_document(document=f)
@bot.message_handler(commands=["start"])
def start(message): # Название функции не играет никакой роли
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Русский')
    btn2 = types.InlineKeyboardButton(text='Englesh')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id,
                     'Привет, перед нашим общением напишите язык на котором будет общение Русский или Английский(Hello,before our communication, which will communicate Russian or English)',
                     parse_mode='html')
@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Русский":
        bot.send_message(message.chat.id,
                     '<b>Меня зовут Атлас, я помощник главного менеджера "WebTrader" и я постараюсь ответить на все ваши вопросы</b>',
                     parse_mode='html')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Пользовательское_соглашение')
        btn2 = types.InlineKeyboardButton(text='Что_такое_WebTrader')
        btn3 = types.InlineKeyboardButton(text='Что_я_могу_продавать')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.from_user.id,
                     "По кнопкам ниже можно задать базовые вопросы, в случаи если у вас есть не отвечанные вопросы то обращайтесь главному меннеджеру: https://t.me/StalinOnlineNumber1",
                     reply_markup=markup)
    elif message.text == "England":
        bot.send_message(message.chat.id,
                     'My name is Atlas, I am the assistant to the general manager of "WebTrader" and I will try to answer all your questions',
                     parse_mode='html')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Terms_of_use')
        btn2 = types.InlineKeyboardButton(text='What_is_WebTrader')
        btn3 = types.InlineKeyboardButton(text='What_i_can_trade')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.from_user.id,
                     "Using the buttons below, you can ask basic questions, in case you have unanswered questions, please contact the main manager: https://t.me/StalinOnlineNumber1",
                     reply_markup=markup)

    elif message.text == "Пользовательское_соглашение":
        bot.send_message(message.chat.id, "http://downloadlinks.ru/%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%BE%D0%B5_%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%88%D0%B5%D0%BD%D0%B8%D0%B5.pdf", parse_mode='html')

    elif message.text == "Terms_of_use":
        bot.send_message(message.chat.id,
                         "http://downloadlinks.ru/%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%BE%D0%B5_%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%88%D0%B5%D0%BD%D0%B8%D0%B5.pdf",
                         parse_mode='html')
    elif message.text == "What_is_'WebTrader'":
        bot.send_message(message.chat.id,"This is an information system for selling your things and other users",parse_mode='html')
    elif message.text == "What_i_can_trade'":
        bot.send_message(message.chat.id, "You can sell whatever you like, but what is allowed in your country, elif you still sell what is prohibited in your country, we will be forced to report this to the authorized bodies of your state",
                         parse_mode='html')
    elif message.text == "Что_я_могу_продавать":
        bot.send_message(message.chat.id,
                             "Вы можете продавать что душе угодно, но и то что разрешено в вашей стране, если вы все же будете продавать то что запрещено в вашей стране, мы будем вынуждены сообщить об этом в уполномоченые органы ващего государства",
                             parse_mode='html')
    elif message.text == "Что_такое_WebTrader":
        bot.send_message(message.chat.id,
                             "Это информационная система для продажи ващих вещей так и других пользователей",
                             parse_mode='html')
    else:
        bot.send_message(message.chat.id,
                 "I beg your pardon, but I do not understand what you are saying (if you have a question that I could not answer, write to the general manager: https://t.me/StalinOnlineNumber1)",
                 parse_mode='html')
        bot.send_message(message.chat.id, "Прошу прошение, но я не понимаю что вы говорите(если у вас есть вопрос на который я не смог ответить пишите главному менеджеру: https://t.me/StalinOnlineNumber1)", parse_mode='html')



bot.polling(none_stop=True)

