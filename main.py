from telegram.ext import *
import response 
import logging

BOT_TOKEN = "5809892449:AAFE_GhVSKIcTbdya4WIg0qs9AXk5cUlZB4"

def start_command(update, context):
    update.message.reply_text("Hello {update.message.chat.id} welcome to my bot'!")


def help_command(update, context):
    update.message.reply_text("Help commands {update.message.chat.id} welcome to my bot'!")


def handle_message(update, context):
    text = str(update.message.reply).lower()
    logging.info(f'user {update.message.chat.id} says: {text}')

   #bot response to user
    response = responses.get_response(text)
    update.message.reply_text(response)


if __name__ == '__main__':
   updater = Updater(BOT_TOKEN, use_context=True)
   dp = updater.dispatcher

#comds

  dp.add_handler(CommandHandler('start', start_command))
  dp.add_handler(CommandHandler('help', help_command))

#msg
  dp.add_handler(MessageHandler(filters.txt, handle_message))

#run bot
  updater.start_polling(2.0)
  updater.idle()
