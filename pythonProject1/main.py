import telebot
from telebot import types
import json
import random
# import Functions as func

bot = telebot.TeleBot("6653300108:AAFhPJp_q2eu2iUTj-6c4p757X9k8jHNWpw")

print('--BotWorking--')

# --	-- Reserved_Functions -- 	--
# --	-- Reserved_Functions -- 	--

with open('Films.json', 'r', encoding='utf-8') as file_films:
	Films = json.load(file_films)
with open('Serials.json', 'r', encoding='utf-8') as file_serials:
	Serials = json.load(file_serials)

# --	-- Values -- 	--
# --	-- Values -- 	--
counters = {
    "menu_films": 0,
	"film_serial": 0,   # 1 - films 2 - serials
	"search_err": 0,
}
texts = {
	"about_bot": "Бот був створений студентом академії IT-Step для екзамену."
				 "Подальшу інформацію ви побачите нижче:"
				 "\n\nЗадум бота був у розважальних цілях для пошуку фільмів/сервіалів."
				 "У боті ви можете знайти фільм/серіал за допомогую простого пошуку за жанрами, "
				 "за кодом/назвою та за допомогую рандомайзера."
				 "\n\nУ боті були використані батарейки json, telebot, random."
				 "Для перегляду коду бота ви можете перейти за цим посиланням GitHub: URL",
	"about_us": "User/company info"
}

	# ---- GanresFunc ----
	# ---- GanresFunc ----
def Comedy(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Комедія':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Drama(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Драма':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Action(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Бойовик':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Detectiv(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Детектив':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Fiction(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Фантастика':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Horror(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Жахи':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())

# 	# ---- Codes&Random ----
# 	# ---- Codes&Random ----
def Random(FilmsOrSerials, cid):
	randomized = random.randint(1, len(FilmsOrSerials))
	for film in FilmsOrSerials:
		if randomized == film["film_code"]:
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=first_reply_menu())

def Codes(msg):
	cid = msg.chat.id
	code = msg.text

	if counters["film_serial"] == 1:
		try:
			if int(code) > len(Films) or int(code) <= 0:
				return 1 / 0
			else:
				for film in Films:
					if int(film["film_code"]) == int(code):
						photo = open(film["film_info"]['img'], 'rb')
						bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=search_reply_menu())
		except Exception as wrong_code:
			bot.send_message(cid, CodeErrText(), reply_markup=search_reply_menu())

	elif counters["film_serial"] == 2:
		try:
			if int(code) > len(Serials) or int(code) <= 0:
				return 1 / 0
			else:
				for serial in Serials:
					if int(serial["film_code"]) == int(code):
						photo = open(serial["film_info"]['img'], 'rb')
						bot.send_photo(cid, photo, caption=serial["film_info"]['text'], reply_markup=search_reply_menu())
		except Exception as wrong_code:
			bot.send_message(cid, CodeErrText(), reply_markup=search_reply_menu())

def Names(msg):
	cid = msg.chat.id
	name = msg.text

	if counters["film_serial"] == 1:
		for film in Films:
			if name.lower() == film["film_name"].lower():
				photo = open(film["film_info"]['img'], 'rb')
				bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=search_reply_menu())
				counters["search_err"] = 1


	elif counters["film_serial"] == 2:
		for serial in Serials:
			if name.lower() == serial["film_name"].lower():
				photo = open(serial["film_info"]['img'], 'rb')
				bot.send_photo(cid, photo, caption=serial["film_info"]['text'], reply_markup=search_reply_menu())
				counters["search_err"] = 1

	if counters["search_err"] == 0:
		bot.send_message(cid, NameErrText(), reply_markup=search_reply_menu())

# ---- Return&CodeErr Text ----
# ---- Return&CodeErr Text ----
def ReturnText():
	randomized = random.randint(1, 3)
	if randomized == 1:
		return 'Назад 🧭'
	elif randomized == 2:
		return 'Перехід виконано 👌'
	elif randomized == 3:
		return 'Повернуто назад ✔'

def CodeErrText():
	randomized = random.randint(1, 3)
	if randomized == 1:
		return "Невірний код 🚫"
	elif randomized == 2:
		return "Код недійсний ⚠"
	elif randomized == 3:
		return "Такого коду не має 🥲"

def NameErrText():
	randomized = random.randint(1, 3)
	if randomized == 1:
		return "Невірна назва 🚫"
	elif randomized == 2:
		return "Назва недійсна ⚠"
	elif randomized == 3:
		return "Такої назви не має 🥲"
# --	-- REPLY_MENUS SECTION --	--
# --	-- REPLY_MENUS SECTION --	--

def main_reply_menu():
	markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_main.row(types.KeyboardButton('🎞 Фільми'), types.KeyboardButton('🎬 Серіали'))
	markup_main.row(types.KeyboardButton('📖 Інфо'))
	return markup_main

def first_reply_menu():
	markup_films1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_films1.row(types.KeyboardButton('🔎 Пошук за жанрами'), types.KeyboardButton('🔎 Пошук за назвою/кодом'))
	markup_films1.row(types.KeyboardButton('🎲 Випадкове'), types.KeyboardButton('↩ Назад'))
	return markup_films1

def ganres_reply_menu():
	markup_films2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_films2.row(types.KeyboardButton('😄 Комедія'), types.KeyboardButton('😿 Драми'))
	markup_films2.row(types.KeyboardButton('💣 Бойовики'), types.KeyboardButton('🕵‍♂️ Детектив'))
	markup_films2.row(types.KeyboardButton('🛸 Фантастика'), types.KeyboardButton('👻 Жахи'))
	markup_films2.row(types.KeyboardButton('↩ Назад'))
	return markup_films2

