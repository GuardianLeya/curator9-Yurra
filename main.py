import telebot

bot = telebot.TeleBot('6555900620:AAEcnkucKTUqZGqcgKN7eqn8t8gtcG79VeE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здраствуйте, выберите нужный раздел', parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'command1 - Description \n'
                                      'command2 - Чемпионаты России \n'
                                      'command3 - Чемпионаты Англии \n'
                                      'command4 - Чемпионаты Испании \n'
                                      'command5 - Чемпионаты Италии \n'
                                      'command6 - Чемпионаты Испании \n'
                                      'command7 - Чемпионаты Франции \n'
                                      'command8 - Чемпионаты Португалии \n'
                                      'command9 - Чемпионаты Нидерландов \n'
                                      'command10 - Чемпионаты Бразилии \n'
                                      'command11 - Чемпионат Саудовской Про Лиги.', parse_mode='Markdown')

bot.infinity_polling()
