import telebot

token = "7881582171:AAFLSKL5dl_UGzy2X6xKs7X1IcoUDQ2xn30"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def start(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()