def about_us_reply_menu():
	markup_films2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_films2.row(types.KeyboardButton('💻 Про Бот'), types.KeyboardButton('📃 Про Нас'))
	markup_films2.row(types.KeyboardButton('↩ Назад'))
	return markup_films2

def search_reply_menu():
	markup_films2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_films2.row(types.KeyboardButton('🔎 Пошук за назвою'), types.KeyboardButton('🔎 Пошук за кодом'))
	markup_films2.row(types.KeyboardButton('↩ Назад'))
	return markup_films2

# --	-- COMMANDS --	--
# --	-- COMMANDS --	--

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Початок! Оберіть щось одне 📌", reply_markup=main_reply_menu())

@bot.message_handler(commands=['update'])
def send_welcome(message):
	randomized = random.randint(1, 3)
	if randomized == 1:
		bot.reply_to(message, 'Оновлено 👍', reply_markup=main_reply_menu())
	elif randomized == 2:
		bot.reply_to(message, 'Оновлення виконано ✅', reply_markup=main_reply_menu())
	elif randomized == 3:
		bot.reply_to(message, 'Успішно 😸', reply_markup=main_reply_menu())

# --	-- MSGs --	--
# --	-- MSGs --	--

@bot.message_handler(func=lambda message: True)
def echo_all(msg):
	cid = msg.chat.id

	if msg.text == '🎞 Фільми':
		bot.send_message(cid, '🍿 Фільми - хороший вибір!', reply_markup=first_reply_menu())
		counters['menu_films'] += 1
		counters['film_serial'] = 1
		print(counters['film_serial'])
	elif msg.text == '🎬 Серіали':
		bot.send_message(cid, '🥤 Серіали, чудовий спосіб провести кілька вечорів!', reply_markup=first_reply_menu())
		counters['menu_films'] += 1
		counters['film_serial'] = 2
		print(counters['film_serial'])

# ---	- BACK -	---
# ---	- BACK -	---
	elif msg.text == '↩ Назад' and counters['menu_films'] == 1:
		bot.send_message(cid, ReturnText(), reply_markup=main_reply_menu())
		counters['menu_films'] -= 1
	elif msg.text == '↩ Назад' and counters['menu_films'] == 2:
		bot.send_message(cid, ReturnText(), reply_markup=first_reply_menu())
		counters['menu_films'] -= 1

# ---	- GANRES -	---
# ---	- GANRES -	---
	elif msg.text == '🔎 Пошук за жанрами' and counters['menu_films'] == 1:
		bot.send_message(cid, '🕹 Оберіть жанр', reply_markup=ganres_reply_menu())
		counters['menu_films'] += 1

	elif msg.text == '😄 Комедія':
		if counters['film_serial'] == 1:
			Comedy(Films, cid)
		elif counters['film_serial'] == 2:
			Comedy(Serials, cid)
	elif msg.text == '😿 Драми':
		if counters['film_serial'] == 1:
			Drama(Films, cid)
		elif counters['film_serial'] == 2:
			Drama(Serials, cid)
	elif msg.text == '💣 Бойовики':
		if counters['film_serial'] == 1:
			Action(Films, cid)
		elif counters['film_serial'] == 2:
			Action(Serials, cid)
	elif msg.text == '🕵‍♂️ Детектив':
		if counters['film_serial'] == 1:
			Detectiv(Films, cid)
		elif counters['film_serial'] == 2:
			Detectiv(Serials, cid)
	elif msg.text == '🛸 Фантастика':
		if counters['film_serial'] == 1:
			Fiction(Films, cid)
		elif counters['film_serial'] == 2:
			Fiction(Serials, cid)
	elif msg.text == '👻 Жахи':
		if counters['film_serial'] == 1:
			Horror(Films, cid)
		elif counters['film_serial'] == 2:
			Horror(Serials, cid)
# ---	- RANDOM -	---
# ---	- RANDOM -	---
	elif msg.text == '🎲 Випадкове':
		if counters['film_serial'] == 1:
			Random(Films, cid)
		elif counters['film_serial'] == 2:
			Random(Serials, cid)
# ---	- NAMES&CODES -	---
# ---	- NAMES&CODES -	---
	elif msg.text == '🔎 Пошук за назвою/кодом':
		bot.send_message(cid, "🕹 Оберіть метод пошуку", reply_markup=search_reply_menu())
		counters['menu_films'] += 1

	elif msg.text == '🔎 Пошук за назвою':
		mess = bot.send_message(cid, "Введіть назву:")
		bot.register_next_step_handler(mess, Names)

	elif msg.text == '🔎 Пошук за кодом':
		mess = bot.send_message(cid, "Введіть код:")
		bot.register_next_step_handler(mess, Codes)

# ---	- INFO -	---
# ---	- INFO -	---
	elif msg.text == '📖 Інфо':
		bot.send_message(cid, 'Ось деяка інформація 💾', reply_markup=about_us_reply_menu())
		counters['menu_films'] += 1

	elif msg.text == '💻 Про Бот':
		bot.send_message(cid, texts["about_bot"], reply_markup=about_us_reply_menu())
	elif msg.text == '📃 Про Нас':
		bot.send_message(cid, texts["about_us"], reply_markup=about_us_reply_menu())

bot.infinity_polling()
