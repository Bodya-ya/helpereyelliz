import telebot
from pyexpat import native_encoding
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from os import getenv
load_dotenv()
token = getenv("BOT_TOKEN")
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message: Message):
    user_id = message.from_user.id
    name = message.from_user.username
    keyboard = [
        [InlineKeyboardButton("TELEGRAM🔵⚪", url = "t.me/eyelliz")],
        [InlineKeyboardButton("NIGHT YIN-YANG⚫⚪", url="t.me/nightyinyang")],
        [InlineKeyboardButton("MOV CS FROM EYELLIZ🏃", url="t.me/eyellizcs")],
        [InlineKeyboardButton("VK🔵", url="vk.com/eyelliz")],
        [InlineKeyboardButton("TWITCH🟣", url="twitch.tv/eyelliz")],
        [InlineKeyboardButton("FACEIT🟠", url="faceit.com/ru/players/-Eyelliz")],
        [InlineKeyboardButton("OSU!🐙", url="osu.ppy.sh/users/eyelliz")],
        [InlineKeyboardButton("STEAM🔵🎮", url="steamcommunity.com/id/eyelliz")],
        [InlineKeyboardButton("DISCORD🔵🎧", url="discord.com/users/505083687461978122")],
        [InlineKeyboardButton("TIKTOK⚫🔴", url="tiktok.com/@eyelliz")],
        [InlineKeyboardButton("YANDEX.MUSIC🟡⚫", url="music.yandex.ru/playlists/lk.185230fb-95c7-4ec7-8c63-d7cee3ccbe6e?utm_source=desktop&utm_medium=copy_link")],
   ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=911334605,
        text= f"📨 Новое обращение к боту\n"
            f"👤 Имя: {message.from_user.first_name}\n"
            f"🆔 ID: {message.from_user.id}\n"
            f"📧 Юзернейм: @{message.from_user.username}"
    )
    # keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add("TELEGRAM🔵⚪", url = "t.me/eyelliz")
    # keyboard.add("NIGHT YIN-YANG⚫⚪")
    # keyboard.add("MOV CS FROM EYELLIZ🏃")
    # keyboard.add("VK🔵")
    # keyboard.add("TWITCH🟣")
    # keyboard.add("FACEIT🟠")
    # keyboard.add("OSU!🐙")
    # keyboard.add("STEAM🔵🎮")
    # keyboard.add("DISCORD🔵🎧")
    # keyboard.add("TIKTOK⚫🔴")
    # keyboard.add("YANDEX.MUSIC🟡⚫")


    if name == "eyelliz":
        bot.send_message(
            chat_id=message.chat.id,
            text=f"стой... ты {message.from_user.username}?  я тоже eyelliz.",
            reply_markup=reply_markup,
        )
    elif user_id == 2104659191:
        bot.send_message(
            chat_id=message.chat.id and 911334605,
            text=f"Максимушка, че интересно стало?",
            reply_markup=reply_markup,

        )
    elif user_id == 5216678714:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Мишанчик, ты просто ёбырь, знай...",
            reply_markup=reply_markup,

        )
    elif user_id == 1048299984:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Ильюш,лечиться пора:) < 3 ",
            reply_markup=reply_markup,

        )
    elif user_id == 7515702184:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Прилетай быстрее, заебал < 3",
            reply_markup=reply_markup,

        )
    elif user_id == 1804897355:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Алина, добро пожаловать в колени)",
            reply_markup=reply_markup,

        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"хелло {message.from_user.username}, я eyelliz.\n"
            "В общем-то это все мои аккаунты в разных соц.сетях,играх.\n"
            "Кому интересно и нужно, пользуйтесь:)\n"
            "Бот'а лично писал:)\n"
            "(ну мне надо похвастаться)",
            reply_markup = reply_markup,
    )

@bot.message_handler(func=lambda message: True)
def forward_all_messages(message):
        bot.forward_message(911334605, message.chat.id, message.message_id)
        user_info = (
            f"📨 Новое сообщение\n"
            f"👤 Имя: {message.from_user.first_name}\n"
            f"🆔 ID: {message.from_user.id}\n"
            f"📧 Юзернейм: @{message.from_user.username}"
        )

        bot.send_message(911334605, user_info)



if __name__ == "__main__":
    while True:
        try:
            bot.polling()
        except Exception as ex:
            pass




