from config import TELEGRAM_TOKEN, CHAT_ID
import requests as rq
import TELEGRAM_TOKEN

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send(t):
    bot.sendMessage(CHAT_ID, t, parse_model=telegram.ParseMode.HTML)