import json

with open('Configs.json', 'r', encoding = 'utf-8') as file:
	jf = json.load(file)

start_private = f'''<b><i>❕Для того чтоб получить доступ к боту, вам нужно:</i></b> <i><b>\n1)</b> Добавить бота в группу <b>\n2)</b> Дать боту права администратора <b>\n<b>3) Предоставить Тех админу ссылку на группу</b>\n4)</b> Предоставить Тех Админу ID чата (группы) и ID человека которому будет выдана возможность разрешать или запрещать пользоватся ботом в группе конкретным людям</i>\n\n<b><i>Доступные комманды:</i></b>\n<b>/user_id</b> <i>Узнать свой ID</i>\n<b>/chat_id</b> <i>Узнать ID текущего чата</i>\n<b>/version</b> <i>Версия бота</i>\n\n<b>Тех Админ: {jf['Tech_Admin']}</b>'''
inf = '''<b>:: Command Info ::</b>

<b>/r [Text]</b> <i>Стандартный текст</i>
<b>/i [Text]</b> <i>Курсивный текст</i>
<b>/u [Text]</b> <i>Подчеркнутый текст</i>
<b>/b [Text]</b> <i>Жирный текст</i>
<b>/m [Text]</b> <i>Микс курсивного жирного и подчеркнутого текста</i>
<b>/link [Link] [Text]</b> <i>Кликабельный текст</i>
<b>/sar [Text]</b> <i>Голосовое сообщение с руским акцентом</i>
<b>/sae [Text]</b> <i>Голосовое сообщение с английским акцентом</i>
<b>/sau [Text]</b> <i>Голосовое сообщение с украинским акцентом</i>
<b>/gte [Text]</b> <i>Перевод текста на Английский</i>
<b>/gtr [Text]</b> <i>Перевод текста на руский</i>
<b>/gtu [Text]</b> <i>Перевод текста на Украинский</i>
<b>/qrcode [Text / Link]</b> <i>Гинератор QRcode с сылкой или же текстом</i>
<b>/weather</b> <i>Погодная характеристика на сегодня (можно указать город)</i>
<b>/info</b> <i>Показать все доступные команды</i>
<b>/news</b> <i>Список новых комманд после обновления</i>
<b>/version</b> <i>Версия бота</i>
<b>/user_id</b> <i>Узнать свой ID</i>
<b>/chat_id</b> <i>Узнать ID чата</i>'''
info_Admin = '''<b>:: Command Admin ::</b>

<b>/add [User ID] [Name]</b> <i>Дать возможность пользоваться ботом</i>
<b>/del [User ID]</b> <i>Отнять возможность пользоваться ботом</i>
<b>/list</b> <i>Список тех кто может пользоваться ботом</i>
<b>/set_city</b> <i>Указать стандартный город для прогноза погоды</i>
<b>/info_admin</b> <i>Список команд админа</i>'''
info_TAI = '''<b>:: Command Tech Admin ::</b>

<b>/add_group [Group ID] [Group Name] [Admin ID] [Link Chat]</b> <i>Добавить группу</i>
<b>/del_group [Group ID]</b> <i>Удалить группу</i>
<b>/list_group</b> <i>Список всех груп</i>
<b>/tai_add [User ID]</b> <i>Добавить тех админа</i>
<b>/tai_del [User ID]</b> <i>Удалить тех админа</i>
<b>/tai_list</b> <i>Добавить тех админа</i>
<b>/ste [Text]</b> <i>[ send to everyone ] Отправить сообщение всем группам</i>
<b>/sten </b> <i>[ send to everyone news ] Уведомить все группы о новых возможностях после одновления</i>
<b>/load_json</b> <i>скачать config.json</i>
<b>/info_tai</b> <i>Комманды тех админа</i>'''
news = f'''<b>:: Нововведения ::</b>

<b>/weather</b> <i>Погодная характеристика на сегодня (можно указать город)</i>
<b>/gte [Text]</b> <i>Перевод текста на Английский</i>
<b>/gtr [Text]</b> <i>Перевод текста на руский</i>
<b>/gtu [Text]</b> <i>Перевод текста на Украинский</i>
'''
