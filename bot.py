# -*- coding: utf-8 -*-
import telebot
from command_handler import CommandHandler
from users_repository import UsersRepository
from states import State
from users_repository import UserInfo
from requests.exceptions import ReadTimeout
import time
import os
import requests
from bs4 import BeautifulSoup
API_TOKEN = '1391169462:AAG3l2DwCxs1Cys4kqh3L2cG32Od7ryb1ZY'

bot = telebot.TeleBot(API_TOKEN)
users = UsersRepository("users")

handler = CommandHandler(bot, users)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, "Привет. Напиши запрос чтобы узнать курс валют на сегодня. Пример : Курс доллара в Москве")
    if not users.exists(user_id):
        user_info = UserInfo(user_id, state=State.MAIN)
        users.save(user_info)
        #handler.keyboard_in_tournaments(message)
    #else:
        #handler.keyboard_in_tournaments(message)
    file = open(str(user_id), "w")
    file.close()

'''
@bot.message_handler(commands=['call'])
def call(message):
        if ((str(message.from_user.id) == '442152076') or ((str(message.from_user.id) == '284137184'))):
            handler.make_advert(message)
        else:
            bot.send_message(message.chat.id, "У вас нет прав!")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    if ((str(message.from_user.id) == '442152076') or ((str(message.from_user.id) == '284137184'))):
        if message.caption == '1':
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '1.jpg')
            os.remove(path)
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = '1.jpg'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "Фото добавлено")
            handler.kek1(src)
        elif message.caption == '2':
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '2.jpg')
            os.remove(path)
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = "2.jpg"
            with open("2.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "Фото добавлено")
            handler.kek2(src)
        elif message.caption == '3':
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '3.jpg')
            os.remove(path)
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = "3.jpg"
            bot.reply_to(message, "Фото добавлено")
            with open("3.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            handler.kek3(src)
    else:
        bot.send_message(message.chat.id, 'У Вас нет прав!')
'''
@bot.message_handler(content_types=["sticker"])
def sends_sticker(message):
    bot.send_message(message.chat.id, "Четкий стикер. Лучше узнай на сколько сегодня упал рубль.")

