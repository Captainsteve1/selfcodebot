from pyrogram import Client, filters
import config 
import os
import sys
from telegram.ext import Filters, MessageHandler
import asyncio
from os import path as os_path
from subprocess import run as srun

Tbot = Client(name="Myacc", api_id=config.Api_id, api_hash=config.Api_hash, bot_token=config.Bot_Token)

print("Please wait setting up your vars to start your bot")

@Tbot.on_message(filters.command('start') & filters.private)
def welcome(client, message):
    message.reply_text(text="Hello! welcome to Test bot join @tmirrorleech")

print("Owner found @tony9848")
print("Bot started.. go & check your bot")

@Tbots.on.message(filters.command('shell') & filters.private)
def shell(update, context):
    message = update.effective_message
    cmd = message.text
    process = srun(cmd, capture_output=True, shell=True)
    reply = ''
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')
    if len(stdout) != 0:
        reply += f"<b>Stdout</b>\n<code>{stdout}</code>\n"
    if len(stderr) != 0:
        reply += f"<b>Stderr</b>\n<code>{stderr}</code>\n"
    if len(reply) > 3000:
        with open('output.txt', 'w') as file:
            file.write(reply)
        with open('output.txt', 'rb') as doc:
            context.bot.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id)
    elif len(reply) != 0:
        sendMessage(reply, context.bot, update.message)
    else:
        sendMessage('Executed', context.bot, update.message)

Tbot.run()
