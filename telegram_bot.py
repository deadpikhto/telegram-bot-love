import random
import requests
import schedule
import time

# Токен вашего бота и Chat ID девушки
BOT_TOKEN = "7664740886:AAE2urRo9clBge4ipEnM-4CehHFz4AZi3ec"  # Токен, полученный от BotFather
CHAT_ID = "258005348"  # Замените на Chat ID вашей девушки

# Расширенный список сообщений
love_messages = [
    "Привет, лапуля! ☀️ Просто хочу сказать, что ты особенная! 💖.",
    "Каждый день с тобой — как маленький праздник 🎉. Люблю тебя!",
    "Ты моя радость ❤️. Спасибо, что ты есть!",
    "Знаешь, что делает меня счастливым? Твоя улыбка 😊.",
    "Скучаю по тебе Катенька!",
    "Сегодня отличный день, чтобы напомнить: ты самая лучшая 🌟!",
    "Надеюсь, Альбертовна помнит, какая ты крутая! 😍.",
    "Ты моё счастье, и я не устаю это повторять 💕.",
    "Люблю тебя, Екатерина, кровь моей крови!",
    "Ты - луна моей жизни, Катьенька! 🌕❤️",
    "Ты простро прелесть, Катенька. Спасибо, что ты есть 💖."
]

# Функция для отправки сообщения
def send_love_message():
    message = random.choice(love_messages)  # Выбираем случайное сообщение
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"Сообщение отправлено: {message}")
    else:
        print("Ошибка при отправке сообщения:", response.text)

# Настройка расписания: отправка сообщения каждые 4 часа
schedule.every(4).hours.do(send_love_message)

# Основной цикл программы
if __name__ == "__main__":
    print("Бот запущен и ждёт отправки сообщений...")
    send_love_message()  # Отправляем первое сообщение сразу
    while True:
        schedule.run_pending()  # Проверяем расписание
        time.sleep(1)  # Проверка каждую секунду