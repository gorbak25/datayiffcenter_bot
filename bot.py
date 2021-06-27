#!/usr/bin/env python3
import logging
import os
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

if "TOKEN" not in os.environ:
    print("Please add $TOKEN before starting the bot")
    exit(1)

token = os.environ["TOKEN"]
start_sticker = "CAACAgQAAxkBAAMIYNkAAdVOt_LKRDIUNRPaMsuJVNcRAAMDAAJ_MfoNuxVnQkpzCJAgBA"
boop_sticker = "CAACAgEAAxkBAAMSYNkB7pSsYj_3bDTKJ2SZGjm1tAsAAiJ4AAKvGWIHVKhKpnDOMyQgBA"
patpat_sticker = "CAACAgQAAxkBAAMYYNkCa0_-bZHncO7Quff5shgjJokAAkoDAAJ_MfoNXzNJdaEe5UkgBA"
long_stickers = [
    { 'top': "CAACAgEAAxkBAAMsYNkE-uybng03W-h-nPWXAmHWFEgAAi8AA75EPhFHNvLkSXoEBSAE",
      'middle': "CAACAgEAAxkBAAMrYNkE8_S2b_OeVbJaW1T0v8QqbEQAAi4AA75EPhGg0V8LYc3u_CAE",
      'bottom': "CAACAgEAAxkBAAMqYNkE5lm7Ew_qaWEGVOSVNP0-3c4AAi0AA75EPhEYYP2P0oN3jSAE",
    },
    { "top": "CAACAgEAAxkBAANoYNkHSNDGOyPKBb4YUrIHGPbRXikAAvQDAALt__sGGa8K6-l2IoEgBA",
      "middle": "CAACAgEAAxkBAANuYNkH49lovHmaWzOZ3VNonZi1q9oAAvUDAALt__sGPftu4g45na0gBA",
      "bottom": "CAACAgEAAxkBAANvYNkH43AVN5mkRj67phWMgJTHZ3wAAv0DAALt__sGhccHF1-rfi4gBA",
    },
    { "top": "CAACAgEAAxkBAANrYNkHnZcHuiO-jMDsNsAUkmRYq2cAAggEAALt__sG1liwIoQEzlMgBA",
      "middle": "CAACAgEAAxkBAANsYNkHnQ9VzlVYClSWEvxNWzRP43kAAgkEAALt__sG_2-PdFff-wsgBA",
      "bottom": "CAACAgEAAxkBAANtYNkHneKKTbB1UZV4kTVJ1p-EPTAAAgoEAALt__sGVRAzDi5VN1cgBA",
    },
    { "top": "CAACAgEAAxkBAANwYNkICY_GSlpUqWeS2bMx5qCvf2EAAoIRAAIj3RAGmpXg9fEISc4gBA",
      "middle": "CAACAgEAAxkBAANxYNkICThB_sVlN6v-oMBPVohLp54AAoMRAAIj3RAGmX6kpDZTdpogBA",
      "bottom": "CAACAgEAAxkBAANyYNkICbEwxKKgFoHsbV-ZnAu2t0sAAoQRAAIj3RAGSNoGEQ6Hb70gBA",
    },
]
little_angry_sticker = "CAACAgEAAxkBAAM-YNkGC-F_3gABv_39XoW3AAEDpx1cSAAC8IUAAq8ZYgfWaCrRtf2SBiAE"
angry_sticker = "CAACAgEAAxkBAAM1YNkFQarlMSVdw7iJe1iK0z0cArkAAu-FAAKvGWIHLhcDItnEJcsgBA"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def boop(update: Update, context: CallbackContext) -> None:
    update.message.reply_sticker(boop_sticker)

def patpat(update: Update, context: CallbackContext) -> None:
    update.message.reply_sticker(patpat_sticker)

def pad(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) != 1:
        update.message.reply_sticker(little_angry_sticker, quote=False)
        update.message.reply_text("/pad [int]")
        return
    n = None
    try:
        n = int(args[0], 10)
    except:
        update.message.reply_sticker(angry_sticker, quote=False)
        update.message.reply_text("I will bite you!")
        return

    if n < 1 or n > 16:
        update.message.reply_sticker(little_angry_sticker, quote=False)
        update.message.reply_text("n \in [1;16]")
        return

    res = random.choice(long_stickers)
    update.message.reply_sticker(res['top'], quote=False)
    for i in range(n):
        update.message.reply_sticker(res['middle'], quote=False)

    update.message.reply_sticker(res['bottom'], quote=False)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_sticker(start_sticker)
    update.message.reply_text("*raccoon noises")

def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('boop', boop))
    updater.dispatcher.add_handler(CommandHandler('patpat', patpat))
    updater.dispatcher.add_handler(CommandHandler('pad', pad))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
