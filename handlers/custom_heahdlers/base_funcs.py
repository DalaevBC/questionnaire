# from keyboards.inline.all_markup import first_markup
from loader import bot
from aldar_bot.keyboards.inline.all_markup \
    import first_markup, second_markup
from loguru import logger


@bot.message_handler(commands=['start', 'go', 'Начать'])
@logger.catch
def start(message):

    bot.send_message(
        message.from_user.id,
        'Выплата доступна тем, у кого нет и ранее не было карт Альфа-банка.\n'
        'Есть ли у тебя карта Альфы?',
        reply_markup=first_markup())


@bot.callback_query_handler(func=lambda call: call.data.endswith('_first'))
@logger.catch
def get_first(call):
    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'нет_first':
        bot.send_message(
            call.from_user.id,
            'Супер 🔥\nТы старше 18 лет?',
            reply_markup=second_markup())
    else:
        bot.send_message(
            call.from_user.id,
            'Жаль, но ты можешь [отправить ссылку](https://alfa.me/TxE5Kw) друзьям\n',
            disable_web_page_preview=True,
            parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.endswith('_second'))
@logger.catch
def get_second(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'да_second':
        text = 'Отлично💥\n\n' \
               'Как получить 500 рублей:\n' \
               '● оформить заявку на карту [по специальной ссылке](https://alfa.me/TxE5Kw) до 30.10.22;\n' \
               '● получить карту (есть доставка)\n' \
               '● сделать любую покупку (от 10 рублей) до 30.10.22\n' \
               '● банк начислит 500 рублей на *твою бесплатную дебетовую карту*.\n'
        bot.send_message(call.from_user.id, text, disable_web_page_preview=True, parse_mode='Markdown')
        bot.send_message(5590570986, 'Oдин!')
    else:
        bot.send_message(
            call.from_user.id,
            'Жаль, но ты можешь [отправить ссылку](https://alfa.me/TxE5Kw) друзьям, старше 18 лет\n',
            disable_web_page_preview=True,
            parse_mode='Markdown'
        )
