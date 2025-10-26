# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()
# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, width=1)
# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=keyboard
    )