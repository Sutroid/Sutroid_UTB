import telebot
from telebot import types
import prepared_text as pt
import json
from gtts import gTTS
import requests
import datetime
from googletrans import Translator

# ID создателя: 1755170051

with open('Configs.json', 'r', encoding = 'utf-8') as file:
	jf = json.load(file)

bot = telebot.TeleBot(jf['Bot_Token'], skip_pending=True)

@bot.message_handler(content_types = ['new_chat_members', 'left_chat_member'])
def delete(message):
	bot.delete_message(message.chat.id, message.message_id)

# Реакция на команду старт
@bot.message_handler(commands = ['start'])
def start_command(message):
	mt = message.text.split()

	# Если пишет боту
	if message.chat.type  == 'private':
		bot.send_message(message.chat.id, pt.start_private, parse_mode = 'HTML', disable_notification = True)

# версия бота
@bot.message_handler(commands = ['version'])
def version(message):

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		bot.send_message(message.chat.id, f"{jf['Bot_Version']}", parse_mode = 'HTML', disable_notification = True)

# Узнать ID чата
@bot.message_handler(commands = ['chat_id'])
def chat_id(message):

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		bot.send_message(message.chat.id, f'<b>Chat ID:</b> <i>{message.chat.id}</i>', parse_mode = 'HTML', disable_notification = True)

# Узнать свой ID
@bot.message_handler(commands = ['user_id'])
def user_id(message):

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		bot.send_message(message.chat.id, f'<b>User ID:</b> <i>{message.from_user.id}</i>', parse_mode = 'HTML', disable_notification = True)

# Доступно добавленным пользователям
# Инфо о коммандах
@bot.message_handler(commands = ['info'])
def info(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)
			print('0')

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.send_message(message.chat.id, pt.inf, parse_mode = 'HTML', disable_notification = True)

