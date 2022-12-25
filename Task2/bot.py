from telebot import TeleBot, types

TOKEN = ''

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Произвести вычисления')
    item2 = types.KeyboardButton('Вывести log')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_menu_first(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Произвести вычисления':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Вычисление рациональных чисел')
            item2 = types.KeyboardButton('Вычисление комплексных чисел')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выберите операцию', reply_markup=markup)
            bot.register_next_step_handler(message, bot_menu_second)

        elif message.text == 'Вывести log':
            pass
            # bot.register_next_step_handler(message, )    
        
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Произвести вычисления')
            item2 = types.KeyboardButton('Вывести log')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю такую команду. Введите start')

def bot_menu_second(message: types.Message):
    if message.text == 'Вычисление рациональных чисел':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('+')
        item2 = types.KeyboardButton('-')
        item3 = types.KeyboardButton('*')
        item4 = types.KeyboardButton('/')
        back = types.KeyboardButton('Назад')

        markup.add(item1, item2, item3, item4, back)
        bot.send_message(message.chat.id, 'Выберите операцию', reply_markup=markup)
        
        bot.register_next_step_handler(message, rational_operati)

    elif message.text == 'Вычисление комплексных чисел':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('+')
        item2 = types.KeyboardButton('-')
        item3 = types.KeyboardButton('*')
        item4 = types.KeyboardButton('/')
        back = types.KeyboardButton('Назад')

        markup.add(item1, item2, item3, item4, back)
        bot.send_message(message.chat.id, 'Выберите операцию', reply_markup=markup)

        # bot.register_next_step_handler(message, complex_operations)

def rational_operati(message: types.Message):
    operation = message.text

    if operation == '+':
        bot.send_message(message.chat.id, 'Введите числа, через пробел')
        bot.register_next_step_handler(message, operation_1)

    elif operation == '-':
        bot.send_message(message.chat.id, 'Введите числа, через пробел')
        bot.register_next_step_handler(message, operation_2)

    elif operation == '*':
        bot.send_message(message.chat.id, 'Введите числа, через пробел')
        bot.register_next_step_handler(message, operation_3)

    elif operation == '/':
        bot.send_message(message.chat.id, 'Введите числа, через пробел')
        bot.register_next_step_handler(message, operation_4)

def operation_1(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')

def operation_2(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')

def operation_3(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')

def operation_4(msg):
    a, b = map(int, msg.text.split())
    if b == 0:
        bot.send_message(chat_id=msg.from_user.id, text=f'Делить на ноль нельзя!')
    else:    
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')

bot.polling(non_stop=True)

