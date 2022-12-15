from program import client, filters

bot = client(
         "My fist self code",
      api_id = 15855531,
      api_hash = "31e0b87de4285ebff259e003f58bf469",
      bot_token = "5809892449:AAFE_GhVSKIcTbdya4WIg0qs9AXk5cUlZB4"
)

@bot.on.message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send.message(message.chat.id, "Welcome to fucking bot")

bot.run()
