from pyrogram import Client, filters
import config 

Tbot = Client(name="Myacc", api_id=config.Api_id, api_hash=config.Api_hash, bot_token=config.Bot_Token)

print("Please wait setting up your vars to start your bot")

@Tbot.on_message(filters.command('start') & filters.private)
def welcome(client, message):
    message.reply_text(text="Hello {message.from.user.mention} welcome to Test bot join @tmirrorleech")

print("Owner found @tony9848")
print("Bot started.. go & check your bot")
    
Tbot.run() # to start running bot!  
