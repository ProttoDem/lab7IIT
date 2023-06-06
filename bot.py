import telebot
import datetime
import fluent.sender

bot_token = '6036098503:AAHUk0XuznNMgiG5Luk2b4G7iLFh2iUlvJE'

fluentd_host = '127.0.0.1'
fluentd_port = 24224


bot = telebot.TeleBot(bot_token)

logger = fluent.sender.FluentSender('telegram_bot', host=fluentd_host, port=fluentd_port)
time = ""
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    response ="Відповідь від бота: " + user_input + " "

    log_message(user_input, response)

    bot.send_message(message.chat.id, response)

def log_message(user_input, generated_text):
    log_data = {
        'user_input': user_input,
        'generated_text': generated_text
    }
    logger.emit('telegram_message', log_data)

bot.polling()