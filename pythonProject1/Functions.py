import json
import random

with open('Films.json', 'r', encoding='utf-8') as file_films:
	Films = json.load(file_films)
with open('Serials.json', 'r', encoding='utf-8') as file_serials:
	Serials = json.load(file_serials)

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
	# ---- Codes&Random ----
	# ---- Codes&Random ----
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
						bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=first_reply_menu())
		except Exception as wrong_code:
			bot.send_message(cid, CodeErrText(), reply_markup=first_reply_menu())

	elif counters["film_serial"] == 2:
		try:
			if int(code) > len(Serials) or int(code) <= 0:
				return 1 / 0
			else:
				for serial in Serials:
					if int(serial["film_code"]) == int(code):
						photo = open(serial["film_info"]['img'], 'rb')
						bot.send_photo(cid, photo, caption=serial["film_info"]['text'], reply_markup=first_reply_menu())
		except Exception as wrong_code:
			bot.send_message(cid, CodeErrText(), reply_markup=first_reply_menu())

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
