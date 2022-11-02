from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    text = '[Правила программы](https://alfabank.st/site-upload/bd/28/878/rules-friend-cc.pdf)'
    bot.reply_to(message, text, disable_web_page_preview=True, parse_mode='Markdown')

