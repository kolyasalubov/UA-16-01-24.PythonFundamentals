import telebot
bot = telebot.TeleBot('7169218123:AAGvGHxjkK4QJquwPSCYbRoZHPILizkKr6A')

# @bot.message_handler()
# def info(message):

carbohydrates = {'рис', 'гречка','булгур','паста'}

@bot.message_handler(commands=['start', 'restar'])

def main(message):
    bot.send_message(message.chat.id, 'привіт')
   
@bot.message_handler(content_types=['text'])
def calc(message):
    global carbohydrates
    cal = int(message.text)
    morning = int((cal *36) / 100)
    print(morning)
    bot.reply_to(message, 'Вибери їжу')
    
    for item in enumerate(carbohydrates, 1):
        print(item, sep = ". ")
        bot.reply_to(message)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Скільки ?")

bot.infinity_polling()