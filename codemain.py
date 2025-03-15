import telebot

token = '7251843209:AAF1lx4tFnsAPbtpbUezxO5xUv4DwjBsGLU'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello there")


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, "No one will help you ")


@bot.message_handler(content_types=['text'])
def new_message(message):
    if message.text == "Hello there":
        bot.send_message(message.chat.id, "General Kenobi")
    elif message.text == "Доброе утро":
        bot.send_message(message.chat.id, "https://media.tenor.com/vZPFii0AJScAAAAd/darth-vader-vader.gif")

    elif message.text == "Hello there!":
        bot.send_message(message.chat.id, "General Kenobi!!! kha")
    elif message.text == "Да":
        bot.send_message(message.chat.id, "Не задохнитесь в своих амбициях")
    elif message.text == "gif":
        bot.send_animation(message.chat.id, "https://i.gifer.com/XTWJ.gif")
    elif message.text == "Где император?":
        bot.send_animation(message.chat.id, "https://avatars.mds.yandex.net/get-pdb/1889015/d4086fa6-47c8-47d2-bb41-244b00921bc7/orig")
    elif message.text == "Кто это?":
        bot.send_message(message.chat.id, "Jedy skam!")
    elif message.text == "Что это?":
        bot.send_message(message.chat.id, "Jedy skam!")
    elif message.text == "эники беники":
        bot.send_message(message.chat.id, "ели вареники")
    elif message.text == "Эй!":
        bot.send_message(message.chat.id, "Are you talking with me?")
    elif message.text == "Го рубить повстанцев?":
        bot.send_message(message.chat.id, "го")
    elif message.text == "Танцуем":
        bot.send_animation(message.chat.id, "https://i.gifer.com/embedded/download/Wj9w.gif")

    elif message.text == "ты отстой, вэйдер":
        bot.send_animation(message.chat.id,
                           "https://i.pinimg.com/originals/99/13/1f/99131f0b92365a426cf348216a85a4c4.gif")
    else:
        bot.send_message(message.chat.id, "go f*ck yourself")

bot.polling(none_stop=True)
