from pyrogram import Client

api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"
bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
