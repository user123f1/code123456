import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# здесь нужно указать токен вашего бота
bot = telebot.TeleBot('YOUR_TOKEN')

# здесь нужно указать логин Telegram пользователя, который будет иметь доступ к боту
authorized_user = 'YOUR_USERNAME'

# здесь нужно указать список названий кнопок, которые будут отображаться на главном экране
buttons = ['Кнопка 1', 'Кнопка 2', 'Кнопка 3', 'Кнопка 4', 'Кнопка 5',
           'Кнопка 6', 'Кнопка 7', 'Кнопка 8', 'Кнопка 9', 'Кнопка 10',
           'Кнопка 11', 'Кнопка 12', 'Кнопка 13', 'Кнопка 14', 'Кнопка 15',
           'Кнопка 16', 'Кнопка 17', 'Кнопка 18', 'Кнопка 19', 'Кнопка 20',
           'Кнопка 21', 'Кнопка 22', 'Кнопка 23', 'Кнопка 24', 'Кнопка 25',
           'Кнопка 26', 'Кнопка 27', 'Кнопка 28', 'Кнопка 29', 'Кнопка 30']

# здесь нужно указать список статусов, которые могут выбираться для каждой кнопки
statuses = ['Присутствует', 'Отсутствует', 'Болеет']

# здесь будет храниться информация о выбранных статусах для каждой кнопки
status_data = {button: '' for button in buttons}

# главный экран
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        markup.add(KeyboardButton(button))
    return markup

# меню выбора статуса для конкретной кнопки
def status_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for status in statuses:
        markup.add(KeyboardButton(status))
    markup.add(KeyboardButton('Вернуться обратно'))
    return markup

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # проверяем, что пользователь имеет доступ к боту
    if message.from_user.username != authorized_user:
        bot.send_message(message.chat.id, 'У вас нет доступа к этому боту!')
        return
    # отправляем главное меню
    bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=main_menu())

# обработчик нажатия на кнопку на главном экране
@bot.message_handler(func=lambda message: message.text in buttons)
def button_pressed(message):
    # запоминаем, какая кнопка была нажата
    button = message.text
    # отправляем меню выбора статуса
    bot.send_message(message.chat.id, 'Выберите статус для кнопки "{}"'.format(button), reply_markup=status_menu())

# обработчик нажатия на кнопку в меню выбора статуса
@bot.message_handler(func=lambda message: message.text in statuses or message.text == 'Вернуться обратно')
def status_selected(message):
# получаем кнопку, для которой выбирается статус
button = status_data.keys()[list(status_data.values()).index('')]
# проверяем, что пользователь имеет доступ к боту
if message.from_user.username != authorized_user:
bot.send_message(message.chat.id, 'У вас нет доступа к этому боту!')
return
# обновляем информацию о выбранном статусе
if message.text in statuses:
status_data[button] = message.text
bot.send_message(message.chat.id, 'Статус для кнопки "{}" был успешно обновлен'.format(button))
# отправляем главное меню
bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=main_menu())

обработчик команды /report
@bot.message_handler(commands=['report'])
def report(message):
# проверяем, что пользователь имеет доступ к боту
if message.from_user.username != authorized_user:
bot.send_message(message.chat.id, 'У вас нет доступа к этому боту!')
return
# формируем отчет
report_text = 'Отчет:\n\n'
for button, status in status_data.items():
report_text += '{}: {}\n'.format(button, status)
# отправляем отчет
bot.send_message(message.chat.id, report_text)

запускаем бота
bot.polling()