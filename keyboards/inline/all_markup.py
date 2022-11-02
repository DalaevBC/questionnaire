from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def first_markup() -> InlineKeyboardMarkup:
    """
    Функция возвращает кнопки Да и Нет
    :return: Кнопки 'Да' 'Нет'
    """
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Да', callback_data='да_first'))
    markup.add(InlineKeyboardButton(text='Нет', callback_data='нет_first'))
    return markup


def second_markup() -> InlineKeyboardMarkup:
    """
    Функция возвращает кнопки Да и Нет
    :return: Кнопки 'Да' 'Нет'
    """
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Да', callback_data='да_second'))
    markup.add(InlineKeyboardButton(text='Нет', callback_data='нет_second'))
    return markup
