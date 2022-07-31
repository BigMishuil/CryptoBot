import requests
from datetime import datetime
import telebot
from auth_data import token

bot = telebot.TeleBot(token)
def get_date():
    req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
    response = req.json()
    print(response)
    sell_price = response['eth_usd']['sell']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Ethereum price: {sell_price}')

def get_datebtc():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    print(response)
    sell_price = response['btc_usd']['sell']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Bitcoin price: {sell_price}')

def get_datedoge():
    req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
    response = req.json()
    print(response)
    sell_price = response['doge_usd']['sell']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Dogecoin price: {sell_price}')   

def get_dateusdt():
    req = requests.get("https://yobit.net/api/3/ticker/usdt_usd")
    response = req.json()
    print(response)
    sell_price = response['usdt_usd']['sell']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell USDT price: {sell_price}')   

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello!")
        bot.send_message(message.chat.id, 'Write "ethereum" in order to find out the current price of Ethereum')
        bot.send_message(message.chat.id, 'Write "bitcoin" in order to find out the current price of Bitcoin')
        bot.send_message(message.chat.id, 'Write "dogecoin" in order to find out the current price of Dogecoin')
        bot.send_message(message.chat.id, 'Write "usdt" in order to find out the current price of USDT')

    @bot.message_handler(content_types = ["text"])
    def send_text(message):
        if message.text.lower() == "ethereum":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                response = req.json()
                sell_price = response['eth_usd']['sell']
                bot.send_message(message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Ethereum price: {sell_price}')
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Something was wrong...")

        elif message.text.lower() == "bitcoin":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response['btc_usd']['sell']
                bot.send_message(message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Bitcoin price: {sell_price}')
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Something was wrong...")

        elif message.text.lower() == "dogecoin":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
                response = req.json()
                sell_price = response['doge_usd']['sell']
                bot.send_message(message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Dogecoin price: {sell_price}')
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Something was wrong...")

        elif message.text.lower() == "usdt":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/usdt_usd")
                response = req.json()
                sell_price = response['usdt_usd']['sell']
                bot.send_message(message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell USDT price: {sell_price}')
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Something was wrong...")
        else:
            bot.send_message(message.chat.id, "I don't quite understand you")

    bot.polling()
if __name__ == '__main__':
    #get_date()
    #get_datebtc()
    #get_datedoge()
    #get_dateusdt()
    telegram_bot(token)