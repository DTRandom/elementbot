import botogram
from ..objects.user import User

def process_start_command(chat, message, bot):
    u = User(message.sender)
    u.state("home")
    btns = botogram.Buttons()
    btns[0].callback("👉🏻 Chi siamo? 👈🏻", 'who')
    btns[1].callback("💁🏻‍♂️ Reclutamenti 🙋🏻‍♂️", 'recruit')
    btns[1].callback("👨🏻‍✈️ Staff Telegram 👩🏻‍✈️", 'staff')
    btns[2].callback("👥 Contattaci", 'contact')
    text = "Questo bot ti aiuterà a conoscere la nostra <b>multigaming</b>."
    chat.send(text, syntax = 'HTML', attach = btns)

def process_who_callback(chat, message, query, bot):
    u = User(query.sender)
    u.state("who")
    btns = botogram.Buttons()
    btns[0].callback("⬅️ Torna Indietro", 'home')
    text = "\nElement Gaming è un nuovo <b>progetto italiano</b> in continua evoluzione dedicato al <b>netgaming competitivo</b>, creato <b>dai players per i players</b>.\nLe nostre sezioni sono composte da <b>teams paralleli</b> che si allenano tra loro per gareggiare nei circuiti <b>nazionali</b> e <b>internazionli</b> dei relativi giochi. Supportiamo giochi di vario genere, dagli <b>MMO</b> agli <b>FPS</b> passando per i <b>MOBA</b> e gli <b>RTS</b>.\nL’obiettivo è quello di dare un importante contributo allo sviluppo del panorama videoludico italiano.\nElement Gaming nasce nel Maggio del 2014 e il suo successo iniziale si è basato su una nuova concezione di <b>Multigaming</b>, che sposa il lato puramente agonistico/competitivo con quello social/goliardico, tipico delle Community.\nElement infatti supporta anche giochi non tipicamente “competitivi”, quali gli <b>MMORPG</b> e i <b>Survival</b>, permettendo ad ogni giocatore di trovare un gruppo stabile all’interno di ogni gioco, tra quelli più famosi al mondo.\nInoltre permette ai nuovi giocatori di apprendere le basi del gaming online, tramite <b>allenamenti di gruppo</b>, <b>coaching</b>, <b>creazione di guide</b> e <b>tutorials</b>, indirizzandoli infine verso la scena competitiva.\nDopo quasi 3 anni di attività, il progetto è cresciuto esponenzialmente e ora conta <b>migliaia di iscritti</b>, diventando nel 2015 un’Associazione Sportiva Dilenttantistica che prevede un tesseramento.\nE’ importante sapere che il tesseramento ad Element Gaming è <b>facoltativo</b>. Questo per sottolineare la filosofia di base di Element, che è quella di un progetto <b>senza scopo di lucro</b>.\nNonostante la giovane età del progetto, gli importanti risultati ottenuti all’interno dei circuiti competitivi di giochi quali <b>LOL</b>, <b>Hearthstone</b>, <b>CSGO</b>, <b>Starcraft</b>, ecc.. annoverano Element tra le multigaming <b>più vincenti in assoluto nella storia del gaming italiano</b>."
    chat.send_photo("data/img/foto1.jpg")
    chat.send_photo("data/img/foto2.jpg")
    chat.send(text, syntax = 'HTML', attach = btns)

def process_home_callback(chat, message, query, bot):
    u = User(query.sender)
    u.state("home")
    btns = botogram.Buttons()
    btns[0].callback("👉🏻 Chi siamo? 👈🏻", 'who')
    btns[1].callback("💁🏻‍♂️ Reclutamenti 🙋🏻‍♂️", 'recruit')
    btns[1].callback("👨🏻‍✈️ Staff Telegram 👩🏻‍✈️", 'staff')
    btns[2].callback("👥 Contattaci", 'contact')
    text = "Questo bot ti aiuterà a conoscere la nostra <b>multigaming</b>."
    message.edit(text, syntax = 'HTML', attach = btns)

