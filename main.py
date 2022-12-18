from pyrogram import Client, filters
import config 
import os
import sys
import asyncio
from os import path as os_path

Tbot = Client(name="Myacc", api_id=config.Api_id, api_hash=config.Api_hash, bot_token=config.Bot_Token)

print("Please wait setting up your vars to start your bot")

@Tbot.on_message(filters.command('start') & filters.private)
def welcome(client, message):
    message.reply_text(text="Hello! welcome to Test bot join @tmirrorleech")

print("Owner found @tony9848")
print("Bot started.. go & check your bot")

@Tbots.on.message(filters.command('shell') & filters.private)
def tg_s_Handler(bot: Tbot, message: Message):
    cmd = message.text.split(' ', 1)
    sts = await message.reply_text("Please wait ....")
    if len(cmd) == 1:
        return await sts.edit('**Send a command to execute**')
    cmd = cmd[1]
    for check in cmd.split(" "):
        if check.upper().endswith(BLACKLISTED_EXTENSIONS):
            return await sts.edit("you can't execute this cmd")
    reply = ''
    stderr, stdout = await run_comman_d(cmd)
    newstdout = ""
    for line in stdout.split("\n"):
        if not line.upper().endswith(BLACKLISTED_EXTENSIONS):
            newstdout += line + "\n"
    if len(newstdout) != 0:
        reply += f"<b>Stdout</b>\n<code>{newstdout}</code>\n"
    if len(stderr) != 0:
        reply += f"<b>Stderr</b>\n<code>{stderr}</code>\n"
    if len(reply) > 3000:
        with open('output.txt', 'w') as file:
            file.write(reply)
        with open('output.txt', 'rb') as doc:
            await message.reply_document(
                document=doc,
                caption=f"`{cmd}`")
            await sts.delete()
    elif len(reply) != 0:
        await sts.edit(reply)
    else:
        await sts.edit('Executed')

Tbot.run() # to start running bot!  
