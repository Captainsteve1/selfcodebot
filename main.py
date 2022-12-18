from pyrogram import Client, filters
import config 

Tbot = Client(name="Myacc", api_id=config.Api_id, api_hash=config.Api_hash, bot_token=config.Bot_Token)

print("Please wait setting up your vars to start your bot")

@Tbot.on.message(filters.command('start') & filters.private)
def welcome(client, message):
    message.reply_text(text="Hello {user} welcome to Test bot join @tmirrorleech")
    
Tbot.run() # to start running bot!   
print("Bot started.. go & chk")
