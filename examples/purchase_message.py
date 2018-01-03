
import asyncio

from balebot.filters import *
from balebot.models.messages import *
from balebot.updater import Updater

# A token you give from BotFather when you create your bot set below
updater = Updater(token="114d273b48f04cd7c3be657328d2aa5521dae020",
                  loop=asyncio.get_event_loop())
dispatcher = updater.dispatcher


def success(result, user_data):
    print("success : ", result)
    print(user_data)


def failure(result, user_data):
    print("failure : ", result)
    print(user_data)


@dispatcher.message_handler(PhotoFilter())
def a_purchase_message(bot, update):
    message = update.get_effective_message()
    user_peer = update.get_effective_user()
    purchase_message = PurchaseMessage(msg=message, account_number=6037991822619544, amount=11100)
    bot.send_message(purchase_message, user_peer, success_callback=success, failure_callback=failure)
    bot.get_file_download_url(message.file_id, user_peer.peer_id, "photo", success_callback=success,
                              failure_callback=failure)


@dispatcher.error_handler()
def error_handler(bot, update, error):
    if update:
        print(update)
    print(error, "  :  handled by error_handler")


@dispatcher.default_handler()
def default_handler_func(bot, update):
    bot.respond(update, "default handler is replying.".format(), success_callback=success,
                failure_callback=failure)


