from telegram.ext import *

Token = "5809892449:AAFE_GhVSKIcTbdya4WIg0qs9AXk5cUlZB4"

print("Starting up your bot my Tony...")

def start(update, context):
    update.message.reply_text ('Hello {user} welcome to my bot') 
   