@bot.message_handler(content_types=['text'])
def sends(message):
    '''
    if (message.text == '📜 Расписание уроков'):
        handler.start1(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '⏰ Расписание звонков'):
        handler.start2(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '🍛 Меню в столовой'):
        handler.start3(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '📝 График дежурств'):
        handler.start4(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '☎ Контакты'):
        bot.send_message(message.chat.id, 'Адрес:\n'
                                          'Город Павлодар, ул. Ленина д.12\n'
                                          'Телефон:\n'
                                          '53-47-14\n'
                                          'Email:\n'
                                          'lizey8@mail.ru\n')
        handler.keyboard_in_tournaments(message)
    '''
    flag2 = False
    if (message.text != "" or message):
        a = message.text
        a = a.lower()
        ans = ""
        URL = 'https://mainfin.ru/currency/'
        if (a.find("доллар") != -1 or a.find("usd") != -1):
            URL = URL + 'usd/'
            ans = "Курс доллара в "
        elif (a.find("евро") != -1 or a.find("eur") != -1):
            URL = URL + 'eur/'
            ans = "Курс евро в "
        elif (a.find("юан") != -1 or a.find("cny") != -1):
            URL = URL + 'cny/'
            ans = "Курс юаня в "
        elif (a.find("фунт") != -1 or a.find("gbp") != -1):
            URL = URL + 'gbp/'
            ans = "Курс фунта в "
        elif (a.find("йен") != -1 or a.find("jpy") != -1):
            URL = URL + 'jpy/'
            ans = "Курс йены в "
        else:
            bot.send_message(message.chat.id, "Не понял запрос")
            flag2 = True
        if (a.find("петербург") != -1 or a.find("питер") != -1 or a.find("спб") != -1):
            URL = URL + 'sankt-peterburg'
            ans = ans + "Санкт-Петербурге"
        elif (a.find("москв") != -1 or a.find("мск") != -1):
            URL = URL + 'moskva'
            ans = ans + "Москве"
        elif (a.find("ростов") != -1):
            URL = URL + 'rostov-na-donu'
            ans = ans + "Ростове-на-Дону"
        elif (a.find("екатеринбург") != -1):
            URL = URL + 'ekaterinburg'
            ans = ans + "Екатеринбурге"
        elif (a.find("казан") != -1):
            URL = URL + 'kazan'
            ans = ans + "Казани"
        elif ((a.find("нижн") != -1 and a.find("новгород") != -1)):
            URL = URL + 'nizhniy-novgorod'
            ans = ans + "Нижнем Новгороде"
        elif (a.find("новосиб") != -1):
            URL = URL + 'novosibirsk'
            ans = ans + "Новосибирске"
        elif (a.find("омск") != -1):
            URL = URL + 'omsk'
            ans = ans + "Омске"
        elif (a.find("самар") != -1):
            URL = URL + 'samara'
            ans = ans + "Самаре"
        elif (a.find("челябинск") != -1):
            URL = URL + 'chelyabinsk'
            ans = ans + "Челябинске"
        elif (a.find("уф") != -1):
            URL = URL + 'ufa'
            ans = ans + "Уфе"
        elif (a.find("красноярск") != -1):
            URL = URL + 'krasnoyarsk'
            ans = ans + "Красноярске"
        elif (a.find("перм") != -1):
            URL = URL + 'perm'
            ans = ans + "Перми"
        elif (a.find("воронеж") != -1):
            URL = URL + 'voronezh'
            ans = ans + "Воронеже"
        elif (a.find("Волгоград") != -1):
            URL = URL + 'volgograd'
            ans = ans + "Волгограде"
        elif (a.find("краснодар") != -1):
            URL = URL + 'krasnodar'
            ans = ans + "Краснодаре"
        elif (a.find("саратов") != -1):
            URL = URL + 'saratov'
            ans = ans + "Саратове"
        elif (a.find("тюмен") != -1):
            URL = URL + 'tumen'
            ans = ans + "Тюмени"
        elif (a.find("тольят") != -1):
            URL = URL + 'tolyatti'
            ans = ans + "Тольятти"
        elif (a.find("ижевск") != -1):
            URL = URL + 'izhevsk'
            ans = ans + "Ижевске"
        elif (a.find("барнаул") != -1):
            URL = URL + 'barnaul'
            ans = ans + "Барнауле"
        elif (a.find("иркутск") != -1):
            URL = URL + 'irkutsk'
            ans = ans + "Иркутске"
        elif (a.find("ульяновск") != -1):
            URL = URL + 'ulyanovsk'
            ans = ans + "Ульяновске"
        elif (a.find("хабаровск") != -1):
            URL = URL + 'habarovsk'
            ans = ans + "Хабаровске"
        elif (a.find("ярославл") != -1):
            URL = URL + 'yaroslavl'
            ans = ans + "Ярославле"
        elif (a.find("владивосток") != -1):
            URL = URL + 'vladivostok'
            ans = ans + "Владивостоке"
        elif (a.find("махачкал") != -1):
            URL = URL + 'mahachkala'
            ans = ans + "Махачкале"
        elif (a.find("томск") != -1):
            URL = URL + 'tomsk'
            ans = ans + "Томске"
        elif (a.find("оренбург") != -1):
            URL = URL + 'orenburg'
            ans = ans + "Оренбурге"
        elif (a.find("кемерово") != -1):
            URL = URL + 'kemerovo'
            ans = ans + "Кемерово"
        elif (a.find("новокузнецк") != -1):
            URL = URL + 'novokuzneck'
            ans = ans + "Новокузнецке"
        else:
            ans = ans + "России"
        HEADERS = {
            'user_agent': 'head'
        }
        if (flag2 == False):
            try:
                response = requests.get(URL, headers=HEADERS)
                response.encoding = 'utf8'
                soup = BeautifulSoup(response.text, 'html.parser')
                file = open(str(message.from_user.id) + '.txt', "w", encoding="utf-8")
                file.write("🌍" + ans + '\n' + '\n')
                for i in range(5):
                    for tag in soup.find_all('a', {"class": "currpos-{0}".format(i)}):
                        file.write("🏛" + "{0}".format(tag.text) + '\n')
                    d = soup.find('tr', {"data-key": "{0}".format(i)})
                    flag = True
                    for tag in d.findAllNext('span', {"class": "float-convert__btn"}, limit=2):
                        if (flag):
                            file.write("Покупка - {0} руб.".format(tag.text) + '\n')
                            flag = False
                        else:
                            file.write("Продажа - {0} руб.".format(tag.text) + '\n' + '\n')
                file.close()
                file = open(str(message.from_user.id) + '.txt', "r", encoding="utf-8")
                file2 = file.read()
                bot.send_message(message.from_user.id, file2)
                file.close()
            except:
                file = open(str(message.from_user.id) + '.txt', "r", encoding="utf-8")
                file2 = file.read()
                bot.send_message(message.from_user.id, file2)
                file.close()
                return False

while True:

    try:

        bot.polling(none_stop=True)

    except ReadTimeout:
        time.sleep(15)

    except ConnectionError:
        time.sleep(15)

    #except ReadTimeoutError:
    #    time.sleep(15)

