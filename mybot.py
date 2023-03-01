import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("6132194785:AAF8xUccimMC2A-IO6ia7Gu4NRiu8vNKo0g")
CHAT_ID = os.getenv("-1001669793604")

bot = telebot.TeleBot(TOKEN)

def salvarTipEnviada(cor, padrao, msg):
    with open('tips_enviadas.csv', 'a') as f:
        f.write(f'{cor}, {padrao}, {msg.message_id}\n')
    pass

def enviarGale(martingale):
    bot.send_message(CHAT_ID, text=f'Atenção gale: {martingale}')
        
def enviarWinLoss(Result):
    if Result:
        bot.send_message(CHAT_ID, text='GREEN')
    else:
        bot.send_message(CHAT_ID, text='LOSS')
        
def enviarSinalTelegram(cor, padrao, mensagem):
    chat = bot.send_message(CHAT_ID, text=mensagem, parse_mode="HTML")
    salvarTipEnviada(cor, padrao, chat)
    pass
