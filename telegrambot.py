import requests
from datetime import datetime
import telebot
from auth_data import token
from telebot import types


bot = telebot.TeleBot(token)


def telegram_bot(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = types.InlineKeyboardMarkup(row_width=2)
        item_bitcoin = types.InlineKeyboardButton('Ethereum', callback_data='item_1') 
        item_ethereum = types.InlineKeyboardButton('Bitcoin', callback_data='item_2') 
        item_dogecoin = types.InlineKeyboardButton('Dogecoin', callback_data='item_3') 
        item_usdt = types.InlineKeyboardButton('USDT', callback_data='item_4')
        markup.add(item_bitcoin, item_ethereum, item_dogecoin, item_usdt)

        bot.send_message(message.chat.id, "Hello! Choose a cryptocurrency to find out its current price:", reply_markup=markup)
        

    @bot.callback_query_handler(func=lambda call:True)
    def send_text(call):
        if call.message:
            if call.data == 'item_1':
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                    response = req.json()
                    sell_price = response['eth_usd']['sell']
                    bot.send_message(call.message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Ethereum price: {sell_price}')
                except Exception as ex:
                    print(ex)
                    bot.send_message(call.message.chat.id, "Something was wrong...")

        if call.message:
            if call.data == 'item_2':
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                    response = req.json()
                    sell_price = response['btc_usd']['sell']
                    bot.send_message(call.message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Bitcoin price: {sell_price}')
                except Exception as ex:
                    print(ex)
                    bot.send_message(call.message.chat.id, "Something was wrong...")

        if call.message:
            if call.data == 'item_3':
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
                    response = req.json()
                    sell_price = response['doge_usd']['sell']
                    bot.send_message(call.message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell Dogecoin price: {sell_price}')
                except Exception as ex:
                    print(ex)
                    bot.send_message(call.message.chat.id, "Something was wrong...")

        if call.message:
            if call.data == 'item_4':
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/usdt_usd")
                    response = req.json()
                    sell_price = response['usdt_usd']['sell']
                    bot.send_message(call.message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell USDT price: {sell_price}')
                except Exception as ex:
                    print(ex)
                    bot.send_message(call.message.chat.id, "Something was wrong...")
        else:
            pass

    bot.polling()
    
    
if __name__ == '__main__':
    telegram_bot(token)
