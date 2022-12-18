from pyrogram import Client, filters
import config 

Tbot = Client("Myacc", Api_id=config.Api_id, Api_hash=config.Api_hash, Bot_Token=config.Bot_Token)

print("Please wait setting up your vars to start your bot")

@Tbot.on.message(filters.command('start') & filters.private)
def welcome(client, message):
    message.reply_text(text="Hello {user} welcome to Test bot join @tmirrorleech")
    
Tbot.run() # to start running bot!   
print("Bot started.. go & chk")
