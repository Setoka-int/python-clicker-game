import telebot


bot = telebot.TeleBot("8294526501:AAFuV5iXagxvsTTNmO8IJdk6thoVRU3zCxw")

@bot.message_handler(commands=["start"])
def hello(mess):
    first_name = mess.from_user.first_name or ""
    last_name = mess.from_user.last_name or ""
    bot.send_message(mess.chat.id, f"Привет {first_name} {last_name}я Сора, бот созданный господином Сергеем, вы можете запросить список команд(/команды)")

@bot.message_handler()




@bot.message_handler()
def list_command(mess):
    if mess.text.lower() == "/команды":
        bot.send_message(mess.chat.id, "команды бота:\n/фото\n/видео\n/команды")

bot.polling(none_stop=True)