# Жирный текст
@bot.message_handler(commands = ['news'])
def news(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					bot.send_message(message.chat.id, pt.news, parse_mode = 'HTML', disable_notification = True)

# Стандартный текст
@bot.message_handler(commands = ['r'])
def r(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/r [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						bot.send_message(message.chat.id, res, parse_mode = 'HTML', disable_notification = True)

# Жирный текст
@bot.message_handler(commands = ['b'])
def b(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/b [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						bot.send_message(message.chat.id, f'<b>{res}</b>', parse_mode = 'HTML', disable_notification = True)

# Курсивный текст
@bot.message_handler(commands = ['i'])
def i(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/i [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						bot.send_message(message.chat.id, f'<i>{res}</i>', parse_mode = 'HTML', disable_notification = True)

# Подчеркнутый текст
@bot.message_handler(commands = ['u'])
def u(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/u [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						bot.send_message(message.chat.id, f'<u>{res}</u>', parse_mode = 'HTML', disable_notification = True)

# Микс -i, -u, -b текстов
@bot.message_handler(commands = ['m'])
def m(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/m [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						bot.send_message(message.chat.id, f'<b><i><u>{res}</u></i></b>', parse_mode = 'HTML', disable_notification = True)

# Кликабельный текст
@bot.message_handler(commands = ['link'])
def link(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) <= 2:
						bot.send_message(message.chat.id, f'<b>/link [link] [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[2:])
						bot.send_message(message.chat.id, f'<a href="{mt[1]}">{res}</a>', parse_mode = 'HTML', disable_web_page_preview = True, disable_notification = True)

# Просмотр погоды
@bot.message_handler(commands = ['weather'])
def weather(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					with open('Configs.json', 'r', encoding = 'utf-8') as file:
						jf = json.load(file)

					weather_token = jf['Weather_Token']

					if len(mt) == 1:
						if jf['Group_List'][str(message.chat.id)]['Set_City'] == 'None':
							bot.send_message(message.chat.id, f'<b>❕Вам доступно /weather [City] (С указанием города) для использования без указания города обратитесь к администратору группы</b>', parse_mode = 'HTML', disable_notification = True)

						else:
							city = jf['Group_List'][str(message.chat.id)]['Set_City']
							url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={weather_token}'

							res = requests.get(url)
							inf_city = res.json()

							lat = inf_city[0]['lat']				# Широта
							lon = inf_city[0]['lon']				# Долгота
							city = inf_city[0]["local_names"]["ru"] # Город

							res_link = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}&units=metric&lang=ru'

							res = requests.get(res_link)
							data = res.json()

							city = data['name']						# Город
							temp = data["main"]["temp"]				# Температура
							feels_like = data["main"]["feels_like"]	# Ощущается как
							humidity = data["main"]["humidity"]		# Влажность
							speed = data["wind"]["speed"]			# Скорость ветра
							pressure = data["main"]["pressure"]		# Давление

							bot.send_message(message.chat.id,
								f'<b># # # {datetime.datetime.now().strftime("%Y-%m-%d")} # # #</b>\n\n'
								f'<b>● Город:</b> {city}\n'
								f'<b>● Температура:</b> {int(temp)} °C\n'
								f'<b>● Ощущается:</b> {int(feels_like)}\n'
								f'<b>● Влажность:</b> {humidity} %\n'
								f'<b>● Ветер:</b> {speed} м/c\n'
								f'<b>● Давление:</b> {pressure} мбар\n',
								parse_mode = 'HTML',
								disable_notification = True
								)

					else:
						city = ' '.join(mt[1:])
						url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={weather_token}'

						try:
							res = requests.get(url)
							inf_city = res.json()

							lat = inf_city[0]['lat']                # Широта
							lon = inf_city[0]['lon']                # Долгота
							city = inf_city[0]["local_names"]["ru"] # Город
							error_state = False

						except Exception as ex:
							bot.send_message(message.chat.id, '<b>Weather: Название города введено не верно</b>', parse_mode = 'HTML', disable_notification = True)
							error_state = True
							print(ex)

						if error_state == False:
							res_link = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}&units=metric&lang=ru'

							res = requests.get(res_link)
							data = res.json()

							city = data['name']	                    # Город
							temp = data["main"]["temp"]             # Температура
							feels_like = data["main"]["feels_like"] # Ощущается как
							humidity = data["main"]["humidity"]     # Влажность
							speed = data["wind"]["speed"]           # Скорость ветра
							pressure = data["main"]["pressure"]     # Давление

							bot.send_message(message.chat.id,
								f'<b># # # {datetime.datetime.now().strftime("%Y-%m-%d")} # # #</b>\n\n'
								f'<b>● Город:</b> {city}\n'
								f'<b>● Температура:</b> {int(temp)} °C\n'
								f'<b>● Ощущается:</b> {int(feels_like)}\n'
								f'<b>● Влажность:</b> {humidity} %\n'
								f'<b>● Ветер:</b> {speed} м/c\n'
								f'<b>● Давление:</b> {pressure} мбар\n',
								parse_mode = 'HTML',
								disable_notification = True
								)

# Перевод текста на en
@bot.message_handler(commands = ['gte'])
def gte(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/gte [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						translator = Translator()
						to_en = translator.translate(res, dest = 'en')
						bot.send_message(message.chat.id, to_en.text, parse_mode = 'HTML', disable_notification = True)

# Перевод текста на ru
@bot.message_handler(commands = ['gtr'])
def gtr(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/gte [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						translator = Translator()
						to_ru = translator.translate(res, dest = 'ru')
						bot.send_message(message.chat.id, to_ru.text, parse_mode = 'HTML', disable_notification = True)

# Перевод текста на uk
@bot.message_handler(commands = ['gtu'])
def gtu(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/gte [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						translator = Translator()
						to_uk = translator.translate(res, dest = 'uk')
						bot.send_message(message.chat.id, to_uk.text, parse_mode = 'HTML', disable_notification = True)

# Гинератор QRcode
@bot.message_handler(commands = ['qrcode'])
def qrcode(message):
	import qrcode
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/qrcode [Text / link]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						if len(res) > 1750:
							bot.send_message(message.chat.id, '<b>Длина текста ограничена до 1750 символов</b>', parse_mode = 'HTML', disable_notification = True)

						else:
							img = qrcode.make(res)
							img.save('send_photo.png')

							with open('send_photo.png', 'rb') as file:
								data = file.read()
								bot.send_photo(message.chat.id, data, disable_notification = True)

# Голосовое ru
@bot.message_handler(commands = ['sar'])
def m(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/sar [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						tts = gTTS(res, lang='ru')
						tts.save('send_audio.ogg')
						with open('send_audio.ogg', 'rb') as audio:
							bot.send_voice(message.chat.id, audio)

# Голосовое en
@bot.message_handler(commands = ['sae'])
def m(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)
		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе
				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/sae [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						tts = gTTS(res, lang='en')
						tts.save('send_audio.ogg')
						with open('send_audio.ogg', 'rb') as audio:
							bot.send_voice(message.chat.id, audio)

# Голосовое uk
@bot.message_handler(commands = ['sau'])
def m(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Обычный чел
				try:
					user_presence = False
					for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
						if int(i) == message.from_user.id:
							user_presence = True

				except Exception as ex:
					print(ex)

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if user_presence == True or TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/sau [Text]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						tts = gTTS(res, lang='uk')
						tts.save('send_audio.ogg')
						with open('send_audio.ogg', 'rb') as audio:
							bot.send_voice(message.chat.id, audio)

# Доступно администратору группы
# добавить ID в группу
@bot.message_handler(commands = ['del'])
def del_(message):
	mt = message.text.split()
	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) == 1:
						bot.send_message(message.chat.id, f'<b>/del [User ID]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						try:
							s = int(mt[1])
							state = True

						except:
							state = False

						if state == False:
							bot.send_message(message.chat.id, '<b>ID указан не верно</b>', parse_mode = 'HTML', disable_notification = True)

						elif state == True:
							with open('Configs.json', 'r', encoding = 'utf-8') as file:
								jf = json.load(file)

							state = False
							for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
								if i == mt[1]:
									state = True

							if state == False:
								bot.send_message(message.chat.id, '<b>Указаного вами ID нет в списке</b>', parse_mode = 'HTML', disable_notification = True)

							elif state == True:
								del jf['Group_List'][str(message.chat.id)]['Group_User'][mt[1]]
								with open('Configs.json', 'w', encoding = 'utf-8') as file:
									json.dump(jf, file, ensure_ascii=False, indent = 4)
									bot.send_message(message.chat.id, '<b>ID успешно удалено</b>', parse_mode = 'HTML', disable_notification = True)

# Дать право пользоваться ботом
@bot.message_handler(commands = ['add'])
def add(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					if len(mt) <= 2:
						bot.send_message(message.chat.id, f'<b>/add [id] [name]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						if len(mt[1]) > 15:
							bot.send_message(message.chat.id, '<b>Длина ID ограничена до 15-ти символов</b>', parse_mode = 'HTML', disable_notification = True)

						else:
							state = False
							try:
								s = int(mt[1])
								state = True

							except:
								state = False

							if state == False:
								bot.send_message(message.chat.id, '<b>ID указан не верно</b>', parse_mode = 'HTML', disable_notification = True)

							elif state == True:
								res = ' '.join(mt[2:])
								if len(res) > 13:
									bot.send_message(message.chat.id, '<b>Ограничение 13 символов в имени</b>', parse_mode = 'HTML', disable_notification = True)

								else:
									for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
										if i == mt[1]:
											state = False

									if state == True:
										res = ' '.join(mt[2:])
										jf['Group_List'][str(message.chat.id)]['Group_User'][mt[1]] = res

										with open('configs.json', 'w', encoding = 'utf-8') as file:
											json.dump(jf, file, ensure_ascii=False, indent = 4)
											bot.send_message(message.chat.id, f'<b>ID успешно добавлен</b>', parse_mode = 'HTML', disable_notification = True)

									else:
										bot.send_message(message.chat.id, '<b>ID уже есть в списке</b>', parse_mode = 'HTML', disable_notification = True)

# Установить стандартный город для показания погоды
@bot.message_handler(commands = ['set_city'])
def set_city(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if TAI == True or group_admin == True:

					# Основная функция
					if len(mt) == 1:
						bot.send_message(message.chat.id, '<b>/set_city [City]</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						res = ' '.join(mt[1:])
						if res.lower() == 'none':
							jf['Group_List'][str(message.chat.id)]['Set_City'] = "None"
							bot.send_message(message.chat.id, '<b>Weather: Сброс до None</b>', parse_mode = 'HTML', disable_notification = True)
							with open('Configs.json', 'w', encoding = 'utf-8') as file:
								json.dump(jf, file, ensure_ascii = False, indent = 4)

						else:
							try:
								with open('Configs.json', 'r', encoding = 'utf-8') as file:
									jf = json.load(file)

								weather_token = jf['Weather_Token']
								url = f'http://api.openweathermap.org/geo/1.0/direct?q={res}&limit=1&appid={weather_token}'
								res_test = requests.get(url)
								data = res_test.json()
								error_test = data[0]['lat']
								error_test = data[0]['lon']
								error_state = False

							except Exception as ex:
								error_state = True
								print(ex)

							if error_state == True:
								bot.send_message(message.chat.id, '<b>Weather: Город введён не коректно</b>', parse_mode = 'HTML', disable_notification = True)

							elif error_state == False:
								jf['Group_List'][str(message.chat.id)]['Set_City'] = str(res)
								with open('Configs.json', 'w', encoding = 'utf-8') as file:
									json.dump(jf, file, ensure_ascii = False, indent = 4)

								bot.send_message(message.chat.id, f'<b>Weather: Город обновлён на: {res}</b>', parse_mode = 'HTML', disable_notification = True)

# Комманды Админа
@bot.message_handler(commands = ['info_admin'])
def info_admin(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if TAI == True or group_admin == True:

					# Основная функция
					bot.send_message(message.chat.id, pt.info_Admin, parse_mode = 'HTML', disable_notification = True)


# Список кто может пользоватся ботом в этом чате
@bot.message_handler(commands = ['list'])
def list(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка групы
		for i in jf['Group_List']:
			if int(i) == message.chat.id:
				# Проверка на наличие в группе

				# Тех админ
				try:
					TAI = False
					for i in jf['Tech_Admin_ID']:
						if i == message.from_user.id:
							TAI = True

				except Exception as ex:
					print(ex)

				# Админ группы
				try:
					group_admin = False
					if jf['Group_List'][str(message.chat.id)]['Group_Admin'] == message.from_user.id:
						group_admin = True

				except Exception as ex:
					print(ex)

				# Проверка на наличие хоть кого то
				if TAI == True or group_admin == True:

					# Основная функция
					bot.delete_message(message.chat.id, message.message_id)
					list_str = []
					if len(jf['Group_List'][str(message.chat.id)]['Group_User']) == 0:
						bot.send_message(message.chat.id, '<b>На данный момент никто не может использовать бота в этом чате</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						for i in jf['Group_List'][str(message.chat.id)]['Group_User']:
							try:
								b1 = int(i)
								list_str.append(f'<b>{i} =</b> <i>{jf["Group_List"][str(message.chat.id)]["Group_User"][i]}</i>')

							except:
								pass

						ssp1 = "\n".join(map(str, list_str))
						bot.send_message(message.chat.id, f'<b>:: Allowed ID ::</b>\n\n'+f'{ssp1}\n\n<b>Group:</b> <i>{message.chat.id}</i>', parse_mode = 'HTML', disable_notification = True)

# Доступно только тех админам
# Добавить группу
@bot.message_handler(commands = ['add_group'])
def add_group(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:
			# Основная функция

			if len(mt) < 4:
				bot.send_message(message.chat.id, '<b>/add_group [Group ID] [Group Name] [Admin ID] [Link Chat]</b>', parse_mode = 'HTML', disable_notification = True)

			else:
				if len(mt[1]) > 15 or len(mt[1]) > 15:
					bot.send_message(message.chat.id, '<b>Ограничена длина ID до 15 символов</b>', parse_mode = 'HTML', disable_notification = True)

				else:
					if len(mt[2]) > 15:
						bot.send_message(message.chat.id, '<b>Ограничена длина имени до 15 символов</b>', parse_mode = 'HTML', disable_notification = True)

					else:
						try:
							s = int(mt[1])
							s = int(mt[3])
							state = True

						except:
							state = False

						if state == False:
							bot.send_message(message.chat.id, '<b>Не верно указано ID</b>', parse_mode = 'HTML', disable_notification = True)

						else:
							state = False
							for i in jf['Group_List']:
								if i == mt[1]:
									state = True

							if state == True:
								bot.send_message(message.chat.id, '<b>Группа с таким ID уже существует</b>', parse_mode = 'HTML', disable_notification = True)

							else:
								if len(mt) == 4:
									jf['Group_List'][mt[1]] = {
										"Group_Name": mt[2],
										"Set_City": "None",
										"Group_Admin": int(mt[3]),
										"Group_Link": "NULL",
										"Group_User": {}
									}

									with open('Configs.json', 'w', encoding = 'utf-8') as file:
										json.dump(jf, file, ensure_ascii = False, indent = 4)
										
									bot.send_message(message.chat.id, f'<b>◾️Создана группа:</b>\n\n<b>◾️ID:</b> <i>{mt[1]}</i>\n<b>◾️Name:</b> <i>{mt[2]}</i>\n<b>◾️Admin:</b> <i>{mt[3]}</i>\n<b>◾️Link:</b> <i>NULL</i>', parse_mode = 'HTML', disable_notification = True)
								
								elif len(mt) >= 5:
									jf['Group_List'][mt[1]] = {
										"Group_Name": mt[2],
										"Set_City": "None",
										"Group_Admin": int(mt[3]),
										"Group_Link": f"<a href='{mt[4]}'>click</a>",
										"Group_User": {}
									}

									with open('Configs.json', 'w', encoding = 'utf-8') as file:
										json.dump(jf, file, ensure_ascii = False, indent = 4)
									
									bot.send_message(message.chat.id, f'<b>◾️Создана группа:</b>\n\n<b>◾️ID:</b> <i>{mt[1]}</i>\n<b>◾️Name:</b> <i>{mt[2]}</i>\n<b>◾️Admin:</b> <i>{mt[3]}</i>\n<b>◾️Link:</b> <i><a href="{mt[4]}">click</a></i>', parse_mode = 'HTML', disable_notification = True)

# Список всех груп
@bot.message_handler(commands = ['list_group'])
def list_group(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			if len(jf['Group_List']) == 0:
				bot.send_message(message.chat.id, '<b>На данный момент нет никаких груп</b>', parse_mode = 'HTML', disable_notification = True)


			else:
				for i in jf['Group_List']:
					for s in jf['Group_List'][i]:
						jName = jf['Group_List'][i]['Group_Name']
						jAdmin = jf['Group_List'][i]['Group_Admin']
						jLink = jf['Group_List'][i]['Group_Link']
						jUser = len(jf['Group_List'][i]['Group_User'])

					bot.send_message(message.chat.id, f'<b>Name:</b> <i>{jName}</i>\n<b>ID:</b> <i>{i}</i>\n<b>Admin:</b> <i>{jAdmin}</i>\n<b>Link:</b> <i>{jLink}</i>\n<b>Users:</b> <i>{jUser}</i>', parse_mode = 'HTML', disable_notification = True, disable_web_page_preview = True)

# Удалить группу
@bot.message_handler(commands = ['del_group'])
def del_group(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			if len(mt) < 2:
				bot.send_message(message.chat.id, '<b>/del_group [Group ID]</b>', parse_mode = 'HTML', disable_notification = True)

			else:
				state = False
				for i in jf['Group_List']:
					if int(i) == int(mt[1]):
						state = True

				if state == True:
					del jf['Group_List'][mt[1]]
					with open('Configs.json', 'w', encoding = 'utf-8') as file:
						json.dump(jf, file, ensure_ascii = False, indent = 4)

					bot.send_message(message.chat.id, '<b>Группа успешно удалена</b>', parse_mode = 'HTML', disable_notification = True)

# Отправить сообщение во все группы
@bot.message_handler(commands = ['ste'])
def ste(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			groups = []
			for i in jf['Group_List']:
				groups.append(int(i))

			if len(mt) == 1:
				bot.send_message(message.chat.id, f'<b>/ste [Text]</b>', parse_mode = 'HTML', disable_notification = True)

			else:
				res = ' '.join(mt[1:])
				for i in groups:
					bot.send_message(int(i), res, parse_mode = 'HTML', disable_notification = True)

# Вышла обнова
@bot.message_handler(commands = ['sten'])
def sten(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			for i in jf['Group_List']:
				bot.send_message(int(i), f'{pt.news}\n\n<b>Обновлено до:</b> {jf["Bot_Version"]}', parse_mode = 'HTML', disable_notification = True)

# скачать Configs.json
@bot.message_handler(commands = ['load_json'])
def load_json(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			bot.send_document(message.chat.id, data = open('Configs.json', 'rb'), disable_notification = True)

# Добавить тех админа
@bot.message_handler(commands = ['tai_add'])
def tai_add(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			if len(mt) == 1:
				bot.send_message(message.chat.id, '<b>/tai_add [User ID]</b>', parse_mode = 'HTML', disable_notification = True)

			else:
				try:
					s = int(mt[1])
					state = True

				except:
					state = False

				if state == False:
					bot.send_message(message.chat.id, '<b>ID введено не верно</b>', parse_mode = 'HTML', disable_notification = True)

				elif state == True:
					state = False
					for i in jf['Tech_Admin_ID']:
						if s == i:
							state = True

					if state == True:
						bot.send_message(message.chat.id, '<b>Такой ID уже записан</b>', parse_mode = 'HTML', disable_notification = True)

					elif state == False:
						jf['Tech_Admin_ID'].append(s)
						with open('Configs.json', 'w', encoding = 'utf-8') as file:
							json.dump(jf, file, ensure_ascii = False, indent = 4)

						bot.send_message(message.chat.id, '<b>ID Успешно записан</b>', parse_mode = 'HTML', disable_notification = True)

# Удалить тех админа
@bot.message_handler(commands = ['tai_del'])
def tai_del(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			if len(mt) == 1:
				bot.send_message(message.chat.id, '<b>/tai_add [User ID]</b>', parse_mode = 'HTML', disable_notification = True)

			else:
				try:
					s = int(mt[1])
					state = True

				except:
					state = False

				if state == False:
					bot.send_message(message.chat.id, '<b>ID введено не верно</b>', parse_mode = 'HTML', disable_notification = True)

				elif state == True:
					state = False

					for i in jf['Tech_Admin_ID']:
						if s == i:
							state = True

					if state == False:
						bot.send_message(message.chat.id, '<b>Такого ID нет в списке</b>', parse_mode = 'HTML', disable_notification = True)

					elif state == True:
						jf['Tech_Admin_ID'].remove(s)
						with open('Configs.json', 'w', encoding = 'utf-8') as file:
							json.dump(jf, file, ensure_ascii = False, indent = 4)

						bot.send_message(message.chat.id, '<b>ID Успешно удалён</b>', parse_mode = 'HTML', disable_notification = True)

# Список тех админов
@bot.message_handler(commands = ['tai_list'])
def tai_list(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			tail = []
			count = 1
			for i in jf['Tech_Admin_ID']:
				if i == message.from_user.id:
					tail.append(f'<b>[{count}]</b> <i>{i}</i> -ваш')
					count = count + 1

				else:
					tail.append(f'<b>[{count}]</b> <i>{i}</i>')
					count = count + 1

			res = '\n'.join(tail)
			bot.send_message(message.chat.id, f'<b>:: Tech Admin List ::</b>\n\n{res}', parse_mode = 'HTML', disable_notification = True)

# Комманды тех админа
@bot.message_handler(commands = ['info_tai'])
def info_tai(message):
	mt = message.text.split()

	# Если пишет боту или в группу
	if message.chat.type  == 'private' or message.chat.type  == 'group' or message.chat.type  == 'supergroup':
		with open('Configs.json', 'r', encoding = 'utf-8') as file:
			jf = json.load(file)

		# Проверка на тех админа
		state = False
		for i in jf['Tech_Admin_ID']:
			if message.from_user.id == i:
				state = True

		if state == True:

			# Основная функция
			bot.send_message(message.chat.id, pt.info_TAI, parse_mode = 'HTML', disable_notification = True)

bot.polling(none_stop=True,interval=0)