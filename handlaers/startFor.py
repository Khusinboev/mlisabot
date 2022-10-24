import pytz
import datetime
from function.functions import *
from databas import *
from key import *
from buttons.mButtons import *
from Statess.statess import From
from aiogram.dispatcher import FSMContext

sent_number = types.ReplyKeyboardMarkup(resize_keyboard=True)
sent_number.add(types.KeyboardButton(text="Raqamni yuborish📱", request_contact=True))

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    user_id = message.chat.id
    sql.execute("""CREATE TABLE IF NOT EXISTS users ("user_id"  INTEGER,"date"  INTEGER, "lang" INTEGER, "tel_Num" INTEGER);""")
    db.commit()
    check = sql.execute(f"""SELECT user_id FROM users WHERE user_id = {user_id}""").fetchone()

    if check == None:
        if message.chat.type == 'private':
            sana = datetime.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%d-%m-%Y %H:%M')
            sql.execute(f"""INSERT INTO users (user_id, date, lang) VALUES ('{user_id}', '{sana}', '{message.from_user.language_code}')""")
            db.commit()

    await message.answer(f"""👋 Assalomu alakum! {message.from_user.first_name}

👮🏻‍♂️ Men guruhlardagi kirdi-chiqdi xabarlarni guruhlardan o'chirib turaman. 

🧑‍💻Ishimni boshlashim uchun meni guruhingizda qo'shing va ADMIN qiling""", reply_markup=join_chat1)

