from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    Message,
)

BOT_TOKEN = '7964586647:AAH6OpF8PBINDn0Cg5R31u0zlNp1dFzCXrk'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

light_db = {
    'balance': 0,
    'rashod': 0,
    'zarabotok': 0,
    'summar': 0,
}

# Флаги для отслеживания режима изменения
changing_mode = None  # 'balance', 'rashod', 'zarabotok'

# Клавиатура главного меню
kb_builder = ReplyKeyboardBuilder()
balance = KeyboardButton(text='баланс💸')
rashod = KeyboardButton(text='расходы❗️')
summar = KeyboardButton(text='итоговая сумма')
zarabotok = KeyboardButton(text='заработок✅')
kb_builder.row(balance, width=1)
kb_builder.row(zarabotok, rashod, width=2)
kb_builder.row(summar, width=1)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)

# Клавиатура для раздела баланса
balance_builder = ReplyKeyboardBuilder()
change_balance = KeyboardButton(text='изменить баланс')
back_to_menu = KeyboardButton(text='назад в меню')
balance_builder.row(change_balance, back_to_menu, width=2)
balance_keyboard: ReplyKeyboardMarkup = balance_builder.as_markup(resize_keyboard=True)

# Клавиатура для раздела расходов
rashod_builder = ReplyKeyboardBuilder()
change_rashod = KeyboardButton(text='изменить расходы')
back_to_menu_rashod = KeyboardButton(text='назад в меню')
rashod_builder.row(change_rashod, back_to_menu_rashod, width=2)
rashod_keyboard: ReplyKeyboardMarkup = rashod_builder.as_markup(resize_keyboard=True)

# Клавиатура для раздела заработка
zarabotok_builder = ReplyKeyboardBuilder()
change_zarabotok = KeyboardButton(text='изменить заработок')
back_to_menu_zarabotok = KeyboardButton(text='назад в меню')
zarabotok_builder.row(change_zarabotok, back_to_menu_zarabotok, width=2)
zarabotok_keyboard: ReplyKeyboardMarkup = zarabotok_builder.as_markup(resize_keyboard=True)

@dp.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text='Это бот менеджер\n чтобы начать работу, пропишите команду /menu\n для поддержки писать @Levvis22')

@dp.message(Command('menu'))
async def main(message: Message):
    global changing_mode
    changing_mode = None
    await message.answer('выберите действие', reply_markup=keyboard)

@dp.message(F.text == 'баланс💸')
async def show_balance(message: Message):
    global changing_mode
    changing_mode = None
    await message.answer(
        f'ваш баланс: {light_db["balance"]}\n\n'
        'Что хотите сделать?',
        reply_markup=balance_keyboard
    )

@dp.message(F.text == 'расходы❗️')
async def show_expenses(message: Message):
    global changing_mode
    changing_mode = None
    await message.answer(
        f'ваши расходы: {light_db["rashod"]}\n\n'
        'Что хотите сделать?',
        reply_markup=rashod_keyboard
    )

@dp.message(F.text == 'заработок✅')
async def show_income(message: Message):
    global changing_mode
    changing_mode = None
    await message.answer(
        f'ваш заработок: {light_db["zarabotok"]}\n\n'
        'Что хотите сделать?',
        reply_markup=zarabotok_keyboard
    )

@dp.message(F.text == 'итоговая сумма')
async def show_summ(message:Message):
    ans = light_db['balance'] - light_db['rashod'] + light_db['zarabotok']
    await message.answer(f'ваша итоговая сумма: {ans}')

@dp.message(F.text == 'изменить баланс')
async def change_balance_handler(message: Message):
    global changing_mode
    changing_mode = 'balance'
    await message.answer(
        'Введите новое значение баланса:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='отмена')]],
            resize_keyboard=True
        )
    )

@dp.message(F.text == 'изменить расходы')
async def change_rashod_handler(message: Message):
    global changing_mode
    changing_mode = 'rashod'
    await message.answer(
        'Введите новое значение расходов:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='отмена')]],
            resize_keyboard=True
        )
    )

@dp.message(F.text == 'изменить заработок')
async def change_zarabotok_handler(message: Message):
    global changing_mode
    changing_mode = 'zarabotok'
    await message.answer(
        'Введите новое значение заработка:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='отмена')]],
            resize_keyboard=True
        )
    )

@dp.message(F.text == 'отмена')
async def cancel_change(message: Message):
    global changing_mode
    changing_mode = None
    await message.answer('Изменение отменено', reply_markup=keyboard)

@dp.message(F.text == 'назад в меню')
async def back_to_main_menu(message: Message):
    global changing_mode
    changing_mode = None
    await message.answer('возврат в главное меню', reply_markup=keyboard)

# Общий обработчик для ввода новых значений
@dp.message()
async def handle_value_input(message: Message):
    global changing_mode
    
    if changing_mode:
        try:
            new_value = int(message.text)
            if changing_mode == 'balance':
                light_db['balance'] = new_value
                await message.answer(f'✅ Баланс изменен на: {new_value}', reply_markup=balance_keyboard)
            elif changing_mode == 'rashod':
                light_db['rashod'] = new_value
                await message.answer(f'✅ Расходы изменены на: {new_value}', reply_markup=rashod_keyboard)
            elif changing_mode == 'zarabotok':
                light_db['zarabotok'] = new_value
                await message.answer(f'✅ Заработок изменен на: {new_value}', reply_markup=zarabotok_keyboard)
            
            changing_mode = None
            
        except ValueError:
            await message.answer('❌ Пожалуйста, введите целое число:')

if __name__ == "__main__":
    print("Бот запускается...")
    dp.run_polling(bot)