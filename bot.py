from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')

def start(update: Update, context: CallbackContext):
    update.message.reply_text('🎯 ربات سیگنال فعال شد! دستورات: /price /signal')

def price(update: Update, context: CallbackContext):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url).json()
        btc_price = response['bitcoin']['usd']
        update.message.reply_text(f'💰 بیت‌کوین: ${btc_price:,}')
    except:
        update.message.reply_text('❌ خطا در دریافت قیمت')

def signal(update: Update, context: CallbackContext):
    signal_text = "📈 سیگنال تستی: BTC/USDT - خرید - ورود: 45,000-46,000"
    update.message.reply_text(signal_text)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("price", price))
updater.dispatcher.add_handler(CommandHandler("signal", signal))

print("✅ ربات فعال شد...")
updater.start_polling()
updater.idle()
