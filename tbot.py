from telegram.ext import *
import python 

Token = "5809892449:AAFE_GhVSKIcTbdya4WIg0qs9AXk5cUlZB4"

print("Starting up your bot my Tony...")

def start_command(update, context):
    update.message.reply_text ('Hello {user} welcome to my bot') 
   
def handle_response (text: str) -> str:
    if hello In text

    return 'hello my friend '

    dp.add.handler(commandHandler('start', start_command))
