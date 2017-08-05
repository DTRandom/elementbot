import botogram
import time
import botogram.objects.base

import config
from src.objects.user import User
from src.updates import commands

bot = botogram.create(config.BOT_TOKEN)

@bot.command("start")
def start_command(chat, message):
    if chat.type != "private":
        m = chat.send("<i>Non utilizzarmi in chat di gruppo, usami in privata</i>")
        c = chat.id
        time.sleep(5)
        m.delete()
        message.delete()
    else:
        commands.process_start_command(chat, message, bot)

@bot.callback("home")
def home_callback(chat, message, query):
    if chat.type != "private":
        return
    else:
        commands.process_home_callback(chat, message, query, bot)

@bot.callback("who")
def who_callback(chat, message, query):
    if chat.type != "private":
        return
    else:
        commands.process_who_callback(chat, message, query, bot)

@bot.callback("recruit")
def recuit_callback(chat, message, query):
    if chat.type != "private":
        return
    else:
        commands.process_recruit_callback(chat, message, query, bot)

@bot.callback("staff")
def staff_callback(chat, message, query):
    if chat.type != "private":
        return
    else:
        commands.process_staff_callback(chat, message, query, bot)

@bot.callback('contact')
def contact_callback(chat, message, query):
    if chat.type != "private":
        return
    else:
        commands.process_contact_callback(chat, message, query, bot)

@bot.process_message
def message_recieved(chat, message):
    if chat.type == "private":
        u = User(message.sender)
        state = u.state().decode('utf-8')
        if state != "contact":
            return
        else:
            if message.forward_from == None or message.forward_from.id == message.sender.id:
                bot.chat(config.ADMINS).send("⚠️ <b>NUOVA RICHIESTA IN ARRIVO</b> ⚠️", syntax = 'HTML')
                message.forward_to(config.ADMINS)
            else:
                chat.send("Per motivi di sicurezza non sono accettati messaggi inoltrati da altri.")
    else:
        if message.reply_to_message == None:
            return
        else:
            replyed_message = message.reply_to_message
            if replyed_message.forward_from == None:
                return
            else:
                bot.chat(config.ADMINS).send("✅ Risposta inviata")
                bot.chat(replyed_message.forward_from.id).send("<b>Admin: </b>" + message.text, syntax = 'HTML')