def process_recruit_callback(chat, message, query, bot):
    u = User(query.sender)
    u.state("recruit")
    btns = botogram.Buttons()
    btns[0].url("League of Legends", "https://docs.google.com/forms/d/e/1FAIpQLSeKnPvJ-T3Z14UL7aSYpxRkAZBGrFUcx0qulRRoTi8THq3nTQ/viewform")
    btns[0].url("Overwatch", "http://goo.gl/QwpX9F")
    btns[1].url("CS: GO", "https://goo.gl/bfYEQ9")
    btns[1].url("HearthStone", "https://goo.gl/ExvArx")
    btns[2].url("Starcraft 2", "http://bit.ly/1ULt6jj")
    btns[2].url("GWENT", "https://www.facebook.com/groups/648502678681252/?fref=ts")
    btns[3].url("Rainbow Six Siege", "https://docs.google.com/forms/d/e/1FAIpQLSc9Pn6SsXswH9p5KJfCPTFplm0twLV2qr_q9nPpbaf2706wCA/viewform")
    btns[3].url("Call of Duty", "https://www.facebook.com/EMTCoD/?fref=ts")
    btns[4].url("Playersunknown’s Battlegrounds", "https://www.facebook.com/groups/1899485960310557/?fref=ts")
    btns[4].url("DayZ", "http://fireclan.it/")
    btns[5].url("FIFA", "https://www.facebook.com/groups/1849893668555507/?fref=ts")
    btns[5].url("ArhceAge", "https://goo.gl/WivTDo")
    btns[6].url("Elder Scrolls Online", "https://goo.gl/wehE5t")
    btns[6].url("FFXIV", "https://goo.gl/JP8CVg")
    btns[7].url("LoTR Online", "https://goo.gl/aZk29I")
    btns[7].url("Tera", "https://goo.gl/ytbxmW")
    btns[8].url("Clash Royale", "https://www.facebook.com/groups/240952299581555/?fref=ts")
    btns[8].url("Critical Ops", "https://www.facebook.com/groups/272289599896469/?fref=ts")
    btns[9].url("VainGlory", "https://www.facebook.com/groups/927061917390486/?fref=ts")
    btns[9].url("Splatoon", "https://goo.gl/euM5rG")
    btns[10].callback("⬅️ Torna Indietro", 'home')
    text = "Sei un player e vuoi entrare nel mondo ElementGaming?\nScegli il tuo gioco qui sotto:"
    chat.send_photo("data/img/foto3.jpg")
    chat.send(text, attach = btns)

def process_staff_callback(chat, message, query, bot):
    u = User(query.sender)
    u.state("staff")
    btns = botogram.Buttons()
    btns[0].callback("⬅️ Torna Indietro", 'home')
    text = "Ecco la lista dello staff di Element-Gaming per il gruppo Telegram:\n\n🔱 <b>FOUNDER</b>\n- @LordZargum\n\n⚜️<b>ADMIN</b>\n- @Gildarts777\n- @Diego757\n- @DoggoPoliziotto\n- @XY_Jackal\n\n🚸 <b>MODERATORI</b>\n- @MiphnaZora\n- @Rod_K\n- @DrG95\n\nCi teniamo a precisare che lo staff riguarda solo il gruppo Telegram @ElementGaming. La multigaming ha uno staff molto più ampio che racchiude <b>più di 100 persone</b> tra admin e mod.\nSe vuoi fare parte dello staff del gruppo telegram ed iniziare una carriera come moderatore, al momento dovrai parlare con @LordZargum. Presto verrà implementata la funzione tramite il questo bot."
    chat.send_photo("data/img/foto4.jpg")
    chat.send(text, syntax = 'HTML', attach = btns)

def process_contact_callback(chat, message, query, bot):
    u = User(query.sender)
    u.state("contact")
    btns = botogram.Buttons()
    btns[0].callback("⬅️ Torna Indietro", 'home')
    text = "Scrivi un messaggio a questo bot, gli admin ti risponderanno il prima possibile."
    message.edit(text, attach = btns)
