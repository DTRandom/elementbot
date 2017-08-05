import botogram
import config
bot = botogram.create(config.BOT_TOKEN)
@bot.process_message
def message_sent(chat, message):
    m = chat.send("Prova")
    f = m.sender.id
    chat.send(str(f))

bot.run()
